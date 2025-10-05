import os

def concat_folder_filename(*parts) -> str:
    return os.path.join(*parts)

def file_exists(path:str):
    return os.path.isfile(path)


PARSER = "Parser"
LEXER = "Lexer"
EXTENSION_DEFAULT = "g4"

antlr_version = "4.13.1-complete"


EXTERNAL_LIBS_FOLDER = "." # concat_folder_filename(".", "external_libs")

XML_DAO_GRAMMAR_NAME = "XML"
XML_DAO_GRAMMAR_EXTENSION = "g4"
XML_DAO_GRAMMAR_FOLDER = "." # concat_folder_filename('.', 'src', 'parsers', 'xml')

class AntlrConfig:
    def __init__(self, folder_path:str, grammar_name: str):
        self.folder_path = folder_path
        self.grammar_name = grammar_name

    def get_grammar_filepath(self, extension=EXTENSION_DEFAULT):
        return concat_folder_filename(self.folder_path, f"{self.grammar_name}{PARSER}.{extension}")
    def get_lexer_filepath(self, extension=EXTENSION_DEFAULT):
        return concat_folder_filename(self.folder_path, f"{self.grammar_name}{LEXER}.{extension}")
    def __repr__(self):
        return """
        {{
            folder_path: {0},
            grammar_name: {1},
        }}
        """.format(self.folder_path, self.grammar_name)
    def to_json(self):
        return self.__repr__()



def commands_froms_inputs():
    file_extension = EXTENSION_DEFAULT

    try:
        antlr_path = concat_folder_filename(EXTERNAL_LIBS_FOLDER, f"antlr-{antlr_version}.jar")
        print(f"loading grammar at: {XML_DAO_GRAMMAR_FOLDER}")
        grammar_config = AntlrConfig(XML_DAO_GRAMMAR_FOLDER, XML_DAO_GRAMMAR_NAME)
        folder_path = grammar_config.folder_path

        grammar_filepath = grammar_config.get_grammar_filepath(file_extension)
        lexer_filepath = grammar_config.get_lexer_filepath(file_extension)# grammar_filepath


        to_compile_data = [
            {'filepath': lexer_filepath, 'visitor': False, 'listener': False},
            {'filepath': grammar_filepath, 'visitor': True, 'listener': False}
        ]
        to_compile_commands = [
            f"java -jar {antlr_path} -Dlanguage=Python3 {tcd['filepath']} {'-visitor' if tcd['visitor'] else ''} {'-listener' if tcd['listener'] else ''}"
            for tcd in to_compile_data
        ]
        # the list of files to compile
        final_commands_list = to_compile_commands #
        """[ \
                f"{to_compile_command} {other_commands}" \
                for to_compile_command in to_compile_commands
        ]
        """
        # make the destination folder a potential Python module -> create an __init__.py file
        path_init_file:str = concat_folder_filename(folder_path, "__init__.py") 
        if not file_exists(path_init_file):
            final_commands_list.append(f"echo # > {path_init_file}")
        final_command = ' & '.join(final_commands_list)
        return final_command
    except Exception as e:
        print("ERROR:")
        print(e)
        return ""
    

def exec(command):
    return os.system(command)


def main():
    print("init")
    command = commands_froms_inputs()
    print(f"commands: {command}")
    o = exec(command)
    print("results in ->")
    print(o)

if __name__ == "__main__":
    main()


# python .\compile_grammar.py

#  python translator_cli.py -fn "translate" -tt "optimized" -f ".\\data\\Travelhive_final_model.xml" -gen_test