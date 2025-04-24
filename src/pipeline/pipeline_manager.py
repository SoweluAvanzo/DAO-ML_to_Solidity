from .pipeline_item import PipelineItem

class PipelineManager:
    def __init__(self):
        self.items:list[PipelineItem] = []
    
    def addItem(self, item: PipelineItem):
        self.items.append(item)
    
    def getItem(self, key:str)-> PipelineItem:
        for item in self.items:
            if item.key == key:
                return item
        return None

    def runPipeline(self) -> any:
        print("START RUN PIPELINE")
        previous_output = None
        for item in self.items:
            print( f"now running { item.key } ")
            previous_output = item.run( previous_output )
        print(" FINITO ")
        return previous_output
        
