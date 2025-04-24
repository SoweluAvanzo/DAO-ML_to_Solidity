
class PipelineItem:
    def __init__(self, key:str, dependencies=None):
        self.key = key
        self.dependencies = dependencies
    
    def run(self, input:dict[str, any]) -> any:
        print(f"ERROR: PipelineItem has not implemented the run method. Key:")
        print(self.key)
        pass
