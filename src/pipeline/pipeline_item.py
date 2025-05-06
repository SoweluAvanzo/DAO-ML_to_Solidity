
class PipelineItem:
    def __init__(self, key:str, dependencies=None):
        self.key = key
        self.dependencies:list[str] = dependencies
    
    def run(self, input): # input:dict[str, any]) -> any:
        print(f"ERROR: PipelineItem has not implemented the run method. Key:")
        print(self.key)
        pass

    def addDependency(self, newDependency):
        self.dependencies.append(newDependency)

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
