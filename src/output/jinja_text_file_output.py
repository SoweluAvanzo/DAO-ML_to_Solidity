
import src.output.text_file_output as tfo
import src.files.file_utils as fu
import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.model_converter_base as mcb
#import src.postprocessing.output_preparation.templates.jinja.model_to_template_mapper_jinja as mtt_mapper_j
import src.postprocessing.model_conversion.solidity.solidity_converter_general as stg
import src.postprocessing.output_preparation.templates.jinja.compiled_solidity as compiled_sol

# TODO (2025-08-10) DA SISTEMARE

class JinjaTextFileOutput(tfo.TextFileOutput):
    def __init__(self, pipeline_item_data: pi.PIData, \
                key_translated_diagram:str, \
                #key_model_to_template_mapper_jinja:str, \
                base_destination=None \
                ):
        super().__init__(pipeline_item_data, base_destination)
        self.key_translated_diagram = key_translated_diagram
        #self.key_model_to_template_mapper_jinja = key_model_to_template_mapper_jinja
        self.current_inputs = None

    def run(self, inputs:dict):
        self.current_inputs = inputs
        r = super().run(inputs)
        self.current_inputs = None
        return r
        

    def to_output(self, what, destination:str=None, additional_data=None) -> bool:
        ok = True
        translated_diagram = what
        # set the "output mode" if absent
        if additional_data is None:
            additional_data = { "mode": "w" }
        elif "mode" not in additional_data:
            additional_data["mode"] = "w"
        # now, sanity checks
        print(f"outputting a {type(what)} in jinja :D")
        if not isinstance(translated_diagram, compiled_sol.CompiledSolidityDiagram):
            if self.key_translated_diagram is None :
                print(f"WARNING: is missing key_translated_diagram : {self.key_translated_diagram }")
                translated_diagram = self.get_ith_input(0, additional_data)
            else:
                if self.key_translated_diagram in additional_data:
                    translated_diagram = self.current_inputs[self.key_translated_diagram]
                else:
                    print(f"ERROR: translated_diagram is not a compiled_sol.CompiledSolidityDiagram and is missing key_translated_diagram : {self.key_translated_diagram }")
                    translated_diagram = None

        if not isinstance(translated_diagram, compiled_sol.CompiledSolidityDiagram):
            raise Exception(f"The provided translated diagram should be an instance of TranslatedDiagram, but it's a: {type(translated_diagram)}")
        
        #def append_template_filename_output(array:list, translated_data:mcb.ModelConversionResultBase, template_filename ):
        def append_template_filename_output(array:list, compiled_thing:str, template_filename ):
            if isinstance(template_filename, str):
                array.append((compiled_thing, template_filename))
            elif isinstance(template_filename, list):
                array.extend([ (compiled_thing, tf) for tf in template_filename])
            elif isinstance(template_filename, dict) or isinstance(template_filename, map):
                array.extend([ (compiled_thing, template_filename[ktf]) for ktf in template_filename.keys()])
            return array

        # start with diagram ....
        # TODO (225-08-13) AGGIUSTAREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        content_and_filepath_to_output = append_template_filename_output( \
            [], \
            translated_diagram.get_compiled(), \
            translated_diagram.get_template_name() \
            )
        # ... then DAOs ...
        for dao_id, dao_compiled_struct in translated_diagram.get_daos_compiled_by_id().items():
            dao = dao_compiled_struct
            append_template_filename_output( \
                content_and_filepath_to_output, \
                dao.get_compiled(), \
                dao.get_template_name() \
            )
            # ... then committees ...
            for committee_id, committee_compiled_struct in dao.committees.items():
                    committee = committee_compiled_struct
                    append_template_filename_output( \
                        content_and_filepath_to_output, \
                        committee.get_compiled(), \
                        committee.get_template_name() \
                    )
                # ... then ... what? is there something specific to each committee?
                # TODO: (202-08-13) STILL MISSING, WAITING FOR "TemplateJinjaSolidity_1_0_0" TO FINISH IMPLEMENTATION
        # then, produce the output  
        for output_and_filepath in content_and_filepath_to_output:
            output_to_print = output_and_filepath[0]
            filepath = output_and_filepath[1]
            try:
                full_path = fu.concat_folder_filename(self.base_destination, filepath)
                folder = fu.extract_folder_from_full_path(full_path)
                fu.check_and_make_folder(folder)
                ok &= super().to_output(output_to_print, full_path, additional_data)
            except Exception as e:
                print(f"ERROR while outputting some Jinja compiled thing into: {filepath}")
                print(e)

        return ok