import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi

import src.model.base_entity as be
import src.model.diagram_manager as dm
import src.model.role as ro

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
import src.postprocessing.consts as consts_t
import src.utilities.utils as u
import src.utilities.comparisons as comp


def diffs(bd: dm.DiagramManager, nd: dm.DiagramManager) -> list[str]:
    """ Returns a list of errors and mismatches
    Args:
        bd (dm.DiagramManager): base Diagram (XML) to compare onto
        nd (dm.DiagramManager): new Diagram (JSON) to be compared
        field_path (str, optional): sequence of field names from the root obhect to the current field. Defaults to "".
        current_field_base (_type_, optional): _description_. Defaults to None.
        current_field_new (_type_, optional): _description_. Defaults to None.

    Returns:
        bool: _description_
    """
    return comp.check_differences(bd, nd)


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
k_input_xml = input_p_g_xml.key_output_for_next_step
add_pi_s(input_items_xml)

# ... model
mg_data_xml: pb_m_g.AdditionalDataModelGeneration = pb_m_g.ModelXMLGeneratordData(
    FILE_PATH_XML_SCHEMA,
    key_input_provider=k_input_xml
)
mg_p_g_xml: pb.PipelineItemsGenerated = pf_model_generator.new_pipeline_items(
    mg_data_xml)
model_items_xml = mg_p_g_xml.pipeline_items
k_model_generator_xml = mg_p_g_xml.key_output_for_next_step
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
k_input_json = input_p_g_json.key_output_for_next_step
add_pi_s(input_items_json)

# ... model
mg_data_json: pb_m_g.AdditionalDataModelGeneration = pb_m_g.ModelJSONGeneratordData(
    key_input_provider=k_input_json
)
mg_p_g_json: pb.PipelineItemsGenerated = pf_model_generator.new_pipeline_items(
    mg_data_json
)
model_items_json = mg_p_g_json.pipeline_items
k_model_generator_json = mg_p_g_json.key_output_for_next_step
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
model_xml: dm.DiagramManager = results_by_key[k_p_model_storer_xml]
model_json: dm.DiagramManager = results_by_key[k_p_model_storer_json]
if not isinstance(model_xml, dm.DiagramManager):
    printer_debug.print_error(
        f"Model XML is not a DiagramManager but: {type(model_xml)}")
if not isinstance(model_json, dm.DiagramManager):
    printer_debug.print_error(
        f"Model JSON is not a DiagramManager but: {type(model_json)}")

printer_debug.print_msg("\n\n\n now comparing...")


"""_summary_
def check_differences(dm_xml:dm.DiagramManager,dm_json:dm.DiagramManager) -> list[str]:
    errors: list[str] = []
    if dm_xml.get_id() != dm_json.get_id():
        errors.append(
            f"DM have different id: xml= {dm_xml.get_id() } ; JSON={ dm_json.get_id()}")
    if 
    return errors

"""

FIELDS_TO_FILTER = ["controlGraphGenerator",
                    # "dao_control_graph",
                    "control_graph"
                    ]
ids_checked = set()


def field_filter(current_field_base, current_field_new, field_path: str):
    if (field_path is None) or (field_path == ""):
        return False
    needs_to_be_filtered = False
    for ftf in FIELDS_TO_FILTER:
        if field_path.endswith(ftf):
            needs_to_be_filtered = True
            break
    if not needs_to_be_filtered:
        if isinstance(current_field_base, be.BaseEntity) and isinstance(current_field_new, be.BaseEntity):
            id_base = current_field_base.get_id()
            id_new = current_field_new.get_id()
            if (id_base in ids_checked) and (id_new in ids_checked):
                return True  # already checked
            # not found -> can check
            ids_checked.add(id_base)
            ids_checked.add(id_new)
        return False  # can check
    return True


differences: list[str] = comp.check_differences(
    model_xml, model_json,
    field_path_filterer=field_filter
)
if (differences is None) or (len(differences) <= 0):
    printer_debug.print_msg("All ok! ^_^")
else:
    printer_debug.print_error(f"ERROR: {len(differences)} differences:")
    for e in differences:
        printer_debug.print_error(e)

    def print_entity(entity: be.BaseEntity):
        printer_debug.print_error(
            f"\t\t - {entity.get_id()} : {entity.get_name()}")

    printer_debug.print_error("\n the roles were:")
    for m_t, model in [("xml", model_xml), ("json", model_json)]:
        printer_debug.print_error(f"\n... on {m_t}:")
        for dao_id, dao in model.daoByID.items():
            printer_debug.print_error(f"\tdao: {dao_id}")
            printer_debug.print_error("\t    owner role:")
            if dao.owner_role is None:
                printer_debug.print_error("\t\t NONE!!!")
            else:
                print_entity(dao.owner_role)
            printer_debug.print_error(f"\t {len(dao.roles)} roles:")
            for role_id, role in dao.roles.items():
                print_entity(role)
            printer_debug.print_error(",,, conditions:")
            for cond in dao.conditions:
                printer_debug.print_error(f"\t {cond}")


# python -m src.tests.pipeline.manual.t_read_json > OUT_t_read_json.txt
