from enum import Enum
from collections import deque

import src.pipeline.pipeline_item as pi

class NodeRunStatus(Enum):
    CRASHED = -1
    NEVER_RUN = 0
    QUEUED = 1
    RUNNING = 2
    DONE = 3

def newEmptyDependencyOutputData(done=False, data=None) -> list[bool, any]:
    return [done, data]
class PipelineNode:
    def __init__(self, item: pi.PipelineItem):
        self.item = item
        self.status_run = NodeRunStatus.NEVER_RUN
        self.dependants:dict[str, pi.PipelineItem] = {}
        self.dependency_outputs:dict[str, list[bool, any]] = {}
    def getItem(self):
        return self.item
    def getDependencies(self):
        return self.item.dependencies
    def getDependants(self):
        return self.dependants
    def addDependant(self, newDependant: pi.PipelineItem):
        key = newDependant.key
        self.dependants[key] = newDependant
        self.dependency_outputs[key] = newEmptyDependencyOutputData()
    def getInputForRun(self)->dict[str,any]:
        return { ite[0]: ite[1][1] for ite in self.dependency_outputs.items()}
    def canRun(self):
        if self.status_run != NodeRunStatus.NEVER_RUN:
            return False
        for dep in self.dependants.keys():
            if dep not in self.dependency_outputs or not self.dependency_outputs[dep][0]: # are all dependencies satisfied? if not -> can't run
                return False
        return True
    def addInput(self, input_value: any, dependency_job: pi.PipelineItem):
        key = dependency_job.key
        output_data = None
        if key in self.dependency_outputs:
            output_data = self.dependency_outputs[key]
            if output_data[0]:
                print(f"ERROR: input from {key} already added")
                return
            output_data[0] = True
            output_data[1] = input_value
        else:
            output_data = newEmptyDependencyOutputData(True, input_value)
            self.dependency_outputs[key] = output_data

class PipelineManager:
    def __init__(self):
        self.items:dict[str, pi.PipelineItem] = {}
    
    def addItem(self, item: pi.PipelineItem):
        self.items[item.key] = item
    
    def getItem(self, key:str)-> pi.PipelineItem:
        for item in self.items:
            if item.key == key:
                return item
        return None

    def runPipeline(self) -> any:
        print("START RUN PIPELINE")
        #setup the data structures
        items_as_list = list(self.items.values())
        nodes = { item.key: PipelineNode(item) for item in items_as_list }
        roots = []
        # setup dependendants
        for item in items_as_list:
            if item.dependencies != None and (len(item.dependencies) > 0):
                for d in item.dependencies:
                    if d not in nodes:
                        print(f"ERROR: dependency {d} does not exist")
                    else:
                        n = nodes[d]
                        n.addDependant(item)
            else:
                roots.append(item)
                n = nodes[item.key]
                n.status_run = NodeRunStatus.QUEUED
        job_queues = deque(roots) # a.k.a. "frontier" ; single thread -> only one item at a time can run
        del roots
        #RUN
        print("actual start of running")
        while len(job_queues) > 0:
            job:PipelineNode = job_queues.popleft()
            job.status_run = NodeRunStatus.RUNNING
            print(f"running job {job.item.key}")
            input = job.getInputForRun()
            try:
                output = job.item.run(input)
                job.status_run = NodeRunStatus.DONE
                #update dependants
                if len(job.getDependants()) > 0:
                    for dependant in job.getDependants().values():
                        d_node = nodes[dependant.key]
                        d_node.addInput(output, job.item)
                        if d_node.status_run == NodeRunStatus.NEVER_RUN and d_node.canRun():
                            # add to queue
                            print(f"enqueuing job {dependant.key}")
                            d_node.status_run = NodeRunStatus.QUEUED
                            job_queues.append(d_node)
            except Exception as e:
                job.status_run = NodeRunStatus.CRASHED
                print(f"ERROR while running job __ {job.item.key} __")
                print(e)
        print(" FINITO ")
        
