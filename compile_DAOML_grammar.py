import src.files.file_utils as files
import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi

import src.cli.antlr_invoker as grammar_compiler

XML_DAO_GRAMMAR_FILENAME = "XMLParser"
XML_DAO_GRAMMAR_EXTENSION = "g4"
XML_DAO_GRAMMAR_FILEPATH = files.concat_folder_filename('.', 'src', 'parsers', 'xml', f"{XML_DAO_GRAMMAR_FILENAME}.{XML_DAO_GRAMMAR_EXTENSION}")


def main():
    print("AAAAAAAAAAAAAA")

    pm = pmp.PipelineManager()
    k_grammar_generator = "k_grammar_generator"
    print(f"loading grammar at: {XML_DAO_GRAMMAR_FILEPATH}")
    grammar_generator = grammar_compiler.AntlrInvoker(pi.PIData(k_grammar_generator, None), XML_DAO_GRAMMAR_FILEPATH)
    pm.addItem(grammar_generator)


    print("RUN\n\n\n")
    pm.runPipeline()

    print("\n\n\nEND")



if __name__ == "__main__":
    main()