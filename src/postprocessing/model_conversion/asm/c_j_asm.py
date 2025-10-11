import src.pipeline.pipeline_item as pi


import src.postprocessing.model_conversion.shared.model_converter_base as mcb
import src.postprocessing.model_conversion.shared.conversion_result_base as crb
import src.postprocessing.model_conversion.shared.templates.conversion_result_template as crt
import src.postprocessing.model_conversion.solidity.solidity_converter_general as stg

import src.model.dao as dao_m
import src.model.diagram_manager as diagram_manager_m
import src.model.aggregable_entity as aggregable_e

import src.files.file_utils as fu
import src.utilities.utils as u


class ConvertedDAO_ASM_Jinja_1_0_0(crt.ConvertedSubpartTemplated):
    def __init__(self, dao: dao_m.DAO, dao_specific_data: dict,
                 is_convertible: bool = True
                 ):
        crt.ConvertedSubpartTemplated.__init__(
            self, dao, dao_specific_data, is_convertible=is_convertible)
        # dict of ( output_filename, compiled_template )
        """
        self.other_subparts_converted_by_name: dict[str,
            crt.ConvertedSubpartTemplated] = {}
        """


class ConvertedDiagram_ASM_Jinja_1_0_0(crt.ConvertedSubpartTemplated):
    def __init__(self, diagram: diagram_manager_m.DiagramManager, diagram_specific_data: dict,
                 is_convertible: bool = True
                 ):
        crt.ConvertedSubpartTemplated.__init__(
            self, diagram, diagram_specific_data, is_convertible=is_convertible)
        self.dao_converted_by_id: dict[str, ConvertedDAO_ASM_Jinja_1_0_0] = {}
        # dict of ( output_filename, compiled_template )
        """
        self.other_subparts_converted_by_name: dict[str,
            crt.ConvertedSubpartTemplated] = {}
        """

    def add_dao_converted(self, dao_c: ConvertedDAO_ASM_Jinja_1_0_0):
        self.dao_converted_by_id[dao_c.get_id()] = dao_c

#


class ConverterJinjaASM(mcb.ModelConverterBase):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_model: str = None
                 ):
        super().__init__(pipeline_item_data,
                         key_model=key_model
                         )
        self.optional_external_data = optional_external_data

    def new_translated_diagram(self, diagram: diagram_manager_m.DiagramManager, other_data=None) -> ConvertedDiagram_ASM_Jinja_1_0_0:
        return ConvertedDiagram_ASM_Jinja_1_0_0(diagram, other_data)

    def new_translated_dao(self, diagram: diagram_manager_m.DiagramManager, dao: dao_m.DAO, other_data=None) -> ConvertedDAO_ASM_Jinja_1_0_0:
        return ConvertedDAO_ASM_Jinja_1_0_0(dao, other_data)

    #

    def translate_DAO_to_ASM(self, diagram: diagram_manager_m.DiagramManager,  dao: dao_m.DAO) -> ConvertedDAO_ASM_Jinja_1_0_0:
        asm_data = {}
        converted_dao = self.new_translated_dao(
            diagram, dao, other_data=asm_data)
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
        """
        print(f"\n debug {len(dao.permissions)} permissions")
        for p in dao.permissions.values():
            print(f"p {p.get_name()} -> {p.ref_gov_area}")
        print(f"debug {len(dao.governance_areas)} governanceArea")
        for p in dao.governance_areas.values():
            print(f"g.a. -> {str(p)}")
        """
        asm_data["governanceAreas"] = [u.to_keyword(
            g.get_name()) for g in dao.governance_areas.values()]
        # no user pre-defined (apart from the Owner) at this stage of development
        asm_data["users"] = []
        # no custom operation defined at this stage of development
        asm_data["custom_operations"] = []
        #
        return converted_dao

    def convert(self, model: diagram_manager_m.DiagramManager, additional_data=None) -> crb.ModelConversionResultBase:
        diagram_specific_data = None
        diagram_converted = self.new_translated_diagram(
            model, other_data=diagram_specific_data)
        for dao in model.daoByID.values():
            dao_converted = self.translate_DAO_to_ASM(model, dao)
            diagram_converted.add_dao_converted(dao_converted)
        return diagram_converted
