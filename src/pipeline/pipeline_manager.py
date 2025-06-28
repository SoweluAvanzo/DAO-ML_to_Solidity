from enum import Enum
from collections import deque

import src.pipeline.pipeline_item as pi

class NodeRunStatus(Enum):
    CRASHED = -1
    NEVER_RUN = 0
    QUEUED = 1
    RUNNING = 2
    DONE = 3

def newEmptyDependencyOutputData(done=False, data=None): # -> list[bool, any]:
    return [done, data]
class PipelineNode(pi.PipelineItem):
    def __init__(self, pipelineManager, item: pi.PipelineItem):
        super().__init__(pi.PIData(item.get_key(), None))
        self.pipelineManager=pipelineManager
        self.item = item
        self.status_run = NodeRunStatus.NEVER_RUN
        self.dependants:dict[str, PipelineNode] = {}
        self.dependency_inputs:dict[str, list[bool, any]] = {}

    def getItem(self):
        return self.item

    def getDependencies(self):
        return self.item.get_dependencies()

    def getDependants(self):
        return self.dependants
    
    def addDependant(self, newDependant:any):
        if not isinstance(newDependant, PipelineNode):
            raise TypeError(f"Provided dependant is not a PipelineNode, but a {type(newDependant)}")
        item_dependant:pi.PipelineItem = newDependant.getItem()
        key = item_dependant.get_key()
        self.dependants[key] = newDependant
        # self.dependency_outputs[key] = newEmptyDependencyOutputData()
        newDependant.dependency_inputs[self.item.get_key()] = newEmptyDependencyOutputData()
    
    def getInputForRun(self): # ->dict[str,any]:
        return { ite[0]: ite[1][1] for ite in self.dependency_inputs.items()}
    
    def canRun(self):
        """
        A Node can run if and only if all of its inputs are satisfied (i.e., the first item in that array, which is a boolean)
        """
        if self.status_run != NodeRunStatus.NEVER_RUN:
            return False
        for dep in self.item.get_dependencies():
            if (dep not in self.dependency_inputs) or (not self.dependency_inputs[dep][0]): # are all dependencies satisfied? if not -> can't run
                return False
        return True
    
    def addInput(self, input_value: any, dependency_job: pi.PipelineItem):
        key = dependency_job.get_key()
        output_data = None
        if key in self.dependency_inputs:# if the data is already present, then update the "completed" value (the boolean value, first item of the array)
            output_data = self.dependency_inputs[key]
            if output_data[0]:
                return
            output_data[0] = True
            output_data[1] = input_value
        else:
            output_data = newEmptyDependencyOutputData(True, input_value)
            self.dependency_inputs[key] = output_data
    def repr_inner(self):
        return """
            "item": {{
                    {0}
            }},
            "status": "{1}",
            "dependants": {2},
            "dependency_inputs": {3}    
        """.format(repr(self.item), \
                    self.status_run, \
                    str(list(self.dependants.keys())), \
                    repr(self.dependency_inputs))

class PipelineManager:
    def __init__(self):
        self.items:dict[str, pi.PipelineItem] = {}
    
    def addItem(self, item: pi.PipelineItem):
        self.items[item.get_key()] = item

    def removeItem(self, key: str):
        if key not in self.items:
            return
        del self.items[key]
    
    def getItem(self, key:str)-> pi.PipelineItem:
        return self.items[key]

    def runPipeline(self) -> any:
        #setup the data structures
        items_as_list = list(self.items.values())
        nodes = { item.get_key(): PipelineNode(self, item) for item in items_as_list }
        roots = []
        # setup dependendants
        for item in items_as_list:
            key = item.get_key()
            current_node = nodes[key]
            if item.get_dependencies() != None and (len(item.get_dependencies()) > 0):
                for d in item.get_dependencies():
                    if d not in nodes:
                        print(f"ERROR: dependency {d} does not exist")
                    else:
                        n = nodes[d]
                        n.addDependant(current_node)
            else:
                n = nodes[item.get_key()]
                roots.append(n)
                n.status_run = NodeRunStatus.QUEUED
        job_queues = deque(roots) # a.k.a. "frontier" ; single thread -> only one item at a time can run
        del roots
        #RUN
        while len(job_queues) > 0:
            job:PipelineNode = job_queues.popleft()
            job.status_run = NodeRunStatus.RUNNING
            input = job.getInputForRun()
            try:
                output = job.item.run(input)
                job.status_run = NodeRunStatus.DONE
                #update dependants
                if len(job.getDependants()) > 0:
                    for dependant_node in job.getDependants().values():
                        item_dependant = dependant_node.item
                        dep_key = item_dependant.get_key()
                        dependant_node.addInput(output, job.item)
                        if dependant_node.status_run == NodeRunStatus.NEVER_RUN and dependant_node.canRun():
                            # add to queue
                            dependant_node.status_run = NodeRunStatus.QUEUED
                            job_queues.append(dependant_node)
            except Exception as e:
                job.status_run = NodeRunStatus.CRASHED
                print(f"ERROR while running job: {job.item.get_key()}")
                print(e)
                import traceback
                traceback.print_exception(e)
        
