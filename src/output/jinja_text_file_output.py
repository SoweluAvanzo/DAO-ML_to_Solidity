
import src.output.text_file_output as tfo
import src.files.file_utils as fu
import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.model_converter_base as mcb
#import src.postprocessing.output_preparation.templates.jinja.model_to_template_mapper_jinja as mtt_mapper_j
import src.postprocessing.model_conversion.solidity.solidity_converter_general as stg

# TODO 2025-08-10 DA SISTEMARE

class JinjaTextFileOutput(tfo.TextFileOutput):
    def __init__(self, pipeline_item_data: pi.PIData, \
                key_translated_diagram:str, \
                key_model_to_template_mapper_jinja:str, \
                base_destination=None \
                ):
        super().__init__(pipeline_item_data, base_destination)
        self.key_translated_diagram = key_translated_diagram
        self.key_model_to_template_mapper_jinja = key_model_to_template_mapper_jinja
        self.current_inputs = None

    def run(self, inputs:dict):
        self.current_inputs = inputs
        r = super().run(inputs)
        self.current_inputs = None
        return r
        

    def to_output(self, what, destination:str=None, additional_data=None) -> bool:
        ok = True
        translated_diagram = self.current_inputs[self.key_translated_diagram]
        model_to_template_mapper_jinja = self.current_inputs[self.key_model_to_template_mapper_jinja]
        if not isinstance(translated_diagram, stg.TranslatedDiagram):
            raise Exception(f"The provided translated diagram should be an instance of TranslatedDiagram, but it's a: {type(translated_diagram)}")
        if not isinstance(model_to_template_mapper_jinja, mtt_mapper_j.ModelToTemplateMapperJinja):
            raise Exception(f"The provided model_to_template_mapper_jinja should be an instance of ModelToTemplateMapperJinja, but it's a: {type(model_to_template_mapper_jinja)}")

        def append_template_filename_output(array:list, translated_data:mcb.ModelConversionResultBase, template_filename ):
            if isinstance(template_filename, str):
                array.append((translated_data, template_filename))
            elif isinstance(template_filename, list):
                array.extend([ (translated_data, tf) for tf in template_filename])
            elif isinstance(template_filename, dict) or isinstance(template_filename, map):
                array.extend([ (translated_data, template_filename[ktf]) for ktf in template_filename.keys()])
            return array

        # start with diagram ....
        content_and_filepath_to_output = append_template_filename_output( \
            [], \
            translated_diagram.diagram_specific_data, \
            model_to_template_mapper_jinja.get_template_filename_by_key(translated_diagram) \
            ) \
            if model_to_template_mapper_jinja.has_template_filename_for_key(translated_diagram) else []
        # ... then DAOs ...
        for dao_id in translated_diagram.daos_by_id.keys():
            if model_to_template_mapper_jinja.has_template_filename_for_key(translated_diagram.daos_by_id[dao_id]):
                dao = translated_diagram.daos_by_id[dao_id]
                append_template_filename_output( \
                    content_and_filepath_to_output, \
                    dao, \
                    model_to_template_mapper_jinja.get_template_filename_by_key(dao) \
                )
                # ... then committees ...
                for committee_id in dao.committees_by_id.keys():
                        committee = dao.committees_by_id[committee_id]
                        append_template_filename_output( \
                            content_and_filepath_to_output, \
                            committee, \
                            model_to_template_mapper_jinja.get_template_filename_by_key(committee) \
                        )
                    # ... then ... what? is there something specific to each committee?
        # then, produce the output  
        for output_and_filepath in content_and_filepath_to_output:
            output_to_print = output_and_filepath[0]
            filepath = output_and_filepath[1]
            try:
                ok &= super().to_output(output_to_print, filepath, additional_data)
            except Exception as e:
                print(f"ERROR while outputting some Jinja compiled thing into: {filepath}")
                print(e)

        return ok