
import src.files.file_utils as files
import src.pipeline.utilities.pi_str as pstr
import src.pipeline.utilities.pi_any_value as pval
import src.pipeline.utilities.pi_printer as pri

import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi
import src.input.txt_file_input as tfi
import src.output.text_file_output as tfo

# import src.templates.template_jinja_solidity as tjs
import src.templates.template_jinja_base as tjb

JINJA_TEMPLATE_NAME = "test_jinja"
JINJA_TEMPLATE_EXTENSION = "jinja"
JINJA_TEMPLATE_FILEPATH = files.concat_folder_filename(
    ".", "Templates", "test_scripts", f"{JINJA_TEMPLATE_NAME}.{JINJA_TEMPLATE_EXTENSION}")

OUTPUT_COMPILED = files.concat_folder_filename(
    ".", "outputs", f"{JINJA_TEMPLATE_NAME}.compiled")

if __name__ == "__main__":
    print("AAAAAAAAAAAAAA TEST JINJAAAAAAA")

    pm = pmp.PipelineManager()

    k_jinja_template_filepath = "k_jinja_template_filepath"
    jinja_template_filepath = pstr.PIStr(
        pi.PIData(k_jinja_template_filepath, None), JINJA_TEMPLATE_FILEPATH)
    pm.addItem(jinja_template_filepath)

    k_jinja_template_input = "k_jinja_template_input"
    jinja_template_input = tfi.TextFileInput(
        pi.PIData(k_jinja_template_input, [k_jinja_template_filepath]))
    pm.addItem(jinja_template_input)

    jinja_test_data = {
        "name": "test manual Marco",
        "flag": True,
        "a_list": [3, 1, 4, 1, 5, 9, 2, 65, "pi"],
        "pets": [
            ("pacioccola", "cat"),
            ("puzzolo", "rat"),
            ("beppe", "dog"),
            ("fluffolo", "platapus")
        ],
        "lenlen": lambda x: f"{len(x)} is the length of: {x}"
    }
    k_jinja_test_data_provider = "k_jinja_test_data_provider"
    jinja_test_data_provider = pval.PIAnyValue(
        pi.PIData(k_jinja_test_data_provider, None), jinja_test_data)
    pm.addItem(jinja_test_data_provider)

    # the real test

    k_jinja_name = "k_jinja_name"
    jinja_name = pstr.PIStr(
        pi.PIData(k_jinja_name, None), "TEST JINJA manuyally")
    pm.addItem(jinja_name)

    k_jinja_template_compiler = "k_jinja_template_compiler"
    jinja_template_compiler = tjb.CompilerTemplateJinjaBase(
        pi.PIData(k_jinja_template_compiler, [
            k_jinja_name,
            k_jinja_template_input,
            k_jinja_test_data_provider
        ]
        ),
        key_template_name=k_jinja_name,
        key_template_skeleton=k_jinja_template_input,
        key_template_instance_data=k_jinja_test_data_provider
    )
    pm.addItem(jinja_template_compiler)

    # output
    k_compiled_printer = "k_compiled_printer"
    compiled_printer = pri.PIPrinter(
        pi.PIData(k_compiled_printer, [k_jinja_template_compiler]), None, True)
    pm.addItem(compiled_printer)

    k_compiled_to_file = "k_compiled_to_file"
    compiled_to_file = tfo.TextFileOutput(
        pi.PIData(k_compiled_to_file, [k_jinja_template_compiler]), OUTPUT_COMPILED)
    pm.addItem(compiled_to_file)

    print("RUN\n\n\n")
    pm.runPipeline()

    print("\n\n\nEND")
