
import src.pipeline.pipeline_item as pi
import src.postprocessing.model_translation.shared.model_translator_base as mcb
import src.postprocessing.model_translation.shared.templates.translation_result_model_templated as trmt
import src.postprocessing.model_translation.shared.translation_result_base as crb
import src.postprocessing.model_translation.shared.translation_result_model as trm
import src.postprocessing.model_translation.solidity.tests.solidity_tests_translator as stt

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c


"""

class TranslatedCommittee(crsp.TranslatedSubpart):
    def __init__(self, committee: c.Committee, committee_specific_data: dict,
                 is_convertible: bool = True
                 ):
        super().__init__(committee, committee_specific_data,
                         is_convertible=is_convertible
                         )

    def get_specific_data_name(self):
        return "committee_specific_data"


class TranslatedDAO(crsp.TranslatedSubpart):
    def __init__(self, dao: d.DAO, dao_specific_data: dict,
                 is_convertible: bool = True
                 ):
        super().__init__(dao, dao_specific_data,
                         is_convertible=is_convertible
                         )
        self.committees_by_id: dict[str, TranslatedCommittee] = {}

    def get_specific_data_name(self):
        return "dao_specific_data"

    def add_translated_committee(self, committee_translated: TranslatedCommittee):
        self.committees_by_id[committee_translated.entity.get_id(
        )] = committee_translated

    def toJSON(self):
        o = super().toJSON()
        o["committees_by_id"] = {
            i: self.committees_by_id[i].toJSON() for i in self.committees_by_id.keys()}
        return o


class TranslatedDiagram(crsp.TranslatedSubpart):
    def __init__(self, diagram: dm.DiagramManager, diagram_specific_data: dict,
                 is_convertible: bool = True
                 ):
        super().__init__(diagram, diagram_specific_data,
                         is_convertible=is_convertible
                         )
        self.daos_by_id: dict[str, TranslatedDAO] = {}

    def get_specific_data_name(self):
        return "diagram_specific_data"

    def add_translated_dao(self, dao_translated: TranslatedDAO):
        self.daos_by_id[dao_translated.entity.get_id()] = dao_translated

    def toJSON(self):
        o = super().toJSON()
        o["daos_by_id"] = {i: self.daos_by_id[i].toJSON()
                           for i in self.daos_by_id.keys()}
        return o

"""


class SolidityTestsTranslatorJinjaHardhat_1_0_0(stt.SolidityTestsTranslator):
    def __init__(self, pipeline_item_data: pi.PIData, key_model: str = None):
        super().__init__(pipeline_item_data, key_model=key_model)

    def translate_DAO_test(self, diagram: dm.DiagramManager, dao: d.DAO, additional_data=None) -> trmt.TranslatedDAOTemplated:
        dao_translated_data = {}
        dao_translated = trmt.TranslatedDAOTemplated(
            dao, dao_translated_data, is_convertible=True)
        """
        From TestGenerator



            def generate_test_script(self, folder_template_path: str) -> list[TranslatedSmartContract]:
                if self.optimized:
                    script_name = "optimized_test_script_template"  
                else:
                    script_name = "standard_test_script_template"
                return [\
                    self.generate_test_from_template(folder_template_path, script_name) \
                        ] # TODO: add the other tests, if any
            
            def generate_test_from_template(self, template_path: str, name: str, output_folder="test", extension=".js") -> TranslatedSmartContract:
                # Define the full path to the template file
                file_name_and_path = f"{template_path}/{name}{extension}.jinja"
                # Initialize an empty list to store each rendered line
                rendered_lines = []
                addresses_list = self.generate_address_list()
                addressesByEntityValue = self.generate_addresses_by_entity_value()
                owner_id_bitmask = self.entity_to_data[ self.dao.owner_role.role_id]['final_id']
                owner_role_value = owner_id_bitmask # redundant, but kept for clarity
                permission_tests_expected_results = self.generate_permission_tests_expected_results()
                
                with open(file_name_and_path, 'r', encoding='utf-8') as f:
                    template_content = f.read()
                    template = Template(template_content)
                    rendered_lines = template.render(
                        entity_to_data = self.name_to_final_id(),
                        solidity_version=self.context.solidity_version,
                        addresses_list=addresses_list,
                        addressesByEntityValue=addressesByEntityValue,
                        owner=owner_id_bitmask,
                        DAO_name=self.dao.dao_name.replace(" ", "_"),
                        owner_role_value=owner_role_value,
                        control_relation_results=self.generate_control_tests_expected_results(),
                        permissions=permission_tests_expected_results,
                        committee_addresses=[ \
                            #entity_data['final_id'] : entity_data['address'] \
                            entity_data['address'] \
                            for entity_data in self.entity_to_data.values() \
                                if entity_data['entity_type'] == EntityTypeControllable.COMMITTEE.value \
                        ]
                    ).splitlines()

                # Return a TranslatedSmartContract object with the list of rendered lines
                return TranslatedSmartContract(rendered_lines, self.context.dao.dao_name + "_test", folder=output_folder, extension=extension)
            
        """
        # TODO
        return dao_translated_data

    def translate_Diagram_test(self, diagram: dm.DiagramManager, additional_data=None) -> trmt.TranslatedDiagramTemplated:
        return trmt.TranslatedDiagramTemplated(diagram, additional_data, is_convertible=False)
