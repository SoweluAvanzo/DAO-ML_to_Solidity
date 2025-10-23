from typing import Generator

import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.compilers.shared.templates.template_base as tb
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd


class CompilerTemplateBaseMultipart(tb.TemplateBase):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None, key_template_instance_data: str = None):
        super().__init__(pipeline_item_data,
                         optional_external_data=optional_external_data,
                         key_template_instance_data=key_template_instance_data
                         )

    def get_all_parts_to_compile_as_generator(self, instance_data: dict, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        raise Exception(
            f"ERROR: get_all_parts_to_compile_as_generator not implemented yet in {self.__class__.__name__}")

    def get_all_parts_to_compile(self, instance_data: dict, additional_data=None) -> list[cgd.CompiledUnitWithID]:
        return [p for p in self.get_all_parts_to_compile_as_generator(instance_data=instance_data, additional_data=additional_data)]

    def compile_template(self, instance_data: dict, additional_data=None) -> list[cgd.CompiledUnitWithID]:
        return self.get_all_parts_to_compile(instance_data=instance_data, additional_data=additional_data)
