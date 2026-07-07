import networkx as nx

import src.pipeline.pipeline_item as pi

import src.validators.base_validator as bv
import src.validators.validation_result as validation_res

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

import src.utilities.utils as u
import src.utilities.errors as e_C


class EntityToSetLinksExtractor:
    def get_collection(self, aggregable_entity: ae.AggregableEntity):
        raise Exception(e_C.ERROR_TEXT__NOT_IMPLEMENTED)

    def extract_links(self, aggregable_entity: ae.AggregableEntity) -> set[str]:
        return set([perm_id for perm_id in self.get_collection(aggregable_entity)])


class PermissionsGetter(EntityToSetLinksExtractor):
    def get_collection(self, aggregable_entity: ae.AggregableEntity) -> set[str]:
        return aggregable_entity.permissions


class AggregatedGetter(EntityToSetLinksExtractor):
    def get_collection(self, aggregable_entity: ae.AggregableEntity) -> set[str]:
        return aggregable_entity.aggregated


class ControllersGetter(EntityToSetLinksExtractor):
    def get_collection(self, aggregable_entity: ae.AggregableEntity) -> set[str]:
        return aggregable_entity.controllers

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
        self.entity_to_set_links_extractor = entity_to_set_links_extractor
        self.link_type = link_type
        self.keys_linked_objects = keys_linked_objects

#


class DiagramModelValidator(bv.BaseValidator):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None):
        super().__init__(pipeline_item_data,
                         printer_debug=printer_debug
                         )

    #

    def aggregation_level_extractor(self, aggr_entity: ae.AggregableEntity) -> int:
        return aggr_entity.aggregation_level

    def federation_level_extractor(self, aggr_entity: ae.AggregableEntity) -> int:
        return aggr_entity.federation_level

    #

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
        """
        Took inspiration from "xml_dao_validator.py".
        This check implements both the "check_relations_in_same_DAO" check and the check "compare_subsets" aganst
        the possible 4 references (["federates_into","aggregates","associated_to","is_controlled_by"]).
        The latter are:
        # 1) All Roles/Committees 's "associated_to" (which are IDs) must be among the Permissions' IDs
        # 2) All Roles' "aggregates" (which are IDs) must be existing Roles' IDs
        # 3) All Committees' "aggregates" (which are IDs) must be existing Committees' IDs
        # 4) All Roles/Committees 's "is_controlled_by" (which are IDs) must be among the Roles/Committees ' IDs
        """
        errors: list[str] = []
        permissions_getter = PermissionsGetter()
        aggregated_getter = AggregatedGetter()
        controllers_getter = ControllersGetter()
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
                OutwardLink(  # 4)
                    [
                        dao.roles,
                        dao.committees
                    ],
                    controllers_getter,
                    "is_controlled_by",
                    all_aggregable_entities_in_dao
                ),
            ]
            index_ol = 0
            for ol in links_to_check:
                associatables_dicts: list[dict[str, ae.AggregableEntity]
                                          ] = ol.collections_same_link_type

                for associatables_dict in associatables_dicts:
                    for aggregable_entity_id, aggregable_entity in associatables_dict.items():
                        if aggregable_entity is None:
                            other_dao_might_belong = self.other_dao_with_BE_of_ID(
                                diagram,
                                dao,
                                aggregable_entity_id
                            )
                            errors.append(
                                f"In DAO '{dao_id}' ({dao.get_name()}), check # {index_ol} , {aggregable_entity.__class__.__name__} with ID '{aggregable_entity_id}' {'do not exists' if other_dao_might_belong is None else f'exists in ANOTHER DAO (id={other_dao_might_belong.get_id()}; name= {other_dao_might_belong.get_name()})'}"
                            )
                        outward_links_ids_not_existing: set[str] = self.ids_to_nowhere(
                            ol.entity_to_set_links_extractor.extract_links(
                                aggregable_entity),
                            ol.keys_linked_objects
                        )
                        if (outward_links_ids_not_existing is not None) and (len(outward_links_ids_not_existing) > 0):
                            # error:
                            for id_unexisting_link in outward_links_ids_not_existing:
                                other_dao_might_belong = self.other_dao_with_BE_of_ID(
                                    diagram,
                                    dao,
                                    id_unexisting_link
                                )
                                errors.append(
                                    f"In DAO '{dao_id}' ({dao.get_name()}), check # {index_ol} , {aggregable_entity.__class__.__name__} with ID '{aggregable_entity_id}' ({aggregable_entity.get_name()}) has '{ol.link_type}' '{id_unexisting_link}' pointing to {'unexisting link' if other_dao_might_belong is None else f' somewhere else in ANOTHER DAO (id={other_dao_might_belong.get_id()}; name= {other_dao_might_belong.get_name()})'}"
                                )
                index_ol += 1
        return errors

    # a.k.a. "check_relation_graphs"
    def check_relations_under_level_hierarchy(self, diagram: dm.DiagramManager) -> list[str]:
        """
        For each "AggregableEntity", check the relations between those instances and both their "aggregated" and "federated_committees":
        each "link" must check, respectively, "aggregation_level" and "federation_level" (which are int or None) and their
        values must be "in order", i.e. must be lesser or equal
        """
        errors: list[str] = []
        extractor_type = type(ae.AggregableEntity.get_aggregated)
        for dao_id, dao in diagram.daoByID.items():
            entities_with_hierarchy_relation: list[dict[str, ae.AggregableEntity]] = [
                dao.roles,
                dao.committees
            ]
            is_role = True
            for entity_dict_by_id in entities_with_hierarchy_relation:
                # for each aggregable entity (in a specific dict), check their "relations regulated by a level-based hierarchy"
                for aggr_entity_id, aggr_entity in entity_dict_by_id.items():
                    relations_and_level_to_check: list[
                        tuple[
                            dict[str, ae.AggregableEntity],
                            int, str,
                            extractor_type
                        ]
                    ] = [
                        (aggr_entity.aggregated,
                         aggr_entity.aggregation_level,
                         "aggregation_level",
                         ae.AggregableEntity.get_aggregation_level  # "Java-alike method reference"
                         ),
                        (aggr_entity.federated_committees,
                         aggr_entity.federation_level,
                         "federation_level",
                         ae.AggregableEntity.get_federation_level  # "Java-alike method reference"
                         ),
                    ]
                    for t in relations_and_level_to_check:
                        relations: dict[str, ae.AggregableEntity] = t[0]
                        level: int = t[1]
                        relation_name: str = t[2]
                        level_extractor = t[3]
                        # THE CHECK
                        if level is not None:
                            for linked_entity_id, linked_entity in relations.items():
                                if linked_entity is None:
                                    errors.append(
                                        f"NONE in relation with level-based hierarchy '{relation_name}' violation: in DAO '{dao_id}' (named: '{dao.get_name()}'), the {aggr_entity.__class__.__name__} '{aggr_entity_id}' (named: {aggr_entity.get_name()}) has NONE relation with a {'Role' if is_role else 'Committee'} id: {linked_entity_id}"
                                    )
                                else:
                                    # (passing the "self" to the "static method")
                                    level_link = level_extractor(linked_entity)
                                    if (level_link is not None) and (level_link > level):
                                        # ERROR
                                        errors.append(
                                            f"relation with level-based hierarchy '{relation_name}' violation: in DAO '{dao_id}' (named: '{dao.get_name()}'), the {aggr_entity.__class__.__name__} '{aggr_entity_id}' (named: {aggr_entity.get_name()}) has level '{level}' and is in relation with {linked_entity.__class__.__name__} '{linked_entity_id}' (named: {linked_entity.get_name()}) with level '{level_link}'"
                                        )
                        # else : should I print it at a debug level?
                is_role = not is_role
        return errors

    def check_cyclic_dependencies(self, diagram: dm.DiagramManager) -> list[str]:
        # must not have cycles in Roles+Committees by considering the links "aggregates" / "Federates_into"
        errors: list[str] = []

        for dao_id, dao in diagram.daoByID.items():
            # graph preparation ...
            graph = nx.DiGraph()
            # .. by defining the vertexes first (to recycle them)
            all_aggregable_entities_in_dao: dict[str, ae.AggregableEntity] = {
                k: v
                for k, v in dao.roles.items()
            }
            for k, v in dao.committees.items():
                all_aggregable_entities_in_dao[k] = v
            # (vertex addition)
            for ae_id, edge_aggregable_entity in all_aggregable_entities_in_dao.items():
                graph.add_node(ae_id)
            # ... then adding the edges ...
            edge_link_extractors_names = [
                # "Java-alike method reference"
                (ae.AggregableEntity.get_aggregated, "aggregated"),
                (ae.AggregableEntity.get_federated_committees,  # "Java-alike method reference"
                 "federated_committees"),
                (ae.AggregableEntity.get_controllers,  # "Java-alike method reference"
                 "controllers")
            ]
            lastly_added_edges: list[tuple[str, str]] = None
            for ele_and_name in edge_link_extractors_names:
                ele = ele_and_name[0]
                ele_name: str = ele_and_name[1]
                if lastly_added_edges is not None:
                    graph.remove_edges_from(lastly_added_edges)
                    lastly_added_edges = None  # free the memory
                lastly_added_edges = []
                for ae_id, edge_aggregable_entity in all_aggregable_entities_in_dao.items():
                    # (passing the "self" to the "static method")
                    dict_destination_link: dict[str, ae.AggregableEntity] = ele(
                        edge_aggregable_entity)
                    # for each outward link, create the edge
                    outward_links_generator = dict_destination_link.keys() \
                        if isinstance(dict_destination_link, dict) else \
                        [l for l in dict_destination_link]  # set-alike, like "controllers"
                    for destination_link_id in outward_links_generator:
                        edge: tuple[str, str] = (ae_id, destination_link_id)
                        lastly_added_edges.append(edge)
                        graph.add_edge(edge[0], edge[1])
                # THE TEST (of a particular type of link)
                all_cycles: list[set[str]] = [
                    set(c) for c in nx.simple_cycles(graph)
                ]
                cycles: list[set[str]] = [
                    c for c in all_cycles
                    if len(c) > 1  # 1 == self-reference, which is admissible
                ]
                if len(cycles) > 0:  # ERROR
                    err_str = [
                        f"In DAO '{dao_id}' (name: {dao.get_name()}), while checking the link '{ele_name}' across the Aggregable Entities, we have {len(cycles)} cycles:"
                    ]
                    i = 0
                    for c_s in cycles:
                        c: list[str] = list(c_s)
                        c.sort()
                        err_str.append(
                            f"\t - {i}\t): [{', '.join(c)}]"
                        )
                        i += 1
                    errors.append(
                        "\n".join(err_str)
                    )
                else:
                    self.print_msg(
                        f"debug: In DAO '{dao_id}' (name: {dao.get_name()}), while checking the link '{ele_name}', we have {len(all_cycles)} self-referencing cycles")
                    if len(all_cycles) > 0:
                        for c in all_cycles:
                            self.print_msg(
                                f"\t -): [{', '.join(c)}]"
                            )

                all_cycles = None  # free the memory
                cycles = None  # free the memory
            lastly_added_edges = None  # free the memory

        return errors

    def validate(self, input_to_validate: dict) -> validation_res.ValidationResult:
        errors: list[str] = []
        if isinstance(input_to_validate, dm.DiagramManager):
            check_fn_type = type(self.check_roles_committess_out_links)
            checks_to_run: list[check_fn_type] = [
                self.check_roles_committess_out_links,
                self.check_relations_under_level_hierarchy,
                self.check_cyclic_dependencies
            ]
            """
            # TODO: do all other checks (06-01-2026) (see "xml_dao_validator.py"):
                check_cyclic_dependencies(d, "aggregates"))
                check_cyclic_dependencies(d, "federates_into"))
            """
            for check_fn in checks_to_run:
                errors_r_c_out_links: list[str] = check_fn(input_to_validate)
                if (errors_r_c_out_links is not None) and (len(errors_r_c_out_links) > 0):
                    errors.extend(errors_r_c_out_links)
                del errors_r_c_out_links  # release the RAM

        else:
            errors.append(
                f"the given input to check is not a DiagramManager, but a: {type(input_to_validate)}")
        # in he end
        is_ok = len(errors) == 0
        res = validation_res.ValidationResult(
            validation_result=is_ok,
            errors=errors,
            input_consumed=input_to_validate,
            additional_data=None
        )
        if not is_ok:
            self.print_error(
                f"{len(errors)} ERRORS in validating given model input:")
            for er in errors:
                self.print_error(er)
        else:
            self.print_msg("Diagram instance has no errors ^_^")
        return res
