import src.files.file_utils as files
import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi
import src.pipeline.utilities.pi_any_value as pi_v

import src.cli.antlr_invoker as grammar_compiler

XML_DAO_GRAMMAR_NAME = "XML"
XML_DAO_GRAMMAR_EXTENSION = "g4"
XML_DAO_GRAMMAR_FOLDER = files.concat_folder_filename('.', 'src', 'parsers', 'xml')


def main():
    print("AAAAAAAAAAAAAA")

    pm = pmp.PipelineManager()

    k_grammar_path_provider = "k_grammar_path_provider"
    print(f"loading grammar at: {XML_DAO_GRAMMAR_FOLDER}")
    antlr_config = grammar_compiler.AntlrConfig(XML_DAO_GRAMMAR_FOLDER, XML_DAO_GRAMMAR_NAME)
    grammar_path_provider = pi_v.PIAnyValue(pi.PIData(k_grammar_path_provider, None), antlr_config)
    pm.addItem(grammar_path_provider)

    k_grammar_generator = "k_grammar_generator"
    grammar_generator = grammar_compiler.AntlrInvoker(pi.PIData(k_grammar_generator, [k_grammar_path_provider]), k_grammar_path_provider, file_extension=XML_DAO_GRAMMAR_EXTENSION)
    pm.addItem(grammar_generator)


    print("RUN\n\n\n")
    pm.runPipeline()

    print("\n\n\nEND")



if __name__ == "__main__":
    main()