import src.cli.cli_executor as cli_module
import src.pipeline.pipeline_item as pi
import src.utilities.constants as consts

import src.files.file_utils as file_utils

class AntlrInvoker(cli_module.CLIExecutor):
    def __init__(self, pipeline_item_data: pi.PIData, input_key_grammar_filepath:str, antlr_version="4.13.1"):
        super().__init__(pipeline_item_data, inputs_as_separated_commands=False)
        if input_key_grammar_filepath is None or input_key_grammar_filepath == "":
            raise Exception("AntlrInvoker needs a non-None, non-empty 'input_key_grammar_filepath' construct parameter")
        self.input_key_grammar_filepath = input_key_grammar_filepath
        self.antlr_version = antlr_version


    def commands_froms_inputs(self, inputs):
        antlr_path = file_utils.concat_folder_filename(consts.EXTERNAL_LIBS_FOLDER, f"antlr-{self.antlr_version}.jar")
        grammar_filepath = inputs[self.input_key_grammar_filepath]
        inputs[self.input_key_grammar_filepath] = ""
        other_commands = super().commands_froms_inputs(inputs)
        inputs[self.input_key_grammar_filepath] = grammar_filepath
        final_command = f"java -jar {antlr_path}  -Dlanguage=Python3 {grammar_filepath}.g4 {other_commands}"
        print(f"final_command: {final_command}")
        return final_command
