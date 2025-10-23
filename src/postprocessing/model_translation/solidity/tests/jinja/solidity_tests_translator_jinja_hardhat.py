
import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.solidity.tests.solidity_tests_translator as st_t
import src.postprocessing.model_translation.solidity.shared_utils as shared_utils_sol

import src.model.aggregable_entity as aggregable_entity
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.permission as p
import src.model.enums.user_functionalities_group_size as user_functionalities_group_size_module
import src.model.enums.entity_type_controllable as entity_type_controllable

import src.postprocessing.consts_template as consts_t

import src.files.file_utils as fu


class SolidityTestsTranslatorJinjaHardhat_1_0_0(st_t.SolidityTestsTranslator):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_model: str = None, is_optimized=True, key_is_optimized: str = None):
        super().__init__(pipeline_item_data,
                         optional_external_data=optional_external_data,
                         key_model=key_model)
        self.is_optimized = is_optimized
        self.key_is_optimized = key_is_optimized

#

    def __aggregable_entities_from_DAO(self, dao: d.DAO) -> list[aggregable_entity.AggregableEntity]:
        return [*dao.roles.values(), *dao.committees.values()]

    def generate_address_list(self, dao: d.DAO, entities: list[aggregable_entity.AggregableEntity]) -> list[str]:
        addresses_list = [f"addr{index}" for index, entity in enumerate(
            entities) if entity.get_id() != dao.owner_role.get_id()]
        return addresses_list

    def get_DAO_functionalities_ids(self, dao: d.DAO):
        """
        Override-designed
        """
        return shared_utils_sol.get_DAO_functionalities_ids(dao)

    def get_control_bitflags(self,
                             dao: d.DAO,
                             role_or_committee: aggregable_entity.AggregableEntity,
                             group_size: user_functionalities_group_size_module.UserFunctionalitiesGroupSize,
                             functionalities_ids: dict[str, int]
                             ):
        """
        Override-designed
        """
        return shared_utils_sol.get_control_bitflags(dao, role_or_committee, group_size, functionalities_ids)

    def compute_states_variables__roles_committee_computed_data(self, dao: d.DAO, functionalities_ids: dict[str, int], group_size: int):
        """
        Override-designed
        """
        return shared_utils_sol.get_roles_committee_computed_data(dao, functionalities_ids, group_size)

    def name_to_final_id(self, entity_to_data: dict[str, dict]) -> dict[str, int]:
        """
        Returns a dictionary mapping entity names to their final IDs.
        """
        return {value['final_id']: value['name'] for value in entity_to_data.values()}

    def generate_addresses_by_entity_value(self, dao: d.DAO, entity_to_data: dict[str, dict]) -> dict[int, dict[str, any]]:
        return shared_utils_sol.addresses_by_entities_data(dao, entity_to_data)

    def generate_control_tests_expected_results(self, entities: list[aggregable_entity.AggregableEntity], entity_to_data: dict[str, dict]) -> list[tuple[int, int, bool]]:

        controlledBy = {entity.get_id(): set(entity.controllers)
                        for entity in entities}
        return [
            (
                # the controller
                entity_to_data[entity.get_id()]['final_id'], \
                # the one who gets controlled by
                entity_to_data[controlled_entity.get_id()]['final_id'], \
                # the test
                entity.get_id() in controlledBy[controlled_entity.get_id()]
            ) \
            # cartesian product
            for entity in entities
            for controlled_entity in entities
        ]

    def generate_permission_tests_expected_results(self, dao: d.DAO,
                                                   entities: list[aggregable_entity.AggregableEntity],
                                                   entity_to_data: dict[str, dict]
                                                   ) -> list[tuple[int, str, bool]]:
        # Filter permissions that correspond to actual function invocations in the DAO. Hence, we need to remove voting and prpoposal permissions.
        postprocessed_permissions: list[p.Permission] = []
        for permission in dao.permissions.values():
            if permission.voting_right == False and permission.proposal_right == False:
                postprocessed_permissions.append(permission)

        permission_tests_expected_results = [(entity_to_data[entity.get_id()]['final_id'],
                                              fu.sanitize_filename(permission.allowed_action).replace(
                                                  "/", "_").replace("\\", ""),
                                              permission in entity.permissions and permission.voting_right == False and permission.proposal_right == False)
                                             for entity in entities
                                             for permission in postprocessed_permissions]
        return permission_tests_expected_results

    #

    def get_test_name_optimized(self, diagram: dm.DiagramManager, dao: d.DAO, additional_data=None):
        return "optimized_test_script_template"

    def get_test_name_simple(self, diagram: dm.DiagramManager, dao: d.DAO, additional_data=None):
        return "standard_test_script_template"

    def translate_DAO(self, diagram: dm.DiagramManager, dao: d.DAO, additional_data=None) -> st_t.TranslatedDAO_SolidityTest:
        dao_translated_data = {}
        dao_translated = st_t.TranslatedDAO_SolidityTest(
            dao, dao_translated_data, is_convertible=True)
        is_opt = self.is_optimized
        if self.key_is_optimized is not None:
            is_opt = not not self.key_is_optimized
        script_name = self.get_test_name_optimized(diagram, dao, additional_data=additional_data) if is_opt \
            else self.get_test_name_simple(diagram, dao, additional_data=additional_data)
        dao_name = fu.sanitize_filename(dao.get_name())
        dao_translated.template_filename_input = f"{script_name}.{consts_t.TESTS_FILE_EXTENSION}"
        dao_translated.translated_name_output = dao_name
        dao_translated.suggested_input_template_folders_path_from_base = consts_t.FOLDERS_PATH_INPUT_SOLIDITY_TEST

        # data calculation
        group_size: user_functionalities_group_size_module.UserFunctionalitiesGroupSize = dao.metadata.user_functionalities_group_size
        entities = self.__aggregable_entities_from_DAO(dao)
        functionalities_ids = self.get_DAO_functionalities_ids(dao)
        rccd = self.compute_states_variables__roles_committee_computed_data(
            dao, functionalities_ids, group_size)
        entity_to_data = rccd["entity_to_data"]
        owner_id_bitmask = entity_to_data[dao.owner_role.get_id()]['final_id']
        owner_role_value = owner_id_bitmask  # redundant, but kept for clarity
        committee_addresses = [ \
            # entity_data['final_id'] : entity_data['address']
            entity_data['address']
            for entity_data in entity_to_data.values()
            if entity_data['entity_type'] == entity_type_controllable.EntityTypeControllable.COMMITTEE.value
        ]
        #
        dao_translated_data["entity_to_data"] = self.name_to_final_id(
            entity_to_data)
        dao_translated_data["solidity_version"] = consts_t.SOLIDITY_VERSION_DEFAULT
        dao_translated_data["addresses_list"] = self.generate_address_list(
            dao, entities)
        dao_translated_data["addressesByEntityValue"] = self.generate_addresses_by_entity_value(
            dao, entity_to_data)
        dao_translated_data["owner"] = owner_id_bitmask
        dao_translated_data["DAO_name"] = dao_name
        dao_translated_data["owner_role_value"] = owner_role_value
        dao_translated_data["control_relation_results"] = self.generate_control_tests_expected_results(
            entities, entity_to_data)
        dao_translated_data["permissions"] = self.generate_permission_tests_expected_results(dao,
                                                                                             entities, entity_to_data)
        dao_translated_data["committee_addresses"] = committee_addresses
        #
        return dao_translated

    def translate_Diagram(self, diagram: dm.DiagramManager, additional_data=None) -> st_t.TranslatedDiagram_SolidityTest:
        return st_t.TranslatedDiagram_SolidityTest(diagram, additional_data, is_convertible=False)
