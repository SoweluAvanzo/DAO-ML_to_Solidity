import os
import src.cli.cli_executor as cli_module
import src.pipeline.pipeline_item as pi
import src.utilities.constants as consts

import src.files.file_utils as file_utils

PARSER = "Parser"
LEXER = "Lexer"
EXTENSION_DEFAULT = "g4"

class AntlrConfig:
    def __init__(self, folder_path:str, grammar_name: str):
        self.folder_path = folder_path
        self.grammar_name = grammar_name

    def get_grammar_filepath(self, extension=EXTENSION_DEFAULT):
        return file_utils.concat_folder_filename(self.folder_path, f"{self.grammar_name}{PARSER}.{extension}")
    def get_lexer_filepath(self, extension=EXTENSION_DEFAULT):
        return file_utils.concat_folder_filename(self.folder_path, f"{self.grammar_name}{LEXER}.{extension}")
    def __repr__(self):
        return """
        {{
            folder_path: {0},
            grammar_name: {1},
        }}
        """.format(self.folder_path, self.grammar_name)
    def to_json(self):
        return self.__repr__()


class AntlrInvoker(cli_module.CLIExecutor):
    def __init__(self, pipeline_item_data: pi.PIData, input_key_grammar_config:str, antlr_version="4.13.1", file_extension=EXTENSION_DEFAULT):
        super().__init__(pipeline_item_data, inputs_as_separated_commands=False)
        if input_key_grammar_config is None:
            raise Exception("AntlrInvoker needs a non-None, non-empty 'input_key_grammar_config' construct parameter")
        self.input_key_grammar_config = input_key_grammar_config
        self.antlr_version = antlr_version
        self.file_extension = file_extension

    def get_file_extensions_to_remove(self):
        return [\
            "py", "interp", "tokens"    
        ]

    def get_grammar_configurations_from_inputs(self, inputs:dict):
        grammar_config:AntlrConfig = inputs[self.input_key_grammar_config] if self.input_key_grammar_config in inputs else None
        if grammar_config is None or not isinstance(grammar_config, AntlrConfig):
            raise Exception(f"ERROR: can't run {type(self)} with a grammar_config (from input) of the wrong type: expected AntlrConfig, got: {type(grammar_config)}")
        return grammar_config

    def commands_froms_inputs(self, inputs):
        try:
            antlr_path = file_utils.concat_folder_filename(consts.EXTERNAL_LIBS_FOLDER, f"antlr-{self.antlr_version}.jar")
            grammar_config:AntlrConfig = self.get_grammar_configurations_from_inputs(inputs)
            folder_path = grammar_config.folder_path
            grammar_filepath = grammar_config.get_grammar_filepath(self.file_extension)
            inputs[self.input_key_grammar_config] = ""
            other_commands = super().commands_froms_inputs(inputs)
            inputs[self.input_key_grammar_config] = grammar_config
            lexer_filepath = grammar_config.get_lexer_filepath(self.file_extension)# grammar_filepath
            to_compile_data = [
                {'filepath': lexer_filepath, 'visitor': False, 'listener': False},
                {'filepath': grammar_filepath, 'visitor': True, 'listener': False}
            ]
            to_compile_commands = [
                f"java -jar {antlr_path} -Dlanguage=Python3 {tcd['filepath']} {'-visitor' if tcd['visitor'] else ''} {'-listener' if tcd['listener'] else ''}"
                for tcd in to_compile_data
            ]
            # the list of files to compile
            final_commands_list = [ \
                    f"{to_compile_command} {other_commands}" \
                    for to_compile_command in to_compile_commands
            ]
            # make the destination folder a potential Python module -> create an __init__.py file
            path_init_file:str = file_utils.concat_folder_filename(folder_path, "__init__.py") 
            if not file_utils.file_exists(path_init_file):
                final_commands_list.append(f"echo # > {path_init_file}")
            final_command = ' & '.join(final_commands_list)
            return final_command
        except Exception as e:
            print("ERROR:")
            print(e)
            return ""
    
    def remove_previous_compilation_outputs(self, inputs:dict):
        extensions_to_remove_pre_compile = self.get_file_extensions_to_remove()
        set_extensions = set(extensions_to_remove_pre_compile)
        grammar_config:AntlrConfig = self.get_grammar_configurations_from_inputs(inputs)
        folder_path = grammar_config.folder_path
        files_in_compilation_folder =  file_utils.list_files_in(folder_path)
        for f in files_in_compilation_folder:
                #f"rm {file_utils.concat_folder_filename(folder_path, f"*.{ext}") }"
            extension_index = f.rfind('.')
            if extension_index >= 0:
                extension = f[extension_index+1 : ]
                if extension in set_extensions \
                    and "__init__" not in f:
                    file_path_to_remove = file_utils.concat_folder_filename(folder_path, f)
                    file_utils.delete_file(file_path_to_remove)
    
    def execute_command(self, command:str, inputs:dict, index:int=None):
        try:
            self.remove_previous_compilation_outputs(inputs)
        except Exception as e:
            print("ERROR while remove_previous_compilation_outputs during execute_command:")
            print(e)
        return super().execute_command(command, index)
        
    def repr_inner(self):
        return \
            """
                {0}
                "input_key_grammar_config": {1},
                "antlr_version": {2},
                "file_extension": {3}
            """.format( \
                super().repr_inner(),
                self.input_key_grammar_config,
                self.antlr_version,
                self.file_extension
            )
