import os
import src.files.file_utils as files
import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi
import src.input.txt_file_input as tfi
import src.input.xml_file_input as xfi
import src.validators.xml_dao_validator as xvi
import src.generators.json_string_model_generator as jg
import src.generators.xml_string_model_generator as xsmg
import src.utilities.constants as consts
import src.cli.cli_executor as clie
import src.cli.antlr_invoker as grammar_compiler

import src.tests.pipeline.shared.pi_printer as pri
import src.tests.pipeline.shared.pi_str as pstr
import src.tests.pipeline.manual.t_file_1_process_pts as tf1_p_pts
import src.tests.pipeline.shared.pi_inputs_to_array as parr

FILE_NAME_TXT_TEST = "dao_test_1"
EXTENSION_JSON = "json"
FOLDER_PATH_TXT_TEST = files.concat_folder_filename(".","data","tests","pipeline")

FILE_NAME_XML_1 = "Travelhive_final_model" # "Travelhive_final_model_mini"
EXTENSION_XML = "xml"
FILE_PATH_XML = f"{files.concat_folder_filename('.','data',FILE_NAME_XML_1)}.{EXTENSION_XML}"
FILE_NAME_XML_SCHEMA = "XSD_DAO_ML"
EXTENSION_XML_SCHEMA = "xsd"
FILE_PATH_XML_SCHEMA = f"{files.concat_folder_filename('.','data',FILE_NAME_XML_SCHEMA)}.{EXTENSION_XML_SCHEMA}"

XML_DAO_GRAMMAR_FILENAME = "XMLParser"
XML_DAO_GRAMMAR_EXTENSION = "g4"
XML_DAO_GRAMMAR_FILEPATH = files.concat_folder_filename('.', 'src', 'parsers', 'xml', f"{XML_DAO_GRAMMAR_FILENAME}.{XML_DAO_GRAMMAR_EXTENSION}")


if __name__ == "__main__":
    print("AAAAAAAAAAAAAA")

    pm = pmp.PipelineManager()

    k_txt_file_input_pi = "k_txt_file_input_pi_1"
    file_path = f"{FOLDER_PATH_TXT_TEST}{os.sep}{FILE_NAME_TXT_TEST}.{EXTENSION_JSON}"
    txt_file_input_pi = tfi.TextFileInput(pi.PIData(k_txt_file_input_pi, None), file_path)
    pm.addItem(txt_file_input_pi)

    k_printer_echo_1 = "k_printer_echo_1"
    printer = pri.PIPrinter(pi.PIData(k_printer_echo_1, [k_txt_file_input_pi]), None, True)
    pm.addItem(printer)

    k_to_json = "k_json_generator"
    json_generator = jg.JsonStringModelGenerator(pi.PIData(k_to_json, [k_txt_file_input_pi]))
    pm.addItem(json_generator)
    
    k_printer_echo_2 = "k_printer_echo_2"
    printer_json = pri.PIPrinter(pi.PIData(k_printer_echo_2, [k_to_json]), None, True)
    pm.addItem(printer_json)

    # TODO: aggiungere valudazione generator che cerca di costruire gli oggetti del modello usando le giuste classi a partire dai dict generati dal JsonStringModelGenerator

    # TODO: aggiungere:
    # 1 )[V] lettore Text File del file xml
    #1.5)[ ] compile the parser
    # 2 )[V] XML validator
    # 3 )[V] XML_to_model_generator
    # 4 )[ ] model_to_json_repr
    # 5 )[ ] txt file_output
    # 6 )[ ] IL TRADUTTORE
    # 7 )[ ] jinja_outputter
    # 8 )[ ] etc
    
    # 1)

    k_xml_filepath_provider = "k_xml_filepath_provider"
    xml_filepath_provider = pstr.PIStr(pi.PIData(k_xml_filepath_provider, None), FILE_PATH_XML)
    pm.addItem(xml_filepath_provider)

    k_xml_file_input_pi = "k_xml_file_input_pi_1"
    xml_file_input_pi = xfi.TextFileInputXML(pi.PIData(k_xml_file_input_pi, [k_xml_filepath_provider]), xml_version="1.0")
    pm.addItem(xml_file_input_pi)

    k_printer_echo_xml = "k_printer_echo_xml"
    printer_json = pri.PIPrinter(pi.PIData(k_printer_echo_xml, [k_xml_file_input_pi]), None, True)
    pm.addItem(printer_json)

    #1.5) 

    k_grammar_generator = "k_grammar_generator"
    print(f"loading grammar at: {XML_DAO_GRAMMAR_FILEPATH}")
    grammar_generator = grammar_compiler.AntlrInvoker(pi.PIData(k_grammar_generator, None), XML_DAO_GRAMMAR_FILEPATH)
    pm.addItem(grammar_generator)


    # 2)

    k_xml_validator = "k_xml_validator"
    xml_validator = xvi.XMLDaoValidator(pi.PIData(k_xml_validator, [k_xml_file_input_pi, k_grammar_generator]), FILE_PATH_XML_SCHEMA)
    pm.addItem(xml_validator)

    k_tf1_p_pts = "k_tf1_p_pts"
    p_pts = tf1_p_pts.TestFile1_Processor_ParsedTreeStringer(pi.PIData(k_tf1_p_pts, [k_xml_validator]))
    pm.addItem(p_pts)
    k_printer_p_pts = "k_printer_p_pts"
    p_pts_printer = pri.PIPrinter(pi.PIData(k_printer_p_pts, [k_tf1_p_pts]), None, True)
    pm.addItem(p_pts_printer)

    # 3)

    k_xml_generator = "k_xml_generator"
    xml_generator = xsmg.XmlStringModelGenerator(pi.PIData(k_xml_generator, [k_xml_validator]))
    pm.addItem(xml_generator)

    k_string_model_printdebug = "k_string_model_printdebug"
    string_model_printdebug = pstr.PIStr(pi.PIData(k_string_model_printdebug, None), "\n\nModel created from XML!")
    pm.addItem(string_model_printdebug)
    k_toarray_model_printdebug = "k_toarray_model_printdebug"
    toarray_model_printdebug = parr.PIInputToArray(pi.PIData(k_toarray_model_printdebug, [k_string_model_printdebug, k_xml_generator]))
    pm.addItem(toarray_model_printdebug)

    k_printer_model_printdebug = "k_printer_model_printdebug"
    printer_model_printdebug = pri.PIPrinter(pi.PIData(k_printer_model_printdebug, [k_toarray_model_printdebug]), None, True)
    pm.addItem(printer_model_printdebug)

    #4)

    #k_model_to_json


    #8)
    k_commands_inputs = "k_commands_inputs"
    commands_inputs = {
        "k_dir": "dir",
        "k_anltr": f"java -jar {os.path.join(consts.EXTERNAL_LIBS_FOLDER, 'antlr-4.13.1.jar')}",
        "k_echo": "echo ciao mamma"
    }
    keys_commands = list(commands_inputs.keys())
    keys_commands_submitter = [f"{k_c}_submitter" for k_c in keys_commands]
    i = 0
    for k_cli_submitter in keys_commands_submitter:
        cli_submitter = pstr.PIStr(pi.PIData(k_cli_submitter, None), commands_inputs[keys_commands[i]])
        pm.addItem(cli_submitter)
        i += 1
    k_cli_exec = "k_cli_exec"
    cli_exec = clie.CLIExecutor(pi.PIData(k_cli_exec, keys_commands_submitter), inputs_as_separated_commands=True)
    pm.addItem(cli_exec)
    
    

    print("RUN\n\n\n")
    pm.runPipeline()

    print("\n\n\nEND")

