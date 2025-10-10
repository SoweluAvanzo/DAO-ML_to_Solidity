import src.pipeline.pipeline_item as pi

import src.postprocessing.output_preparation.compilers.shared.templates.jinja.t_j_base as tjb
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider

import src.model.dao as dao_m
import src.model.aggregable_entity as aggregable_e

import src.files.file_utils as fu
import src.utilities.utils as u

"""
No differences at the moment from the super (Jinja Base) class.
"""


class TemplateJinjaASM(tjb.TemplateJinjaBase):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_template_name: str = None,
                 key_template_skeleton: str = None,
                 key_template_instance_data: str = None,
                 key_template_skeleton_provider_by_name: str = None,
                 ):
        super().__init__(pipeline_item_data, optional_external_data,
                         key_template_name, key_template_skeleton, key_template_instance_data)
        self.key_template_skeleton_provider_by_name = key_template_skeleton_provider_by_name

        """
        
        tpbn = self.get_ith_input(additional_data, 2) if self.key_template_skeleton_provider_by_name is None else additional_data[self.key_template_skeleton_provider_by_name]
        if not isinstance(tpbn, template_provider.TemplateProviderByName):
            raise Exception("template provider by name needed")



            template_skeleton_dao = tpbn.provide_template_skeleton_by_name(template_name=[template_folder_path_base, "asm ___METTERE NELLE COSTANTI___"])
        """

    def translate_DAO_to_ASM(self, dao: dao_m.DAO) -> TranslatedSmartContract:  # TODO
        asm_data = {}
        template_path = fu.concat_folder_filename('.', "Templates", "asm", "")
        name = dao.get_name()
        output_folder = "ASM"
        #
        # reverse directio of "is_controlled_by"
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
        print(f"\n debug {len(dao.permissions)} permissions")
        for p in dao.permissions.values():
            print(f"p {p.get_name()} -> {p.ref_gov_area}")
        print(f"debug {len(dao.governance_areas)} governanceArea")
        for p in dao.governance_areas.values():
            print(f"g.a. -> {str(p)}")

        asm_data["governanceAreas"] = [u.to_keyword(
            g.get_name()) for g in dao.governance_areas.values()]
        # no user pre-defined (apart from the Owner) at this stage of development
        asm_data["users"] = []
        # no custom operation defined at this stage of development
        asm_data["custom_operations"] = []
        #
        return super().generate_file_from_template(
            template_path,
            "DAOML",
            output_folder,
            extension=".asm",
            name_output=name,
            additional_parametrs=asm_data,
            reuse_additional_params_dit=True
        )

# TODO
