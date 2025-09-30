import src.pipeline.pipeline_item as pi

import src.postprocessing.output_preparation.compilers.shared.templates.jinja.t_j_base as tjb
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider

import src.model.dao as dao_m
import src.model.aggregable_entity as aggregable_e

"""
No differences at the moment from the super (Jinja Base) class.
"""
class TemplateJinjaASM(tjb.TemplateJinjaBase):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None, \
                key_template_name:str=None, \
                key_template_skeleton:str=None, \
                key_template_instance_data:str=None, \
                key_template_skeleton_provider_by_name:str=None, \
        ):
        super().__init__(pipeline_item_data, optional_external_data, key_template_name, key_template_skeleton, key_template_instance_data)
        self.key_template_skeleton_provider_by_name = key_template_skeleton_provider_by_name

        """
        
        tpbn = self.get_ith_input(additional_data, 2) if self.key_template_skeleton_provider_by_name is None else additional_data[self.key_template_skeleton_provider_by_name]
        if not isinstance(tpbn, template_provider.TemplateProviderByName):
            raise Exception("template provider by name needed")



            template_skeleton_dao = tpbn.provide_template_skeleton_by_name(template_name=[template_folder_path_base, "asm ___METTERE NELLE COSTANTI___"])
        """

    def translate_DAO_to_ASM(self, dao:dao_m.DAO) -> TranslatedSmartContract: #TODO
        asm_data = {}
        template_path = os.path.join('.', "Templates", "asm", "")
        name = "DAOML"
        output_folder = "ASM"
        #
        controls_relation:dict[str, set[str]] = {} # reverse directio of "is_controlled_by"
        entities_controllable:list[list[aggregable_e.AggregableEntity]] = [dao.roles.values(),  dao.committees.values()]
        for entities in entities_controllable:
            for e_slave in entities:
                masters:list[str] = e_slave.controllers
                for master_controller in masters:
                    slaves_set:set[str] = None
                    if master_controller in controls_relation:
                        slaves_set = controls_relation[master_controller]
                    else:
                        slaves_set = set()
                        controls_relation[master_controller] = slaves_set
                    slaves_set.add(e_slave.get_id())
        asm_data["roles"] = [
            {
                "name": r.role_name,
                "permissions": [p.get_id() for p in r.permissions],
                "controls": list(controls_relation[r.get_id()]) if r.get_id() in controls_relation else [],
                "aggregation": "" if len(r.aggregated) <= 0 else r.aggregated[0].get_name()
            }
            for r in dao.roles.values()
        ]
        asm_data["committees"] = [
            {
                "name": c.committee_description,
                "permissions": [p.get_id() for p in c.permissions],
                "controls":  list(controls_relation[c.get_id()]) if c.get_id() in controls_relation else [],
                "aggregation": "" if len(c.aggregated) <= 0 else c.aggregated[0].get_name()
            }
            for c in dao.committees.values()
        ] 
        asm_data["permissions"] = [
            {
                "name": p.get_id(),
                "governanceArea": p.ref_gov_area
            }
            for p in dao.permissions.values()
        ]
        asm_data["governanceAreas"] = [] # no governance area management defined at this stage of development
        asm_data["users"] = [] # no user pre-defined (apart from the Owner) at this stage of development
        asm_data["custom_operations"] = [] # no custom operation defined at this stage of development
        #
        return super().generate_file_from_template( #TODO
            template_path,
            name,
            output_folder,
            extension = ".asm",
            additional_parametrs=asm_data,
            reuse_additional_params_dit=True
        )

#TODO