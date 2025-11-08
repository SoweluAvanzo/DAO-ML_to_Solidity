from typing import List, Dict

import src.utilities.utils as u


class PIData:
    def __init__(self, key: str, dependencies: List[str] = None):
        self.key = key
        self.dependencies: List[str] = [
        ] if dependencies is None else dependencies

    def add_dependency(self, new_dependency: str):
        self.dependencies.append(new_dependency)

    def __repr__(self):
        return \
            """
                "class": "{0}",
                "data": {{
                    "key": {1},
                    "dependencies": {2}
                }}
            """.format(self.__class__.__name__, self.key, self.dependencies)


class PipelineItem:
    def __init__(self, pipeline_item_data: PIData,
                 printer_debug: u.PrinterDebug = None
                 ):
        if not isinstance(pipeline_item_data, PIData):
            raise Exception(
                f"wrong type for pipeline_item_data: {type(pipeline_item_data)}")
        self.pipeline_item_data = pipeline_item_data
        self.printer_debug = printer_debug

    def print_error(self, msg):
        if self.printer_debug is not None:
            self.printer_debug.print_error(msg)

    def print_msg(self, msg):
        if self.printer_debug is not None:
            self.printer_debug.print_msg(msg)

    def run(self, inputs: Dict[str, any]):  # input:dict[str, any]) -> any:
        self.printer_debug.print_error(
            f"ERROR: PipelineItem has not implemented the run method. Key: {self.get_key()}")
        self.printer_debug.print_error(self.pipeline_item_data.key)
        pass

    def get_pipeline_item_data(self):
        return self.pipeline_item_data

    def get_key(self):
        return self.pipeline_item_data.key

    def add_dependency(self, new_dependency: str):
        self.pipeline_item_data.add_dependency(new_dependency)

    def get_dependencies(self):
        return self.pipeline_item_data.dependencies

    def get_ith_input(self, inputs: Dict[str, any], index: int):
        return inputs[self.get_dependencies()[index]]

    def repr_inner(self):
        return ""

    def __repr__(self):
        return \
            """
                "class": "{0}",
                "data": {{
                    "pipeline_item_data": {1},
                    {2}
                }}
            """.format(self.__class__.__name__, repr(self.pipeline_item_data), self.repr_inner())
