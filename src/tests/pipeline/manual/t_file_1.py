import os
import src.files.file_utils as files
import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi
import src.input.txt_file_input as tfi
import src.generators.json_string_model_generator as jg

import src.tests.pipeline.shared.pi_printer as pri

FILE_NAME = "dao_test_1"
EXTENSION = "json"
FOLDER_PATH = files.concat_folder_filename(".","data","tests","pipeline")


if __name__ == "__main__":
    print("AAAAAAAAAAAAAA")

    pm = pmp.PipelineManager()

    k_txt_file_input_pi = "k_txt_file_input_pi_1"
    file_path = f"{FOLDER_PATH}{os.sep}{FILE_NAME}.{EXTENSION}"
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

    print("RUN\n\n\n")
    pm.runPipeline()

    print("\n\n\nEND")

