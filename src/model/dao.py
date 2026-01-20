import src.model.base_entity as base_entity_module
import src.model.permission as permission_module
import src.model.committee as committee_module
import src.model.role as role_module
import src.model.governance_area as governance_area_module
import src.control_graph.control_graph_generic as control_graph_generic_module
import src.model.enums.user_functionalities_group_size as ufgs


class DAOMetadata:
    def __init__(self):
        self.user_functionalities_group_size = None
        self.size_user_functionalities_group = None

    def save_user_functionalities_group_size(self, roles, committees):
        self.size_user_functionalities_group = len(roles) + len(committees)
        self.user_functionalities_group_size = ufgs.UserFunctionalitiesGroupSize.from_size(
            self.size_user_functionalities_group)

    def toJSON(self):
        return {
            "user_functionalities_group_size": self.user_functionalities_group_size.name,
            "size_user_functionalities_group": self.size_user_functionalities_group
        }

    def __repr__(self):
        return self.toJSON()


class DAO(base_entity_module.BaseEntity):
    def __init__(self, dao_id, dao_name, mission_statement, hierarchical_inheritance):
        super().__init__(dao_id)
        self.dao_name = dao_name
        self.mission_statement = mission_statement
        self.hierarchical_inheritance = hierarchical_inheritance
        self.owner_role: role_module.Role = None
        self.roles: dict[str, role_module.Role] = {}
        self.committees: dict[str, committee_module.Committee] = {}
        self.governance_areas: dict[str,
                                    governance_area_module.GovernanceArea] = {}
        self.permissions: dict[str, permission_module.Permission] = {}
        self.dao_control_graph: control_graph_generic_module.ControlGraphGeneric = None
        self.metadata = DAOMetadata()
        self.conditions: list[str] = []
        self.assignment_conditions: dict[str, str] = {}  # Role
        self.voting_conditions: dict[str, str] = {}  # Committee
        self.proposal_conditions: dict[str, str] = {}  # Committee
        self.decision_making_methods: dict[str, str] = {}  # Committee
        # key: role_or_committee__ID; value: committee__id
        self.role_and_committee_voting_right_dict: dict[str, str] = {}
        # key: role_or_committee__ID; value: committee__id
        self.role_and_committee_proposal_right_dict: dict[str, str] = {}

    def get_name(self) -> str:
        return self.dao_name

    def add_role(self, role: role_module.Role):
        self.roles[role.get_id()] = role

    def add_committee(self, committee: committee_module.Committee):
        self.committees[committee.get_id()] = committee

    def add_permission(self, permission: permission_module.Permission):
        self.permissions[permission.get_id()] = permission

    def add_governance_area(self, governance_area: governance_area_module.GovernanceArea):
        self.governance_areas[governance_area.get_id()] = governance_area

    def toJSON(self):
        obj = super().toJSON()
        obj["dao_name"] = self.dao_name
        obj["mission_statement"] = self.mission_statement
        obj["hierarchical_inheritance"] = self.hierarchical_inheritance
        obj["owner_role"] = "null" if self.owner_role is None else self.owner_role.get_id()
        obj["roles"] = {
            n.get_id(): n.toJSON()
            for n in self.roles.values()
        }
        obj["committees"] = {
            n.get_id(): n.toJSON()
            for n in self.committees.values()
        }
        obj["permissions"] = {
            n.get_id(): n.toJSON()
            for n in self.permissions.values()
        }
        obj["governance_areas"] = {
            n.get_id(): n.toJSON()
            for n in self.governance_areas.values()
        }
        obj["dao_control_graph"] = f"DAO Graph, but not serializable, of type: {self.dao_control_graph.__class__.__name__ if self.dao_control_graph is not None else 'NONE'}"
        obj["metadata"] = self.metadata.toJSON()
        obj["assignment_conditions"] = {
            role_id: role_assignment_method
            for role_id, role_assignment_method
            in self.assignment_conditions.items()
        }
        obj["voting_conditions"] = {
            committee_id: voting_condition
            for committee_id, voting_condition
            in self.voting_conditions.items()
        }

        obj["proposal_conditions"] = {
            committee_id: proposal_condition
            for committee_id, proposal_condition
            in self.proposal_conditions.items()
        }

        obj["decision_making_methods"] = {
            committee_id: dmm
            for committee_id, dmm
            in self.decision_making_methods.items()
        }
        obj["conditions"] = self.conditions  # list[str]
        obj["role_and_committee_voting_right_dict"] = self.role_and_committee_voting_right_dict
        obj["role_and_committee_proposal_right_dict"] = self.role_and_committee_proposal_right_dict
        return obj

    def __str__(self):
        """ 
        parts = [
            f'\tdao_name={self.dao_name}',
            f'\tmission_statement={self.mission_statement}',
            f'\thierarchical_inheritance={self.hierarchical_inheritance}'
        ]
        #for dao in self.daos.values():
        #    pasrts.append(str(dao))
        parts.append("\nRoles:")
        for role in self.roles.values():
            parts.append("\n\t" + str(role))
        parts.append("\nCommittees:")
        for committee in self.committees.values():
            parts.append("\n\t" + str(committee))
        parts.append("\nPermissions:")
        for permission in self.permissions.values():
            parts.append("\n\t" + str(permission))
        additional_parts = "".join(parts)
        parts = None
        return super().__str__(additional_parts)
        """
        import json
        return json.dumps(self.toJSON(), indent="\t")
