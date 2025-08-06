import os
import src.utilities.constants as consts
import src.files.file_utils as files
import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi
import src.input.txt_file_input as tfi
import src.input.xml_file_input as xfi
import src.output.text_file_output as tfo
import src.cli.cli_executor as clie
#import src.cli.antlr_invoker as grammar_compiler
import src.validators.xml_dao_validator as xvi
import src.model_generators.json_string_model_generator as jg
import src.model_generators.xml_string_model_generator as xsmg
import src.postprocessing.output_preparation.model_to_json as m_json
#import src.postprocessing.model_conversion.translation_types as transl_types
import src.postprocessing.model_conversion.model_converter_configurable as mcc
import src.postprocessing.model_conversion.solidity.conversion_types_solidity as transl_types_sol
import src.postprocessing.model_conversion.solidity.optimized.jinja.jinja_optimized_versions as jinja_opt_versions

import src.postprocessing.model_conversion.conversion_types as ct

import src.pipeline.utilities.pi_printer as pri
import src.pipeline.utilities.pi_str as pstr
import src.pipeline.utilities.pi_any_value as pval
import src.pipeline.utilities.pi_inputs_to_array as parr
import src.tests.pipeline.manual.t_file_1_process_pts as tf1_p_pts

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

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

FILE_OUTPUT_MODEL_NAME = f"{FILE_NAME_XML_1}_JSONed"
FILE_OUTPUT_MODEL_EXTENSION = "json"
FILE_OUTPUT_MODEL_FILEPATH = files.concat_folder_filename('.', 'outputs', f"{FILE_OUTPUT_MODEL_NAME}.{FILE_OUTPUT_MODEL_EXTENSION}")


# def setup_input(pm:pmp.PipelineManager):
# def setup_model_generation(pm:pmp.PipelineManager):
# def set up_input(pm:pmp.PipelineManager):



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
    #0.5)[ ] compile the parser -> MUST be done before running this script
    # 1 )[V] lettore Text File del file xml
    # 2 )[V] XML validator
    # 3 )[V] XML_to_model_generator
    # 4 )[V] model_to_json_repr
    # 5 )[V] txt file_output
    # 6 )[T] IL TRADUTTORE
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
    """
    k_grammar_generator = "k_grammar_generator"
    print(f"loading grammar at: {XML_DAO_GRAMMAR_FILEPATH}")
    grammar_generator = grammar_compiler.AntlrInvoker(pi.PIData(k_grammar_generator, None), XML_DAO_GRAMMAR_FILEPATH)
    pm.addItem(grammar_generator)
    """

    # 2)

    k_xml_validator = "k_xml_validator"
    xml_validator = xvi.XMLDaoValidator(pi.PIData(k_xml_validator, [k_xml_file_input_pi]), FILE_PATH_XML_SCHEMA) #, k_grammar_generator
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

    k_model_to_json="k_model_to_json"
    model_to_json = m_json.JsonStringModelGenerator(pi.PIData(k_model_to_json, [k_xml_generator]), True, indent="\t")
    pm.addItem(model_to_json)
    k_model_to_json_printer = "k_model_to_json_printer"
    printer_model_jsonified = pri.PIPrinter(pi.PIData(k_model_to_json_printer, [k_model_to_json]), None, True)
    pm.addItem(printer_model_jsonified)

    # 5)
    k_additional_output_data = "k_additional_output_data"
    additional_metadata = {
        "mode": "w"
    }
    additional_output_data = pval.PIAnyValue(pi.PIData(k_additional_output_data, [k_model_to_json]), additional_metadata)
    pm.addItem(additional_output_data)
    k_model_text_to_file_output = "k_model_text_to_file_output"
    model_text_to_file_output = tfo.TextFileOutput(pi.PIData(k_model_text_to_file_output, [k_model_to_json, k_additional_output_data]), FILE_OUTPUT_MODEL_FILEPATH)
    pm.addItem(model_text_to_file_output)
    k_model_text_to_file_output_ok_printer = "k_model_text_to_file_output_ok_printer"
    model_text_to_file_output_ok_printer = pri.PIPrinter(pi.PIData(k_model_text_to_file_output_ok_printer, [k_model_text_to_file_output]), "DONE ^^", False)
    pm.addItem(model_text_to_file_output_ok_printer)

    #8)
    k_commands_inputs = "k_commands_inputs"
    commands_inputs = {
        "k_dir": "dir",
        "k_anltr": f"java -jar {os.path.join(consts.EXTERNAL_LIBS_FOLDER, 'antlr-4.13.1.jar')}",
        "k_echo": "echo ciao mamma",
        "k_multiple": "cd data & dir & cd .."
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
    
    

    # 6) TRADUTTORE

    # TODO generare gli inputs (per le key_ROBE del costruttore)

    converter_type = ct.ConversionTypes.SOLIDITY.value
    k_translator_type = "k_translator_type"
    pi_translator_type = pstr.PIStr(pi.PIData(k_translator_type, None), converter_type)
    pm.addItem(pi_translator_type)

    jinja_translator_version = jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value
    k_version_translator = "k_version_translator"
    pi_version_translator = pstr.PIStr(pi.PIData(k_version_translator, None), jinja_translator_version)
    pm.addItem(pi_version_translator)

    k_translator_target = "k_translator_target"
    pi_translator_target = pstr.PIStr(pi.PIData(k_translator_target, None), "1.0.0")
    pm.addItem(pi_translator_target)

    converter_solidity_subtype = transl_types_sol.TranslationTypesSolidity.OPTIMIZED.value
    k_converter_solidity_subtype = "k_converter_solidity_subtype"
    pi_converter_solidity_subtype = pstr.PIStr(pi.PIData(k_converter_solidity_subtype, None), converter_solidity_subtype)
    pm.addItem(pi_converter_solidity_subtype)

    k_translator = "k_translator"
    #translator = translator_sol_opt.SolidityConverterOptimized( \
    #translator = to_sol_j_1_0_0.SolidityConverterOptimizedJinja_1_0_0( \
    translator = mcc.ModelConverterConfigurable( \
            pi.PIData(k_translator, [k_xml_generator, k_translator_type, k_version_translator, k_translator_target, k_converter_solidity_subtype]), \
            key_model = k_xml_generator, \
            key_converter_type = k_translator_type, \
            key_converter_version = k_version_translator, \
            key_converter_target = k_translator_target                     
        )
    pm.addItem(translator)

    #

    k_printer__pre__translated_sol_opt = "k_printer__pre__translated_sol_opt"
    printer__pre__translated_sol_opt = pri.PIPrinter(pi.PIData(k_printer__pre__translated_sol_opt, [k_translator]), "\nPRINTING THE TRANSLATED STUFF\n", False)
    pm.addItem(printer__pre__translated_sol_opt)
    k_printer_translated_sol_opt = "k_printer_translated_sol_opt"
    printer_translated_sol_opt = pri.PIPrinter(pi.PIData(k_printer_translated_sol_opt, [k_translator]), None, True)
    pm.addItem(printer_translated_sol_opt)

    # TODO: 2025-07-26 FARE L'OUTPUT E LA TRADUZIONE

    # 7) template compiling
    """
    model_to_template_filename_jinja = mtt_mapper_j.ModelToTemplateMapperJinja()
    # TODO: it's STILL NEEDED TO DEFINE HOW TO PROVIDE (and retrieve?) ALL THE NECESSARY DATA 
    # .... maybe inside that ModelToTemplateMapperJinja instance?
     
    # model_to_template_filename_jinja[dm.DiagramManager.__class__.__name__] = None # no template for Diagram, at the moment
    model_to_template_filename_jinja[d.DAO.__class__.__name__] = files.concat_folder_filename(".", "Templates","DAOOptimizedGeneric.jinja")
    model_to_template_filename_jinja[c.Committee.__class__.__name__] = files.concat_folder_filename(".", "Templates","WHAT ELSE?.jinja")
    """
    # NOTE: other entries might be ID of "things" (Committees, usually) that are known in advance (even their ID as well) to have a specific, custom, user-defined
    # template rather than the "generic" pre-defined one 

    """
    # TODO: 2025-07-26 FARE L'OUTPUT E LA TRADUZIONE
    k_model_to_template_filename_jinja = "k_model_to_template_filename_jinja"
    model_to_template_filename_jinja_submitter = pval.PIAnyValue(pi.PIData(k_model_to_template_filename_jinja, [k_xml_generator]), model_to_template_filename_jinja)
    pm.addItem(model_to_template_filename_jinja_submitter)


    tjs = template_jinja_solidity.TemplateJinjaSolidity(... TODO ...)
    """


    print("RUN\n\n\n")
    pm.runPipeline()

    print("\n\n\nEND")

