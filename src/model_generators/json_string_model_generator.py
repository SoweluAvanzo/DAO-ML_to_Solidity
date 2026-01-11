import json

import src.pipeline.pipeline_item as pi
import src.model_generators.base_generator as bg

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

VERSION = "1.0.0"


class JsonStringModelGenerator(bg.BaseGenerator):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         printer_debug=printer_debug
                         )
        self.print_msg(f"print_msg -> creating JsonStringModelGenerator")
        print(f"print -> creating JsonStringModelGenerator")
        # self._diagram_fields_optionality: dict[str, bool] = None  # lazy
        # self._dao_fields_optionality: dict[str, bool] = None  # lazy
        # self._committee_fields_optionality: dict[str, bool] = None  # lazy
        # self._role_fields_optionality: dict[str, bool] = None  # lazy
        # self._permission: dict[str, bool] = None  # lazy
        # self._gov: dict[str, bool] = None  # lazy
        # lazy
        self._fields_mandatority_by_classname: dict[str, dict[str, bool]] = {}

    def run(self, inputs):
        return super().run(inputs)

    def generate(self, data, additional_data=None):
        self.print_msg(
            f"\n\n\n JsonStringModelGenerator IS GENERATING (with data of type: {type(data)}) \n\n")
        try:
            self.print_msg(
                f"{self.__class__.__name__} is generating JSON with these keys in data (type: {type(data)}): {list(data.__dict__.keys()) if isinstance(data, dict) else len(data)}")
            self.print_msg(
                f"{self.__class__.__name__} is generating JSON with these keys in additional_data (type: {type(additional_data)}): {list((additional_data.__dict__ if not isinstance(additional_data, dict) else additional_data).keys()) if additional_data is not None else 'NO-KEYS'}")
            data_obj: dict = data  # assumption
            is_string = u.is_string_or_list(data)
            if is_string:
                data_obj = json.loads(data)
            elif is_string != None:
                # list
                if len(data) <= 0:
                    raise Exception(
                        "The given data is an empty list of lines (of JSON things)")
                for i in range(len(data)):
                    if not isinstance(data[i], str):
                        raise Exception(
                            f"The data at line # {i} is not a string, but a: {type(data[i])}")
                data_obj = json.loads("".join(data))
            else:
                if not isinstance(data, dict):
                    self.print_error(
                        f"The given data is not a JSON string nor a list (of strings?) but of: type({data})")
            self.print_msg("LOG: Now, parsing the JSON data of the diagram!")
            return self.parse_diagram(data_obj)
        except Exception as e:
            self.print_error(e)
            import traceback
            traceback.print_exception(e)
        return None

    def _exception_missing_data(self, what, where, add_msg: str = None):
        raise Exception(
            f"Missing {what} field(s) in class {where}!{'' if add_msg is None else add_msg}")

    def _check_get_is_primitive(self, what, clazz: type, field_name: str, primitive_type):
        if (what is not None) and (not isinstance(what, primitive_type)):
            raise Exception(
                f"While parsing JSON {clazz.__name__}, the supposed {field_name} is not a {primitive_type.__name__}: {type(what)}")
        return what

    def _check_is_dict(self, what, entity: be.BaseEntity, field_name: str):
        if not isinstance(what, dict):
            raise Exception(
                f"While parsing JSON {type(entity)} (id: {entity.get_id()}), the supposed {field_name} is not a dict: {type(what)}")

    def _check_is_list_str(self, what, entity: be.BaseEntity, field_name: str):
        if not isinstance(what, list):
            raise Exception(
                f"While parsing JSON {type(entity)} (id: {entity.get_id()}), the supposed {field_name} is not a list: {type(what)}")
        for i in range(len(what)):
            if not isinstance(what[i], str):
                raise Exception(
                    f"While parsing JSON {type(entity)} (id: {entity.get_id()}), the {i}-th (0-based) element in the list {field_name} is not a string: {type(what[i])}")

    def check_fields(self, obj: dict, fields: dict[str, bool], className: str, add_msg: str = None) -> bool:
        """
        Given a set of fields (second parameter) and their "mandatority", check if all of them are present
        """
        missing = []
        optional_f = []
        for f, is_mandatory in fields.items():
            if f not in obj:
                if is_mandatory:
                    missing.append(f)
                else:
                    optional_f.append(f)
        optional_msg = None if len(optional_f) == 0 else \
            f"[{', '.join(optional_f)}] fields were optional."
        if len(missing) == 0:
            if optional_msg is not None:
                self.print_msg(f"In class {className}, {optional_msg}")
            return True
        self._exception_missing_data(f"[{', '.join(missing)}]{'' if optional_msg is None else f' ({optional_msg})'})",
                                     className, add_msg=add_msg)
        return False

    def _fields_of(self, clazz: type) -> dict[str, bool]:
        """
        Get the set of fields (passed onto "check_fields(...)") for a specific class
        """
        class_name: str = clazz.__name__
        if class_name in self._fields_mandatority_by_classname:
            fields = self._fields_mandatority_by_classname[class_name]
        else:
            fields = self._fields_of_by_class_name(clazz, class_name)
            self._fields_mandatority_by_classname[class_name] = fields
        return fields

    #
    # Override-designed
    #

    # ... FIELDS

    def _fields_of_by_class_name(self, clazz: type, class_name: str) -> dict[str, bool]:
        """
        Override-designed
        """
        fields: dict[str, bool] = None
        # not using "match" because it needs constant values
        # in decreasing order of encounter-frequencies
        # TODO altre classi in model
        if issubclass(clazz, rel.Relation):
            fields = self._fields_of_relation()
        elif issubclass(clazz, r.Role):
            fields = self._fields_of_role()
        elif issubclass(clazz, c.Committee):
            fields = self._fields_of_committee()
        elif issubclass(clazz, p.Permission):
            fields = self._fields_of_permission()
        elif issubclass(clazz, d.DAO):
            fields = self._fields_of_dao()
        elif issubclass(clazz, ga.GovernanceArea):
            fields = self._fields_of_governance_area()
        elif issubclass(clazz, dm.DiagramManager):
            fields = self._fields_of_diagram()
        return fields

    def _fields_of_diagram(self):
        """
        Override-designed
        """
        return {
            # ... BasicEntity part
            "id": True,
            #
            "daoByID": True,
            "relations_by_dao": True,
            "controlGraphGenerator": False
        }

    def _fields_of_relation(self):
        """
        Override-designed
        """
        return {
            "dao_id": False,
            "relation_type": True,
            "from_id": True,
            "content": True
        }

    def _fields_of_dao(self):
        """
        Override-designed
        """
        return {
            # ... BasicEntity part
            "id": False,
            #
            "dao_name": True,
            "mission_statement": True,
            "hierarchical_inheritance": True,
            "owner_role": True,  # it's an ID, a str
            "roles": True,
            "committees": True,
            "governance_areas": True,
            "permissions": True,
            "dao_control_graph": False,
            # "metadata" can be calculated as: dao.metadata.save_user_functionalities_group_size(dao.roles, dao.committees)
            "metadata": False,
            "assignment_conditions": True,
            "voting_conditions": True,
            "proposal_conditions": True,
            "decision_making_methods": False,
            "conditions": True,
            # TODO: can be False (and therefore be calculated if missing) ?
            "role_and_committee_voting_right_dict": True,
            # TODO: can be False (and therefore be calculated if missing) ?
            "role_and_committee_proposal_right_dict": True
        }

    def _fields_of_aggregable_entity(self):
        """
        Override-designed
        """
        return {
            # ... BasicEntity part
            "id": True,
            # ... AggregableEntity part
            "permissions": True,
            "controllers": True,
            "aggregated": True,
            "federated_committees": True,
            "aggregation_level": False,
            "federation_level": False
        }

    def _fields_of_role(self):
        """
        Override-designed
        """
        role_data_obj = self._fields_of_aggregable_entity()
        role_data_obj["role_name"] = True
        role_data_obj["role_assignment_method"] = True
        role_data_obj["n_agent_min"] = False
        role_data_obj["n_agent_max"] = False
        role_data_obj["agent_type"] = False
        return role_data_obj

    def _fields_of_committee(self):
        """
        Override-designed
        """
        role_data_obj = self._fields_of_aggregable_entity()
        role_data_obj["committee_description"] = True
        role_data_obj["voting_condition"] = True
        role_data_obj["proposal_condition"] = True
        role_data_obj["decision_making_method"] = True
        role_data_obj["member_entities"] = True
        return role_data_obj

    def _fields_of_permission(self):
        """
        Override-designed
        """
        return {
            # ... BasicEntity part
            "id": True,
            #
            "allowed_action": True,
            "permission_type": True,
            "ref_gov_area": None,
            "voting_right": None,
            "proposal_right": None
        }

    def _fields_of_governance_area(self):
        """
        Override-designed
        """
        return {
            # ... BasicEntity part
            "id": True,
            #
            "gov_area_description": True,
            "implementation": True
        }

    # ... PARSING

    def _resolve_cross_references(self, diagram: dm.DiagramManager,  dao_id: str, dao: d.DAO, dao_data_obj: dict):
        # the "AggregableEntities", like Roles and Committees, has 2 lists of pointers (aggregated & federated_committees)
        # and also all Committees' "committee.member_entities"
        is_committee = False
        for aggregable_entities_dict in [dao.roles, dao.committees]:
            for ae_id, ae in aggregable_entities_dict.items():
                # alreaddy done
                """
                permissions_ids: list[str] = ae.permissions
                ae.permissions = {
                    permission_id: dao.permissions[permission_id]
                    for permission_id in permissions_ids
                }
                """
                #
                aggregated_ids: list[str] = ae.aggregated
                ae.aggregated = {
                    ag_id: dao.roles[ag_id] if ag_id in dao.roles else dao.committees[ag_id]
                    for ag_id in aggregated_ids
                }
                #
                federated_committees_ids: list[str] = ae.federated_committees
                ae.federated_committees = {
                    fc_id: dao.roles[fc_id] if fc_id in dao.roles else dao.committees[fc_id]
                    for fc_id in federated_committees_ids
                }
                if is_committee:
                    com: c.Committee = ae
                    member_entities_ids: list[str] = com.member_entities
                    com.member_entities = {
                        committee_id: dao.committees[committee_id]
                        if committee_id in dao.committees else (
                            dao.roles[committee_id]
                            if committee_id in dao.roles
                            else None
                        )
                        for committee_id in member_entities_ids
                    }
            is_committee = not is_committee

    def parse_governance_area(self, diagram: dm.DiagramManager,  dao_id: str, dao: d.DAO, governance_area_data_obj: dict) -> ga.GovernanceArea:
        governance_area_fields = self._fields_of(ga.GovernanceArea)
        self.check_fields(governance_area_data_obj,
                          governance_area_fields, ga.GovernanceArea.__name__)
        governance_area = ga.GovernanceArea(
            self._check_get_is_primitive(
                governance_area_data_obj["id"],
                ga.GovernanceArea,
                "id",
                str
            ),
            self._check_get_is_primitive(
                governance_area_data_obj["gov_area_description"],
                ga.GovernanceArea,
                "gov_area_description",
                str
            ),
            self._check_get_is_primitive(
                governance_area_data_obj["implementation"],
                ga.GovernanceArea,
                "implementation",
                str
            )
        )
        return governance_area

    def _parse_aggregable_entity_part(self, diagram: dm.DiagramManager,  dao_id: str, dao: d.DAO, aggr_entity_data_obj: dict, aggregable_entity: ae.AggregableEntity):
        # let's assume the "id" is already set
        # ... permissions
        permissions_ids: list[str] = aggr_entity_data_obj["permissions"]
        # just str id but should be the instance, for now
        self._check_is_list_str(
            permissions_ids, aggregable_entity, "permissions")
        aggregable_entity.permissions = {
            perm_id: dao.permissions[perm_id] if perm_id in dao.permissions else None
            for perm_id in permissions_ids
        }
        # ... controllers
        controllers_ids: list[str] = aggr_entity_data_obj["controllers"]
        # just str id but should be the instance, for now
        self._check_is_list_str(
            controllers_ids, aggregable_entity, "controllers")
        aggregable_entity.controllers = set(controllers_ids)
        # ... aggregated
        aggregated_ids: list[str] = aggr_entity_data_obj["aggregated"]
        # just str id but should be the instance, for now
        self._check_is_list_str(
            aggregated_ids, aggregable_entity, "aggregated")
        aggregable_entity.aggregated = aggregated_ids
        # ... federated_committees
        federated_committees_ids: list[str] = aggr_entity_data_obj["federated_committees"]
        # just str id but should be the instance, for now
        self._check_is_list_str(federated_committees_ids,
                                aggregable_entity, "federated_committees")
        aggregable_entity.federated_committees = federated_committees_ids
        aggregable_entity.aggregation_level = aggr_entity_data_obj[
            "aggregation_level"] if "aggregation_level" in aggr_entity_data_obj else 0

    def parse_permission(self, diagram: dm.DiagramManager,  dao_id: str, dao: d.DAO, permission_data_obj: dict) -> p.Permission:
        permission_fields = self._fields_of(p.Permission)
        self.check_fields(permission_data_obj,
                          permission_data_obj, p.Permission.__name__)
        permission = p.Permission(
            self._check_get_is_primitive(
                permission_data_obj["id"],
                p.Permission,
                "id",
                str
            ),
            self._check_get_is_primitive(
                permission_data_obj["allowed_action"],
                p.Permission,
                "allowed_action",
                str
            ),
            self._check_get_is_primitive(
                permission_data_obj["permission_type"],
                p.Permission,
                "permission_type",
                str
            ),
            self._check_get_is_primitive(
                permission_data_obj["ref_gov_area"],
                p.Permission,
                "ref_gov_area",
                str
            ) if "ref_gov_area" in permission_data_obj else None,
            self._check_get_is_primitive(
                permission_data_obj["voting_right"],
                p.Permission,
                "voting_right",
                bool
            ) if "voting_right" in permission_data_obj else False,
            self._check_get_is_primitive(
                permission_data_obj["proposal_right"],
                p.Permission,
                "proposal_right",
                bool
            ) if "proposal_right" in permission_data_obj else False
        )
        self.print_msg(f"... ... Permission: id={permission.get_id()}")
        return permission

    def parse_committee(self, diagram: dm.DiagramManager,  dao_id: str, dao: d.DAO, committee_data_obj: dict) -> c.Committee:
        committee_fields = self._fields_of(c.Committee)
        self.check_fields(committee_data_obj,
                          committee_data_obj, c.Committee.__name__)
        committee = c.Committee(
            self._check_get_is_primitive(
                committee_data_obj["id"],
                c.Committee,
                "id",
                str
            ),
            self._check_get_is_primitive(
                committee_data_obj["committee_description"],
                c.Committee,
                "committee_description",
                str
            ),
            self._check_get_is_primitive(
                committee_data_obj["voting_condition"],
                c.Committee,
                "voting_condition",
                str
            ),
            self._check_get_is_primitive(
                committee_data_obj["proposal_condition"],
                c.Committee,
                "proposal_condition",
                str
            ),
            self._check_get_is_primitive(
                committee_data_obj["decision_making_method"],
                c.Committee,
                "decision_making_method",
                str
            )
        )
        self._parse_aggregable_entity_part(
            diagram, dao_id, dao, committee_data_obj, committee)
        # just str id but should be the instance, for now
        member_entities_ids: list[str] = committee_data_obj["member_entities"]
        self._check_is_list_str(member_entities_ids,
                                committee, "member_entities")
        committee.member_entities = member_entities_ids
        return committee

    def parse_role(self, diagram: dm.DiagramManager,  dao_id: str, dao: d.DAO, role_data_obj: dict) -> r.Role:
        role_fields = self._fields_of(r.Role)
        self.check_fields(role_data_obj, role_data_obj, r.Role.__name__)
        role = r.Role(
            self._check_get_is_primitive(
                role_data_obj["id"],
                r.Role,
                "id",
                str
            ),
            self._check_get_is_primitive(
                role_data_obj["role_name"],
                r.Role,
                "role_name",
                str
            ),
            self._check_get_is_primitive(
                role_data_obj["role_assignment_method"],
                r.Role,
                "role_assignment_method",
                str
            ),
            self._check_get_is_primitive(
                role_data_obj["n_agent_min"],
                r.Role,
                "n_agent_min",
                int
            ),
            self._check_get_is_primitive(
                role_data_obj["n_agent_max"],
                r.Role,
                "n_agent_max",
                int
            ),
            self._check_get_is_primitive(
                role_data_obj["agent_type"],
                r.Role,
                "agent_type",
                str
            )
        )
        self._parse_aggregable_entity_part(
            diagram, dao_id, dao, role_data_obj, role)
        return role

    def parse_dao(self, diagram: dm.DiagramManager,  dao_id: str, dao_data_obj: dict) -> d.DAO:
        dao_fields = self._fields_of(d.DAO)
        self.check_fields(dao_data_obj, dao_fields, d.DAO.__name__)
        dao = d.DAO(
            self._check_get_is_primitive(
                dao_data_obj["id"],
                d.DAO,
                "id",
                str
            ) if dao_id is None else dao_id,

            self._check_get_is_primitive(
                dao_data_obj["dao_name"],
                d.DAO,
                "dao_name",
                str
            ),
            self._check_get_is_primitive(
                dao_data_obj["mission_statement"],
                d.DAO,
                "mission_statement",
                str
            ),
            self._check_get_is_primitive(
                dao_data_obj["hierarchical_inheritance"],
                d.DAO,
                "hierarchical_inheritance",
                str
            )
        )
        # ... permissions
        self.print_msg(f"in DAO {dao_id}, parsing permissions ...")
        permissions_data: dict = dao_data_obj["permissions"]
        self._check_is_dict(permissions_data, dao, "permissions_data")
        self.print_msg(f" ... {len(permissions_data)} permissions ...")
        permissions_dict: dict[str, p.Permission] = {}
        for permission_id, permission_data in permissions_data.items():
            permissions_dict[permission_id] = self.parse_permission(
                diagram, dao_id, dao, permission_data
            )
        dao.permissions = permissions_dict
        # ... roles
        self.print_msg(f"in DAO {dao_id}, parsing roles ...")
        roles_data: dict = dao_data_obj["roles"]
        self._check_is_dict(roles_data, dao, "roles")
        self.print_msg(f" ... {len(roles_data)} roles ...")
        roles_dict: dict[str, r.Role] = {}
        for role_id, role_data in roles_data.items():
            roles_dict[role_id] = self.parse_role(
                diagram, dao_id, dao, role_data
            )
        dao.roles = roles_dict
        # ... committees
        self.print_msg(f"in DAO {dao_id}, parsing committees ...")
        committees_data: dict = dao_data_obj["committees"]
        self._check_is_dict(committees_data, dao, "committees")
        self.print_msg(f" ... {len(committees_data)} committees ...")
        committees_dict: dict[str, c.Committee] = {}
        for committee_id, committee_data in committees_data.items():
            committees_dict[committee_id] = self.parse_committee(
                diagram, dao_id, dao, committee_data
            )
        dao.committees = committees_dict
        # ... owner_role
        owner_role_id: str = dao_data_obj["owner_role"]
        if not isinstance(owner_role_id, str):
            raise Exception(
                f"While parsing JSON dao (id: {dao.get_id()}), the supposed owner_role id is not a string: {type(owner_role_id)}")
        if owner_role_id not in dao.roles:
            raise Exception(
                f"While parsing JSON dao (id: {dao.get_id()}), the owner_role id ({owner_role_id}) does not exists in this dao's 'roles' map")
        dao.owner_role = dao.roles[owner_role_id]
        # ... governance_areas
        self.print_msg(f"in DAO {dao_id}, parsing governance_areas ...")
        governance_areas_data: dict = dao_data_obj["governance_areas"]
        self._check_is_dict(governance_areas_data, dao, "governance_areas")
        self.print_msg(
            f" ... {len(governance_areas_data)} governance_areas ...")
        governance_areas_dict: dict[str, ga.GovernanceArea] = {}
        for governance_area_id, governance_area_data in governance_areas_data.items():
            governance_areas_dict[governance_area_id] = self.parse_governance_area(
                diagram, dao_id, dao, governance_area_data)
        dao.governance_areas = governance_areas_dict

        dao.metadata.save_user_functionalities_group_size(
            dao.roles, dao.committees)
        # ... dao_control_graph
        dao.dao_control_graph = None
        # ... conditions
        self.print_msg(f"in DAO {dao_id}, parsing conditions ...")
        conditions_list: list[str] = dao_data_obj["conditions"]
        self._check_is_list_str(conditions_list,
                                dao, "conditions")
        self.print_msg(
            f" ... {len(governance_areas_data)} conditions ...")
        dao.conditions = conditions_list
        # ... other things (dictionaries of primitive types)
        self.print_msg(f"in DAO {dao_id}, parsing other things ...")
        assignment_conditions_data: dict = dao_data_obj["assignment_conditions"]
        self._check_is_dict(assignment_conditions_data,
                            dao, "assignment_conditions")
        dao.assignment_conditions = assignment_conditions_data
        voting_conditions_data: dict = dao_data_obj["voting_conditions"]
        self._check_is_dict(voting_conditions_data, dao, "voting_conditions")
        dao.voting_conditions = voting_conditions_data
        proposal_conditions_data: dict = dao_data_obj["proposal_conditions"]
        self._check_is_dict(proposal_conditions_data,
                            dao, "proposal_conditions")
        dao.proposal_conditions = proposal_conditions_data
        decision_making_methods_data: dict = dao_data_obj["decision_making_methods"]
        self._check_is_dict(decision_making_methods_data,
                            dao, "decision_making_methods")
        dao.decision_making_methods = decision_making_methods_data
        role_and_committee_voting_right_dict_data: dict = dao_data_obj[
            "role_and_committee_voting_right_dict"]
        self._check_is_dict(role_and_committee_voting_right_dict_data,
                            dao, "role_and_committee_voting_right_dict")
        dao.role_and_committee_voting_right_dict = role_and_committee_voting_right_dict_data
        role_and_committee_proposal_right_dict_data: dict = dao_data_obj[
            "role_and_committee_proposal_right_dict"]
        self._check_is_dict(role_and_committee_proposal_right_dict_data,
                            dao, "role_and_committee_proposal_right_dict")
        dao.role_and_committee_proposal_right_dict = role_and_committee_proposal_right_dict_data
        # DONE
        self._resolve_cross_references(diagram, dao_id, dao, dao_data_obj)
        return dao

    def parse_relations_by_dao(self, data_obj: dict, daos_by_id: dict[str, d.DAO], diagram: dm.DiagramManager):
        rbd: dict[str, list[rel.Relation]] = {}
        rbd_data = data_obj["relations_by_dao"]
        self._check_is_dict(rbd_data, diagram, "rbd_data")
        expected_relation_fields = self._fields_of(rel.Relation)
        for dao_id, relations_list in rbd_data.items():
            if dao_id not in daos_by_id:
                raise Exception(f"Missing DAO (id: {dao_id})")
            index_relation = 0
            relations: list[rel.Relation] = []
            for relation in relations_list:
                self.check_fields(
                    relation, expected_relation_fields,
                    rel.Relation.__name__,
                    add_msg=f"Relation # {index_relation} of DAO (id): {dao_id}"
                )
                relations.append(
                    rel.Relation(
                        dao_id,
                        rt.RelationType[relation["relation_type"]],
                        relation["from_id"],
                        relation["content"]
                    )
                )
                index_relation += 1
            rbd[dao_id] = relations
        return rbd

    # there starts the "tree of parsing": diagram -> relations & DAOs -> committees / roles / permissions
    # Note: at each step, 1) get the fields 2) check the fields against the JSON object 3) instantiate the model
    def parse_diagram(self, data_obj) -> dm.DiagramManager:
        fields_mandatority: dict[str, bool] = self._fields_of(
            dm.DiagramManager
        )
        self.check_fields(data_obj, fields_mandatority,
                          dm.DiagramManager.__name__)
        # the parsing
        # TODO: is there a way to generalize the controlGraphGenerator ?
        diagram = dm.DiagramManager(
            # the whole class itself can act as a generator (since its constructor exactly require a DAO as a mandatory field)
            controlGraphGenerator=cgb.ControlGraphBasic
        )
        diagram.id = data_obj["id"]
        self.print_msg(f"Diagram ID: {diagram.get_id()}")
        # ... daos
        daos_by_id: dict[str, d.DAO] = {}
        index_dao = 0
        daos_by_id_data = data_obj["daoByID"]
        self._check_is_dict(daos_by_id_data, diagram, "daos_by_id_data")
        self.print_msg(
            f"Diagram daos_by_id_data len: {len(daos_by_id_data)}; and type: {type(daos_by_id_data)}")
        for dao_id, dao_data in daos_by_id_data.items():
            self._check_is_dict(dao_data, diagram,
                                f"dao (# {index_dao}, ID: {dao_id})")
            self.print_msg(f"... Parsing DAO {index_dao} with ID: {dao_id}")
            dao: d.DAO = self.parse_dao(diagram, dao_id, dao_data)
            diagram.createControlGraph(dao_id, dao=dao)
            daos_by_id[dao_id] = dao
            index_dao += 1
        diagram.daoByID = daos_by_id
        # ... relations_by_dao
        diagram.relations_by_dao = self.parse_relations_by_dao(
            data_obj, daos_by_id, diagram
        )
        # diagram.processRawInstances() # NOT NEEDED ^^
        return diagram
