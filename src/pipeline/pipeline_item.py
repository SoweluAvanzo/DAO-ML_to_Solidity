from typing import List, Dict

class PipelineItem:
    def __init__(self, key: str, dependencies=None):
        self.key = key
        self.dependencies: List[str] = dependencies

    def run(self, inputs: Dict[str, any]):  # input:dict[str, any]) -> any:
        print(f"ERROR: PipelineItem has not implemented the run method. Key:")
        print(self.key)
        pass

    def add_dependency(self, new_dependency: str):
        self.dependencies.append(new_dependency)

    def repr_inner(self):
        return ""

    def __repr__(self):
        return \
            """
                "class": "{0}",
                "data": {{
                    "key": {1},
                    "dependencies": {2},
                    {3}
                }}
            """.format(self.__class__.__name__, self.key, self.dependencies, self.repr_inner())
