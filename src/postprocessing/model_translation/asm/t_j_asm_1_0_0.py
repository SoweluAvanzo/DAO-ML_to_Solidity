import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.asm.t_j_asm as t_j_asm_base
import src.postprocessing.consts_template as c_t

import src.model.dao as dao_m
import src.model.diagram_manager as diagram_manager_m
import src.model.aggregable_entity as aggregable_e

import src.files.file_utils as fu
import src.utilities.utils as u


class TranslatedDAO_ASM_Jinja_1_0_0(t_j_asm_base.TranslatedDAO_ASM_Jinja):
    def __init__(self, dao: dao_m.DAO, dao_specific_data: dict,
                 is_convertible: bool = True
                 ):
        t_j_asm_base.TranslatedDAO_ASM_Jinja.__init__(
            self, dao, dao_specific_data, is_convertible=is_convertible)


class TranslatedDiagram_ASM_Jinja_1_0_0(t_j_asm_base.TranslatedDiagram_ASM_Jinja):
    def __init__(self, diagram: diagram_manager_m.DiagramManager, diagram_specific_data: dict,
                 is_convertible: bool = True
                 ):
        t_j_asm_base.TranslatedDiagram_ASM_Jinja.__init__(
            self, diagram, diagram_specific_data, is_convertible=is_convertible)


class TranslatorJinjaASM_1_0_0(t_j_asm_base.TranslatorJinjaASM):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_model: str = None
                 ):
        super().__init__(pipeline_item_data,
                         optional_external_data=optional_external_data,
                         key_model=key_model
                         )

    def new_translated_diagram(self, diagram: diagram_manager_m.DiagramManager, other_data=None) -> t_j_asm_base.TranslatedDiagram_ASM_Jinja:
        return TranslatedDiagram_ASM_Jinja_1_0_0(diagram, other_data, is_convertible=False)

    def new_translated_dao(self, diagram: diagram_manager_m.DiagramManager, dao: dao_m.DAO, other_data=None) -> t_j_asm_base.TranslatedDAO_ASM_Jinja:
        return TranslatedDAO_ASM_Jinja_1_0_0(dao, other_data)

    def translate_DAO(self, diagram: diagram_manager_m.DiagramManager,  dao: dao_m.DAO, additional_data=None) -> t_j_asm_base.TranslatedDAO_ASM_Jinja:
        asm_data = {}
        converted_dao = self.new_translated_dao(
            diagram, dao, other_data=asm_data)
        asm_dao_template_filename = "DAOML"
        dao_name = fu.sanitize_filename(dao.get_name())
        converted_dao.template_filename_input = f"{asm_dao_template_filename}.{c_t.ASM_FILE_EXTENSION}"
        converted_dao.translated_name_output = dao_name
        converted_dao.suggested_input_template_folders_path_from_base = c_t.FOLDERS_PATH_INPUT_ASM
        # reverse direction of "is_controlled_by"
        controls_relation: dict[str, set[str]] = {}
        entities_controllable: list[list[aggregable_e.AggregableEntity]] = [
            dao.roles.values(),  dao.committees.values()]
        for entities in entities_controllable:
            for e_slave in entities:
                masters: list[str] = e_slave.controllers
                for master_controller in masters:
                    slaves_set: set[str] = None
                    if master_controller in controls_relation:
                        slaves_set = controls_relation[master_controller]
                    else:
                        slaves_set = set()
                        controls_relation[master_controller] = slaves_set
                    slaves_set.add(e_slave.get_id())
        # now, do the actual "conversion" by populating the "other_data"
        asm_data["dao_name"] = dao_name
        asm_data["roles"] = [
            {
                "name": u.to_keyword(r.get_name()),
                "permissions": [u.to_keyword(p.allowed_action) for p in r.permissions],
                "controls": list(controls_relation[u.to_keyword(r.get_name())]) if u.to_keyword(r.get_name()) in controls_relation else [],
                "aggregation": "" if len(r.aggregated) <= 0 else u.to_keyword(r.aggregated[0].get_name())
            }
            for r in dao.roles.values()
        ]
        asm_data["committees"] = [
            {
                "name": u.to_keyword(c.get_name()),
                "permissions": [u.to_keyword(p.allowed_action) for p in c.permissions],
                "controls":  list(controls_relation[u.to_keyword(c.get_name())]) if u.to_keyword(c.get_name()) in controls_relation else [],
                "aggregation": "" if len(c.aggregated) <= 0 else u.to_keyword(c.aggregated[0].get_name())
            }
            for c in dao.committees.values()
        ]
        asm_data["permissions"] = [
            {
                "name": u.to_keyword(p.allowed_action),
                "governanceArea": u.to_keyword(dao.governance_areas[p.ref_gov_area].get_name()) if p.ref_gov_area in dao.governance_areas else None
            }
            for p in dao.permissions.values()
        ]
        asm_data["governanceAreas"] = [u.to_keyword(
            g.get_name()) for g in dao.governance_areas.values()]
        # no user pre-defined (apart from the Owner) at this stage of development
        asm_data["users"] = []
        # no custom operation defined at this stage of development
        asm_data["custom_operations"] = []
        #
        return converted_dao
