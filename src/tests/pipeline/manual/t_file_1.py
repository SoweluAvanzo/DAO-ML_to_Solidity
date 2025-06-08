import os
import src.files.file_utils as files
import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi
import src.input.txt_file_input as tfi
import src.input.xml_file_input as xfi
import src.generators.json_string_model_generator as jg

import src.tests.pipeline.shared.pi_printer as pri
import src.tests.pipeline.shared.pi_str as pstr

FILE_NAME_TXT_TEST = "dao_test_1"
EXTENSION_JSON = "json"
FOLDER_PATH_TXT_TEST = files.concat_folder_filename(".","data","tests","pipeline")

FILE_NAME_XML_1 = "Travelhive_final_model"
EXTENSION_XML = "xml"
FILE_PATH_XML = f"{files.concat_folder_filename('.','data',FILE_NAME_XML_1)}.{EXTENSION_XML}"


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
    # [ ] lettore Text File del file xml
    # [ ] XML validator
    # [ ] XML_to_model_generator
    # [ ] model_to_json_repr
    # [ ] txt file_output
    # [ ] IL TRADUTTORE
    # [ ] jinja_outputter
    # [ ] etc
    
    k_xml_filepath_provider = "k_xml_filepath_provider"
    xml_filepath_provider = pstr.PIStr(pi.PIData(k_xml_filepath_provider, None), FILE_PATH_XML)
    pm.addItem(xml_filepath_provider)

    k_xml_file_input_pi = "k_xml_file_input_pi_1"
    xml_file_input_pi = xfi.TextFileInputXML(pi.PIData(k_xml_file_input_pi, [k_xml_filepath_provider]), xml_version="1.0")
    pm.addItem(xml_file_input_pi)

    k_printer_echo_xml = "k_printer_echo_xml"
    printer_json = pri.PIPrinter(pi.PIData(k_printer_echo_xml, [k_xml_file_input_pi]), None, True)
    pm.addItem(printer_json)

    print("RUN\n\n\n")
    pm.runPipeline()

    print("\n\n\nEND")

