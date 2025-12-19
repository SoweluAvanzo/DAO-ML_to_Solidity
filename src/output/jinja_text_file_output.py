import src.pipeline.pipeline_item as pi

import src.output.text_file_output as tfo

import src.postprocessing.output_preparation.compilers.solidity.compiled_solidity_data as compiled_sol
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd

import src.files.file_utils as fu
import src.utilities.extended_enum as extended_enum
import src.utilities.utils as u


class AcceptedClasses_Jinja_TFO(extended_enum.ExtendedEnum):
    LIST = type([])
    CompiledSolidityDiagram = compiled_sol.CompiledSolidityDiagram


class JinjaTextFileOutput(tfo.TextFileOutput):
    def __init__(self, pipeline_item_data: pi.PIData,
                 key_compiled_diagram: str,
                 printer_debug: u.PrinterDebug = None,
                 # key_model_to_template_mapper_jinja:str,
                 key_base_destination: str = None
                 ):
        super().__init__(
            pipeline_item_data,
            printer_debug=printer_debug,
            key_base_destination=key_base_destination,
            key_filename_extension=None  # here, the strategy is different
        )
        self.key_compiled_diagram = key_compiled_diagram
        # self.key_model_to_template_mapper_jinja = key_model_to_template_mapper_jinja
        self.current_inputs = None

    def run(self, inputs: dict):
        self.current_inputs = inputs
        r = super().run(inputs)
        self.current_inputs = None
        return r

    #

    def append_translated_name_output(self, array: list, compiled_thing: str, template_filename: str):
        if isinstance(template_filename, str):
            array.append((compiled_thing, template_filename))
        elif isinstance(template_filename, list):
            array.extend([(compiled_thing, tf) for tf in template_filename])
        elif isinstance(template_filename, dict) or isinstance(template_filename, map):
            array.extend([
                (compiled_thing, template_filename[ktf]) for ktf in template_filename.keys()
            ])
        return array

    def __td_t_list_o_solidity(self, translated_diagram: compiled_sol.CompiledSolidityDiagram):
        content_and_filepath_to_output = self.append_translated_name_output(
            [],
            translated_diagram.get_compiled(),
            translated_diagram.get_output_full_path()
        ) if translated_diagram.can_diagram_be_compiled else []
        # ... then DAOs ...
        for dao_id, dao_compiled_struct in translated_diagram.get_daos_compiled_by_id().items():
            dao: compiled_sol.CompiledSolidityDAO = dao_compiled_struct
            self.append_translated_name_output(
                content_and_filepath_to_output,
                dao.get_compiled(),
                dao.get_output_full_path()
            )
            for filename, thing_compiled_struct in dao.interfaces_and_dao_related_compiled_contracts.items():
                self.append_translated_name_output(
                    content_and_filepath_to_output,
                    thing_compiled_struct.get_compiled(),
                    thing_compiled_struct.get_output_full_path()
                )
            # ... then committees ...
            for committee_id, committee_compiled_struct in dao.committees_by_id.items():
                committee: compiled_sol.CompiledSolidityCommittee = committee_compiled_struct
                self.append_translated_name_output(
                    content_and_filepath_to_output,
                    committee.get_compiled(),
                    committee.get_output_full_path()
                )
                for filename, compiled_conditions in committee.compiled_conditions_by_name.items():
                    self.append_translated_name_output(
                        content_and_filepath_to_output,
                        compiled_conditions.get_compiled(),
                        compiled_conditions.get_output_full_path()
                    )
        return content_and_filepath_to_output

    def translated_diagram_to_list_output_translators(self, additional_data=None):
        """
        Override-designed
        @return a dict whose keys are "type" (got from the classes itselves; check out
        "AcceptedClasses_Jinja_TFO" for more info)
        """
        def from_list(td):
            content_and_filepath_to_output = []
            for t in td:
                if isinstance(t, cgd.CompiledUnitWithID):
                    content_and_filepath_to_output = self.append_translated_name_output(
                        content_and_filepath_to_output,
                        t.get_compiled(),
                        t.get_output_full_path()
                    )
            return content_and_filepath_to_output
        return {
            AcceptedClasses_Jinja_TFO.LIST.value: from_list,
            AcceptedClasses_Jinja_TFO.CompiledSolidityDiagram.value: lambda td: self.__td_t_list_o_solidity(
                td)
        }

    def to_output(self, what, additional_data=None) -> bool:
        ok = True
        compiled_diagram = what
        # set the "output mode" if absent
        if additional_data is None:
            additional_data = {
                tfo.KEY_OPEN_FILE_MODE: tfo.MODE_VALUES_WRITE_array[0]
            }
        elif tfo.KEY_OPEN_FILE_MODE not in additional_data:
            additional_data[tfo.KEY_OPEN_FILE_MODE] = tfo.MODE_VALUES_WRITE_array[0]
        # now, sanity checks

        # get the list of things to output, based on its class
        # this way, it's possible to modularize and extend the
        # ways to get "things to output"
        class_compiled_diagram = type(compiled_diagram)
        class_based_TD_translator = self.translated_diagram_to_list_output_translators(
            additional_data=additional_data)
        if class_compiled_diagram not in class_based_TD_translator:
            # try to recover the compiled diagram class
            print(
                f"\nERROR: unrecognized class_compiled_diagram: {class_compiled_diagram} - {type(compiled_diagram)}")
            if self.key_compiled_diagram is None:
                compiled_diagram = self.get_ith_input(0, additional_data)
                class_compiled_diagram = type(compiled_diagram)
            else:
                if self.key_compiled_diagram in additional_data:
                    compiled_diagram = self.current_inputs[self.key_compiled_diagram]
                    class_compiled_diagram = type(compiled_diagram)
                else:
                    print(
                        f"ERROR: compiled_diagram is not a compiled_sol.CompiledSolidityDiagram and is missing key_compiled_diagram : {self.key_compiled_diagram}")
                    print(additional_data)
                    compiled_diagram = None
        else:
            print(
                f"class_compiled_diagram not recognized: {class_compiled_diagram}")
        if compiled_diagram is None:
            classes_list = ', '.join(
                c.__name__ for c in class_based_TD_translator.keys())
            raise Exception(
                f"In {type(self)} with key ''{self.get_key()}'', The provided translated diagram should be an instance of one of [{classes_list}], but it's a: {class_compiled_diagram}")

        content_and_filepath_to_output = class_based_TD_translator[class_compiled_diagram](
            compiled_diagram)
        # produce the output
        print(
            f"\n\n\n PRODUCING {len(content_and_filepath_to_output)} outputs in total")
        k_fn_e: str = self.key_filename_extension  # keep the previous value
        is_k_fn_unset = k_fn_e is None
        # add a dummy key _that just need to work_
        if is_k_fn_unset:
            # that's intentionally a string, not its value
            self.key_filename_extension = "key_filename_extension"

        for output_and_filepath in content_and_filepath_to_output:
            output_to_print = output_and_filepath[0]
            filepath = output_and_filepath[1]
            try:
                provided_base_destination: str = additional_data[self.key_base_destination]
                full_path = fu.concat_folder_filename(provided_base_destination, filepath) \
                    if (self.key_base_destination is not None) and (self.key_base_destination in additional_data) \
                    else filepath
                folder = fu.extract_folder_from_full_path(full_path)
                self.print_msg(
                    f"creating folder ({folder}), extracted from full_path: {full_path}")
                fu.check_and_make_folder(folder)
                # update the "key_base_destination" because the superclass needs the full path "up to the filename" ...
                additional_data[self.key_base_destination] = folder
                # ... and the filename in a separate way
                additional_data[self.key_filename_extension] = full_path[len(
                    folder) + 1:]  # "+1" because of the path separator
                ok &= super().to_output(output_to_print, additional_data)
                # revert the modification to key_base_destination
                additional_data[self.key_base_destination] = provided_base_destination
            except Exception as e:
                print(
                    f"ERROR while outputting some Jinja compiled thing into: {filepath}")
                print(e)
        return ok
