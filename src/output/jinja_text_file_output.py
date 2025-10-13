
import src.output.text_file_output as tfo
import src.files.file_utils as fu
import src.pipeline.pipeline_item as pi
import src.postprocessing.model_translation.solidity.solidity_translator_general as stg
import src.postprocessing.output_preparation.compilers.solidity.compiled_solidity_data as compiled_sol
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd
import src.model.enums.extended_enum as extended_enum

# TODO (2025-08-10) DA SISTEMARE


class AcceptedClasses_Jinja_TFO(extended_enum.ExtendedEnum):
    LIST = list
    CompiledSolidityDiagram = compiled_sol.CompiledSolidityDiagram


class JinjaTextFileOutput(tfo.TextFileOutput):
    def __init__(self, pipeline_item_data: pi.PIData,
                 key_translated_diagram: str, \
                 # key_model_to_template_mapper_jinja:str,
                 base_destination=None
                 ):
        super().__init__(pipeline_item_data, base_destination)
        self.key_translated_diagram = key_translated_diagram
        # self.key_model_to_template_mapper_jinja = key_model_to_template_mapper_jinja
        self.current_inputs = None

    def run(self, inputs: dict):
        self.current_inputs = inputs
        r = super().run(inputs)
        self.current_inputs = None
        return r

    #

    def append_template_filename_output(self, array: list, compiled_thing: str, template_filename: str):
        if isinstance(template_filename, str):
            array.append((compiled_thing, template_filename))
        elif isinstance(template_filename, list):
            array.extend([(compiled_thing, tf) for tf in template_filename])
        elif isinstance(template_filename, dict) or isinstance(template_filename, map):
            array.extend([(compiled_thing, template_filename[ktf])
                         for ktf in template_filename.keys()])
        return array

    def __td_t_list_o_solidity(self, translated_diagram: compiled_sol.CompiledSolidityDiagram):
        content_and_filepath_to_output = self.append_template_filename_output(
            [],
            translated_diagram.get_compiled(),
            translated_diagram.get_template_name()
        )
        # ... then DAOs ...
        for dao_id, dao_compiled_struct in translated_diagram.get_daos_compiled_by_id().items():
            dao = dao_compiled_struct
            self.append_template_filename_output(
                content_and_filepath_to_output,
                dao.get_compiled(),
                dao.get_template_name()
            )
            for filename, thing_compiled_struct in dao_compiled_struct.interfaces_and_dao_related_compiled_contracts.items():
                self.append_template_filename_output(
                    content_and_filepath_to_output,
                    thing_compiled_struct.get_compiled(),
                    thing_compiled_struct.get_template_name()
                )
            # ... then committees ...
            for committee_id, committee_compiled_struct in dao.committees.items():
                committee = committee_compiled_struct
                self.append_template_filename_output(
                    content_and_filepath_to_output,
                    committee.get_compiled(),
                    committee.get_template_name()
                )
                for filename, compiled_conditions in committee.compiled_conditions_by_name.items():
                    self.append_template_filename_output(
                        content_and_filepath_to_output,
                        compiled_conditions.get_compiled(),
                        compiled_conditions.get_template_name()
                    )
        return content_and_filepath_to_output

    def translated_diagram_to_list_output_converters(self, additional_data=None):
        """
        Override-designed
        @return a dict whose keys are "type" (got from the classes itselves; check out
        "AcceptedClasses_Jinja_TFO" for more info)
        """
        def from_list(td):
            content_and_filepath_to_output = []
            for t in td:
                if isinstance(t, cgd.CompiledUnitWithID):
                    content_and_filepath_to_output = self.append_template_filename_output(
                        content_and_filepath_to_output,
                        t.get_compiled(),
                        t.get_template_name()
                    )
            return content_and_filepath_to_output
        return {
            AcceptedClasses_Jinja_TFO.LIST.value: from_list,
            AcceptedClasses_Jinja_TFO.CompiledSolidityDiagram.value: lambda td: self.__td_t_list_o_solidity(
                td)
        }

    def to_output(self, what, destination: str = None, additional_data=None) -> bool:
        ok = True
        translated_diagram = what
        # set the "output mode" if absent
        if additional_data is None:
            additional_data = {"mode": "w"}
        elif "mode" not in additional_data:
            additional_data["mode"] = "w"
        # now, sanity checks
        print(f"outputting a {type(translated_diagram)} in jinja :D")

        # get the list of things to output, based on its class
        # this way, it's possible to modularize and extend the
        # ways to get "things to output"
        class_translated_diagram = type(translated_diagram)
        class_based_TD_converter = self.translated_diagram_to_list_output_converters(
            additional_data=additional_data)
        if class_translated_diagram not in class_based_TD_converter:
            if self.key_translated_diagram is None:
                print(
                    f"WARNING: is missing key_translated_diagram : {self.key_translated_diagram}")
                translated_diagram = self.get_ith_input(0, additional_data)
                class_translated_diagram = type(translated_diagram)
            else:
                if self.key_translated_diagram in additional_data:
                    translated_diagram = self.current_inputs[self.key_translated_diagram]
                    class_translated_diagram = type(translated_diagram)
                else:
                    print(
                        f"ERROR: translated_diagram is not a compiled_sol.CompiledSolidityDiagram and is missing key_translated_diagram : {self.key_translated_diagram}")
                    import json
                    print(f"additional_data: {json.dumps(additional_data)}")
                    translated_diagram = None
        else:
            print(
                f"class_translated_diagram not recognized: {class_translated_diagram}")
        if translated_diagram is None:
            raise Exception(
                f"The provided translated diagram should be an instance of one of [{",".join(c.__name__ for c in class_based_TD_converter.keys())}], but it's a: {class_translated_diagram}")

        content_and_filepath_to_output = class_based_TD_converter[class_translated_diagram](
            translated_diagram)
        # produce the output
        print(
            f"\n\n\n PRODUCING {len(content_and_filepath_to_output)} outputs in total")
        for output_and_filepath in content_and_filepath_to_output:
            output_to_print = output_and_filepath[0]
            filepath = output_and_filepath[1]
            try:
                full_path = fu.concat_folder_filename(
                    self.base_destination, filepath)
                folder = fu.extract_folder_from_full_path(full_path)
                fu.check_and_make_folder(folder)
                ok &= super().to_output(output_to_print, full_path, additional_data)
            except Exception as e:
                print(
                    f"ERROR while outputting some Jinja compiled thing into: {filepath}")
                print(e)
        return ok
