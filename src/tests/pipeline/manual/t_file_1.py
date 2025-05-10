import os
import src.files.file_utils as files
import src.pipeline.pipeline_manager as pmp
# import src.pipeline.pipeline_item as pip
import src.input.txt_file_input as tfi

import src.tests.pipeline.shared.pi_printer as pri

FILE_NAME = "dao_test_1"
EXTENSION = "json"
FOLDER_PATH = files.concat_folder_filename(".","data","tests","pipeline")


if __name__ == "__main__":
    print("AAAAAAAAAAAAAA")

    pm = pmp.PipelineManager()

    k_txt_file_input_pi = "k_txt_file_input_pi_1"
    file_path = f"{FOLDER_PATH}{os.sep}{FILE_NAME}.{EXTENSION}"
    txt_file_input_pi = tfi.TextFileInput(k_txt_file_input_pi, file_path)
    pm.addItem(txt_file_input_pi)

    k_printer_echo_1 = "k_printer_echo_1"
    printer = pri.PIPrinter(k_printer_echo_1, [k_txt_file_input_pi], None, True)
    pm.addItem(printer)

    print("RUN\n\n\n")
    pm.runPipeline()

    print("\n\n\nEND")

