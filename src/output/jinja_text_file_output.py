
import src.output.text_file_output as tfo
import src.files.file_utils as fu
import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.templates.jinja.model_to_template_mapper_jinja as mtt_mapper_j
import src.postprocessing.model_conversion.solidity.solidity_translator_general as stg

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

        content_and_filepath_to_output = [
            (translated_diagram.diagram_specific_data, model_to_template_mapper_jinja.get_template_filename_by_key(translated_diagram)) \
            if model_to_template_mapper_jinja.has_template_filename_for_key(translated_diagram) else None,
        ]
        """
        TODO: aggiungere uno per uno, perchè i Committee richiedono _moltissimi_ templates cadauno (e forse pure le DAO), tant'è che un dict, una
        lista o una singola stringa viene restituita dal "get_template_filename_by_key" e ciò deve essere gestito ..
        ... producendo delle tuple come nell'esempio qui sopra

         *[ \
                *[ \
                    model_to_template_mapper_jinja.get_template_filename_by_key( \
                        translated_diagram.daos_by_id[dao_id] \
                    ),
                    *[ \
                        
                        model_to_template_mapper_jinja.get_template_filename_by_key( \
                            translated_diagram.daos_by_id[dao_id] \
                        ),
                        for committee_id in translated_diagram.daos_by_id[dao_id].committees_by_id.keys()
                    ]
                ]\
                if model_to_template_mapper_jinja.has_template_filename_for_key(translated_diagram.daos_by_id[dao_id]) \
                else None
                
                for dao_id in translated_diagram.daos_by_id.keys()
            ]
        """
        for output_and_filepath in content_and_filepath_to_output:
            output_to_print = output_and_filepath[0]
            filepath = output_and_filepath[1]
            try:
                ok &= super().to_output(output_to_print, filepath, additional_data)
            except Exception as e:
                print(f"ERROR while outputting some Jinja compiled thing into: {filepath}")
                print(e)

        return ok