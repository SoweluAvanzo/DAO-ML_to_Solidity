from typing import Generator

import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.compilers.shared.templates.compiler_template_base_multipart as tb_m
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd

import src.utilities.utils as u
# import src.utilities.extended_enum as ext_enum

# class SolidityCompiledParts(ext_enum.ExtendedEnum):
#    IMPORTS = 1
#    CLASS_EXTENSION = 2
#    INSTANCE_DATA = 3
#    MODIFIERS = 4
#    FUNCTIONS = 5


class CompilerTemplateMultipartPermissionParts(tb_m.CompilerTemplateBaseMultipart):
    """
    Compiler for permissions, allowing to define specific parts that a permission adds to the overall template.

    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 optional_external_data=None,
                 # TODO: other things?
                 key_template_instance_data: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         optional_external_data=optional_external_data,
                         key_template_instance_data=key_template_instance_data,
                         printer_debug=printer_debug
                         )

    def get_all_parts_imports(self, instance_data: dict, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        pass

    def get_all_parts_class_extensions(self, instance_data: dict, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        pass

    def get_all_parts_instance_data(self, instance_data: dict, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        pass

    def get_all_parts_functions(self, instance_data: dict, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        pass

    def get_all_parts_modifiers(self, instance_data: dict, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        pass
