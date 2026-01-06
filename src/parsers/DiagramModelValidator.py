import src.pipeline.pipeline_item as pi
import src.validators.base_validator as bv


import src.model.base_entity as be
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c
import src.model.aggregable_entity as ae
import src.model.role as r
import src.model.permission as p
import src.model.governance_area as ga
import src.model.relation as rel
import src.model.enums.relation_type as rt

import src.control_graph.control_graph_basic as cgb

import src.utilities.errors as e_C


class EntityToSetLinksExtractor:
    def get_collection(self, aggregable_entity: ae.AggregableEntity):
        raise Exception(e_C.ERROR_TEXT__NOT_IMPLEMENTED)

    def extract_links(self, aggregable_entity: ae.AggregableEntity) -> set[str]:
        return (perm_id for perm_id in self.get_collection(aggregable_entity))


class PermissionsGetter(EntityToSetLinksExtractor):
    def get_collection(self, aggregable_entity: ae.AggregableEntity) -> set[str]:
        return aggregable_entity.permissions


class AggregatedGetter(EntityToSetLinksExtractor):
    def get_collection(self, aggregable_entity: ae.AggregableEntity) -> set[str]:
        return aggregable_entity.aggregated

#


class OutwardLink:
    def __init__(self,
                 collections_same_link_type: list[dict[str, ae.AggregableEntity]],
                 entity_to_set_links_extractor: EntityToSetLinksExtractor,
                 link_type: str,
                 # a collection of the keys of objects, like the "permissions" field
                 keys_linked_objects: set[str]
                 ):
        self.collections_same_link_type = collections_same_link_type
        self.entity_to_set_links_extractor: EntityToSetLinksExtractor = entity_to_set_links_extractor: EntityToSetLinksExtractor
        self.link_type = link_type
        self.keys_linked_objects = keys_linked_objects

#


class DiagramModelValidator(bv.BaseValidator):
    # TODO actually (2026-01-05), it's more like a "Already-created-model-Validator"....

    # TODO: deve ricevere un oggetto (JSON/dict) e verificare che rispetti il modello denro il model

    """
    Also: (see "xml_dao_validator.py")
        check_relation_graphs(d, "aggregation_level", "aggregates"))
        check_relation_graphs(d, "federation_level", "federates_into"))
        check_cyclic_dependencies(d, "aggregates"))
        check_cyclic_dependencies(d, "federates_into"))
        check_relations_in_same_DAO(d, early_return=False))
    """

    """
    NOTE:
    "check_relations_in_same_DAO" checks if any object (Role/Committee/Relation/Permission/etc) is referring to
    something that is NOT present in the same DAO they belong.
    The possible references are: ["federates_into","aggregates","associated_to","is_controlled_by"].
    Implementation notes:
    a) for each DAO, collect all of those object IDs (including the DAO's one) into a set, which is the value of a map whose keys are the DAOs' IDs (one set for each individual DAO)
    b) for each DAO, collect all of those references (again, in a set for each DAO)
    c.1) perform the "subtraction" "b-a" (i.e., all references in "b" not present in "a")
    c.2) partition the "leftover after the subtraction" into "present in any other DAO | totally missing link" for a better debugging/printing
    c.3) IF c is empty -> ok ELSE error
    """

    def ids_to_nowhere(self, ids_to_check: set[str], ids_to_check_into: set[str]) -> set[str]:
        return ids_to_check.difference(ids_to_check_into)

    def other_dao_with_BE_of_ID(self, diagram: dm.DiagramManager, current_dao: d.DAO, id_to_check: str) -> d.DAO:
        """
        Returns the DAO (if present) having a "BaseEntity" whose ID coincides with the provided one.
        Such DAO must differ from the provided one, because the latter is the one eere the ID cames from.
        (Such ID is an "outward link", like a Permission's ID inside a Role/Committee)
        """
        for dao_id, dao in diagram.daoByID.items():
            if dao_id != current_dao.get_id():  # exclude current DAO
                where_to_check: list[dict[str, be.BaseEntity]] = [
                    dao.permissions,
                    dao.roles,
                    dao.committees,
                    dao.governance_areas
                ]
                for possible_holder in where_to_check:
                    if id_to_check in possible_holder:
                        return dao
        return None

    def check_roles_committess_out_links(self, diagram: dm.DiagramManager) -> list[str]:
        # 1) All Roles/Committees 's "associated_to" (which are IDs) must be among the Permissions' IDs
        # 2) All Roles' "aggregates" (which are IDs) must be existing Roles' IDs
        # 3) All Committees' "aggregates" (which are IDs) must be existing Committees' IDs
        # 4) All Roles/Committees 's "is_controlled_by" (which are IDs) must be among the Roles/Committees ' IDs
        errors: list[str] = []
        permissions_getter = PermissionsGetter()
        aggregated_getter = AggregatedGetter()
        # CHECKS ON EACH DAO
        for dao_id, dao in diagram.daoByID.items():
            all_permissions_ids_in_dao: set[str] = set(
                k for k in dao.permissions.keys())
            all_roles_ids_in_dao: set[str] = set(k for k in dao.roles.keys())
            all_committees_ids_in_dao: set[str] = set(
                k for k in dao.committees.keys())
            all_aggregable_entities_in_dao: set[str] = all_roles_ids_in_dao.union(
                all_committees_ids_in_dao
            )
            # all_associates: set[str] = set()  # 1)
            links_to_check: list[OutwardLink] = [
                OutwardLink(  # 1)
                    [
                        dao.roles,
                        dao.committees
                    ],
                    permissions_getter,
                    "associated_to",
                    all_permissions_ids_in_dao
                ),
                OutwardLink(  # 2)
                    [
                        dao.roles
                    ],
                    aggregated_getter,
                    "aggregates",
                    all_aggregable_entities_in_dao
                ),
                OutwardLink(  # 3)
                    [
                        dao.committees
                    ],
                    aggregated_getter,
                    "aggregates",
                    all_aggregable_entities_in_dao
                ),
                OutwardLink(  # 1)
                    [
                        dao.roles,
                        dao.committees
                    ],
                    permissions_getter,  # TODO: which one?
                    "is_controlled_by",
                    all_permissions_ids_in_dao  # TODO: which one?
                ),
            ]
            # role.per
            # 1)
            associatables_dicts: list[dict[str, ae.AggregableEntity]] = [
                dao.roles,
                dao.committees
            ]
            is_role = True
            for associatables_dict in associatables_dicts:
                for aggregable_entity_id, aggregable_entity in associatables_dict.items():
                    if aggregable_entity is None:
                        other_dao_might_belong = self.other_dao_with_BE_of_ID(
                            diagram,
                            dao,
                            aggregable_entity_id
                        )
                        errors.append(
                            f"In DAO '{dao_id}' ({dao.get_name()}) , {'Role' if is_role else 'Committee'} with ID '{aggregable_entity_id}' {'do not exists' if other_dao_might_belong is None else f'exists in ANOTHER DAO (id={other_dao_might_belong.get_id()}; name= {other_dao_might_belong.get_name()})'}"
                        )
                    permissions_ids_not_existing: set[str] = self.ids_to_nowhere(
                        set(perm_id for perm_id in aggregable_entity.permissions.keys()),
                        all_permissions_ids_in_dao
                    )
                    if (permissions_ids_not_existing is not None) and (len(permissions_ids_not_existing) > 0):
                        # error:
                        for id_unexisting_permission in permissions_ids_not_existing:
                            other_dao_might_belong = self.other_dao_with_BE_of_ID(
                                diagram,
                                dao,
                                id_unexisting_permission
                            )
                            errors.append(
                                f"In DAO '{dao_id}' ({dao.get_name()}) , {aggregable_entity.__class__.__name__} '{aggregable_entity_id}' ({aggregable_entity.get_name()}) has 'associates_to' '{id_unexisting_permission}' pointing to {'unexisting permission' if other_dao_might_belong is None else f' somewhere else in ANOTHER DAO (id={other_dao_might_belong.get_id()}; name= {other_dao_might_belong.get_name()})'}"
                            )
                        # TODO: DOES THEM EXIST IN OTHER DAOs?
                is_role = not is_role
            # TODO: 2, 3, 4
            # for role ... for committee ...
        return errors

    def validate(self, input_to_validate: dict) -> bool:
        errors: list[str] = []
        if isinstance(input_to_validate, dm.DiagramManager):
            errors_r_c_out_links = self.check_roles_committess_out_links(
                input_to_validate)
            if (errors_r_c_out_links is not None) and (len(errors_r_c_out_links) > 0):
                errors.extend(errors_r_c_out_links)
            del errors_r_c_out_links  # release the RAM
            # TODO: do all other checks
        else:
            errors.append(
                f"the given input to check is not a DiagramManager, but a: {type(input_to_validate)}")
        if len(errors) == 0:
            return True
        self.print_error < (
            f"{len(errors)} ERRORS in validating given model input:")
        for er in errors:
            self.print_error(er)
        return False
        # raise Exception("TODO : NOT IMPLEMENTED YET (31-12-2025)")
