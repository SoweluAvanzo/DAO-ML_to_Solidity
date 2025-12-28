import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi

import src.model.diagram_manager as dm

import src.phases_builders.shared as pb_shared
import src.phases_builders.phase_builder as pb
import src.phases_builders.input_fetch as pb_i_f
import src.phases_builders.model_generation as pb_m_g

import src.input.xml_file_input as xfi
import src.validators.xml.xml_dao_validator as xvi
import src.validators.validation_result_to_errors as vete
# import src.model_generators.json_string_model_generator as jg
import src.model_generators.xml_string_model_generator as xsmg

import src.pipeline.utilities.pi_str as pstr
import src.pipeline.utilities.pi_any_value as pval
import src.pipeline.utilities.pi_chain_store_releaser_branching as pstore

import src.files.file_utils as files
import src.postprocessing.consts_template as consts_t
import src.utilities.utils as u

printer_debug = u.PrinterDebug()
pm = pmp.PipelineManager(
    printer_debug=printer_debug
)


def add_pi_s(items: list[pi.PipelineItem]):
    for item in items:
        pm.addItem(item)


# TODO: read both the XML & JSON files and compare the generated model
# constants

FILE_NAME_XML_1 = "Travelhive_final_model"  # T_DAO_1.value
EXTENSION_XML = "xml"
FILE_PATH_XML = files.concat_folder_filename(
    consts_t.DEFAULT_BASE_FOLDER_INPUT, f"{FILE_NAME_XML_1}.{EXTENSION_XML}")
FILE_NAME_XML_SCHEMA = "XSD_DAO_ML"
EXTENSION_XML_SCHEMA = "xsd"
FILE_PATH_XML_SCHEMA = files.concat_folder_filename(
    consts_t.DEFAULT_BASE_FOLDER_INPUT, f"{FILE_NAME_XML_SCHEMA}.{EXTENSION_XML_SCHEMA}")

FILE_PATH_JSON = files.concat_folder_filename(
    ".",
    "out",
    "diagram__dao_a10f2b1a_ee5b_4b99_b531_a704edb909ca.json"
)

# shared things
key_unique_producer = pb_shared.KeyUniqueProducerSimpleSequential()

pf_input = pb_i_f.InputFactory(
    key_unique_producer,
    printer_debug=printer_debug,
    file_input_caching=None
)

pf_model_generator = pb_m_g.ModelGeneratorFactory(
    key_unique_producer,
    printer_debug=printer_debug
)

# XML

# ... input
input_data_xml = pb_i_f.FileXMLAdditionalDataSubPhase(
    filepath=FILE_PATH_XML,
    xml_version="1.0.0",
    should_strip_line=True
)

input_p_g_xml: pb.PipelineItemsGenerated = pf_input.new_pipeline_items(
    input_data_xml
)
input_items_xml = input_p_g_xml.pipeline_items
k_input_xml = input_p_g_xml.key_last_pi
add_pi_s(input_items_xml)

# ... model

mg_data_xml: pb_m_g.AdditionalDataModelGeneration = pb_m_g.ModelXMLGeneratordData(
    FILE_PATH_XML_SCHEMA,
    key_input_provider=k_input_xml
)
mg_p_g_xml: pb.PipelineItemsGenerated = pf_model_generator.new_pipeline_items(
    mg_data_xml)
model_items_xml = mg_p_g_xml.pipeline_items
k_model_generator_xml = mg_p_g_xml.key_last_pi
add_pi_s(model_items_xml)

k_p_model_storer_xml = "k_p_model_storer_xml"
p_model_storer_xml = pstore.PIChainStoreReleaserBranching(
    pi.PIData(k_p_model_storer_xml, [k_model_generator_xml]),
    printer_debug=printer_debug
)
pm.addItem(p_model_storer_xml)


# JSON

# ... input
input_data_json = pb_i_f.FileJSONAdditionalDataSubPhase(
    filepath=FILE_PATH_JSON,
    should_strip_line=True
)
input_p_g_json: pb.PipelineItemsGenerated = pf_input.new_pipeline_items(
    input_data_json
)
input_items_json = input_p_g_json.pipeline_items
k_input_json = input_p_g_json.key_last_pi
add_pi_s(input_items_json)

# ... model

mg_data_json: pb_m_g.AdditionalDataModelGeneration = pb_m_g.ModelJSONGeneratordData(
    key_input_provider=k_input_json
)
mg_p_g_json: pb.PipelineItemsGenerated = pf_model_generator.new_pipeline_items(
    mg_data_json
)
model_items_json = mg_p_g_json.pipeline_items
k_model_generator_json = mg_p_g_json.key_last_pi
printer_debug.print_msg(f"model_items_json: {model_items_json}")
printer_debug.print_msg(f"k_model_generator_json: {k_model_generator_json}")
add_pi_s(model_items_json)

k_p_model_storer_json = "k_p_model_storer_json"
p_model_storer_json = pstore.PIChainStoreReleaserBranching(
    pi.PIData(k_p_model_storer_json, [k_model_generator_json]),
    printer_debug=printer_debug
)
pm.addItem(p_model_storer_json)

# IN THE END

printer_debug.print_msg("\n\n\n running...")
results_by_key: dict = pm.runPipeline()
printer_debug.print_msg("runned:")
keys = list(results_by_key.keys())
printer_debug.print_msg(keys)

printer_debug.print_msg("\n\n\n getting model...")
model_xml = results_by_key[k_p_model_storer_xml]
model_json = results_by_key[k_p_model_storer_json]
if not isinstance(model_xml, dm.DiagramManager):
    printer_debug.print_error(
        f"Model XML is not a DiagramManager but: {type(model_xml)}")
if not isinstance(model_json, dm.DiagramManager):
    printer_debug.print_error(
        f"Model JSON is not a DiagramManager but: {type(model_json)}")

printer_debug.print_msg("\n\n\n now comparing...")

# python -m src.tests.pipeline.manual.t_read_json > OUT_t_read_json.txt
