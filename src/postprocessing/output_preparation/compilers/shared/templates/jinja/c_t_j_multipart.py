from typing import Generator

import src.pipeline.pipeline_item as pi

import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_base as ctjb
import src.postprocessing.output_preparation.compilers.shared.templates.compiler_template_base_multipart as tb_m
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd

import src.postprocessing.model_translation.shared.translation_result_model as trm

import src.utilities.errors as e_c

"""
No differences at the moment from the super (Jinja Base) class.
"""


class CompilerTemplateJinjaMultipart(ctjb.CompilerTemplateJinjaBase, tb_m.CompilerTemplateBaseMultipart):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_diagram_instance_data: str = None,
                 key_diagram_model: str = None,
                 key_template_skeleton_provider_by_name: str = None,
                 key_is_result_as_list: str = None
                 ):
        super().__init__(pipeline_item_data,
                         optional_external_data=optional_external_data,
                         key_template_instance_data=key_diagram_instance_data,
                         key_template_skeleton=None
                         )
        tb_m.CompilerTemplateBaseMultipart.__init__(
            self, pipeline_item_data, optional_external_data=optional_external_data)
        self.key_diagram_model = key_diagram_model
        self.key_template_skeleton_provider_by_name = key_template_skeleton_provider_by_name
        self.key_is_result_as_list = key_is_result_as_list
        self.is_compilation_result_a_list = True

    # checks

    def is_root_of_compilation(self, compiled_part: cgd.CompiledUnitWithID):
        return False

    def is_template_skeleton_provider(self, obj):
        return isinstance(obj, template_provider.TemplateProviderByName)

    def check_instance_data(self, instance_data: dict, additional_data=None):
        raise Exception(
            f"check_instance_data on ({self.__class__.__name__}) {e_c.ERROR_TEXT__NOT_IMPLEMENTED}")

    #

    def get_template_skeleton_provider_by_name(self, additional_data: dict):
        tpbn = self.get_ith_input(
            additional_data, 2) if self.key_template_skeleton_provider_by_name is None else additional_data[self.key_template_skeleton_provider_by_name]
        if not self.is_template_skeleton_provider(tpbn):
            raise Exception(
                f"template provider by name needed, but we got: {type(tpbn)}")
        return tpbn

    def compile_all_parts_as_generator(self, instance_data: dict, tpbn: template_provider.TemplateProviderByName, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    #

    def get_all_parts_to_compile_as_generator(self, instance_data: dict, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        if additional_data is None:
            raise Exception(
                f"Compile template ({self.__class__.__name__}) needs non-None additional_data (from inputs) to get stuff")
        # might throw an Exception
        self.check_instance_data(
            instance_data, additional_data=additional_data)

        tpbn = self.get_template_skeleton_provider_by_name(additional_data)
        for part in self.compile_all_parts_as_generator(instance_data, tpbn, additional_data):
            yield part

    def compile_template(self,
                         diagram_instance_data: trm.TranslatedDiagram,
                         additional_data=None
                         ):
        """
        Depending on the constructor's parameter "key_is_result_as_list", returns either an array of compiledthings or the "root of compilation" (see #is_root_of_compilation(...))
        """
        if (self.key_is_result_as_list is None) or (additional_data is None) or (
                self.key_is_result_as_list in additional_data and additional_data[self.key_is_result_as_list]):
            # return super(tb_m.CompilerTemplateBaseMultipart, self)
            return tb_m.CompilerTemplateBaseMultipart.compile_template(self, instance_data=diagram_instance_data, additional_data=additional_data)
        compiled: cgd.CompiledUnitWithID = None
        for cp in self.get_all_parts_to_compile_as_generator(instance_data=diagram_instance_data, additional_data=additional_data):
            if self.is_root_of_compilation(cp):
                compiled = cp  # assumption: this check is True only ONE time
        if compiled is None:
            print(f"{type(self)} returns NOTHING on compile_template")
        return compiled
