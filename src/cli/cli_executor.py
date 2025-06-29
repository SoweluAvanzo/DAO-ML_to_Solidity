import os
import src.pipeline.pipeline_item as pi

class CLIExecutor(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, inputs_as_separated_commands=False):
        super().__init__(pipeline_item_data)
        self.inputs_as_separated_commands = inputs_as_separated_commands


    def execute_command(self, command:str, inputs:dict, index:int=None):
        o = None
        done = False
        try:
            o = os.system(command)
            done = True
        except Exception as e:
            print(f"Exception at executing command {'' if index is None else '# ' + index} : {command}")
            print(e)
        return done, o

    def commands_froms_inputs(self, inputs):
        deps = self.get_dependencies()
        command = " ".join(inputs[d] for d in deps)
        return command

    def run(self, inputs):
        if self.inputs_as_separated_commands:
            deps = self.get_dependencies()
            outputs = [None] * len(deps)
            i = 0
            for d in deps:
                command = inputs[d]
                # print(f"running command #{i}: {command}")
                done, o = self.execute_command(command, i)
                if done:
                    outputs[i] = o
                i += 1
            return outputs
        command = self.commands_froms_inputs(inputs)
        done, o = self.execute_command(command, inputs, None)
        return o if done else None
        
    def repr_inner(self):
        return \
            """
                "inputs_as_separated_commands": {0}
            """.format( \
                'true' if self.inputs_as_separated_commands else 'false'
            )
