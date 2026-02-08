from typing import List, Dict

import src.utilities.utils as u


class PIData:
    """
        Data used to configure PipelineItems.
    """

    def __init__(self, key: str, dependencies: List[str] = None):
        """
        Args:
            key (str): The key of the PipelineItem, it should be unique across the pipeline and it's used to identify the PipelineItem and to refer to it in the dependencies of other PipelineItems.
            dependencies (List[str], optional): list of keys that the PipelineItem it's related to depends on. The order is fundamental and all keys must exist. Defaults to None meaning that the related PipelineItem is one of the root(s) of the computation.
        """
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

    def get_dependencies(self) -> list[str]:
        return self.pipeline_item_data.dependencies

    def set_dependencies(self, dependencies: list[str]):
        """
        WARRING: this will override the dependencies of the PipelineItem, use with caution. Beware of NPE (Null Pointer Exception) if you set dependencies to None.
        Args:
            dependencies (list[str]): see PIData.dependencies
        """
        if (not isinstance(dependencies, list)) and (not isinstance(dependencies, dict)):
            raise Exception(
                f"wrong type for dependencies: {type(dependencies)}. Only integer-indexable types are allowed (list, dict).")
        self.pipeline_item_data.dependencies = dependencies

    def set_dependency(self, index: int, dependency: str):
        """
        WARRING: this will override the dependencies of the PipelineItem, use with caution. Beware of NPE (Null Pointer Exception) if you set dependencies to None.
        Args:
            index (int): the index of the dependency to set, it must be less than the length of the dependencies list.
            dependency (str): the new dependency to set at the specified index. It must be a valid key of another PipelineItem in the pipeline.
        """
        self.pipeline_item_data.dependencies[index] = dependency

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
