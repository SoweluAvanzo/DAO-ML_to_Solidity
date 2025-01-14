import  model.base_entity as base_entity
import  model.permission as permission
import  model.committee as committee
import  model.role as role
import  model.control_graph_generic as control_graph_generic
import  model.enums.user_functionalities_group_size as user_functionalities_group_size
class DAOMetadata:
    def __init__(self):
        self.user_functionalities_group_size = None
        self.size_user_functionalities_group = None

    def save_user_functionalities_group_size(self, roles, committees):
        self.size_user_functionalities_group = len(roles) + len(committees)
        self.user_functionalities_group_size = user_functionalities_group_size.UserFunctionalitiesGroupSize.from_size(self.size_user_functionalities_group)
    
    def toJSON(self):
        return {
            "user_functionalities_group_size": self.user_functionalities_group_size,
            "size_user_functionalities_group": self.size_user_functionalities_group
        }

class DAO(base_entity.BaseEntity):
    def __init__(self, dao_id, dao_name, mission_statement, hierarchical_inheritance):
        super().__init__(dao_id)
        self.dao_name = dao_name
        self.mission_statement = mission_statement
        self.hierarchical_inheritance = hierarchical_inheritance
        self.roles: dict[str, role.Role] = {}
        self.committees: dict[str, committee.Committee] = {}
        self.permissions: dict[str, permission.Permission] = {}
        self.dao_control_graph: control_graph_generic.ControlGraphGeneric = None
        self.metadata = DAOMetadata()
        self.assignment_conditions: dict[str, str] = {} # Role
        self.voting_conditions: dict[str, str]  = {} # Committee
        self.proposal_conditions: dict[str, str]  = {} # Committee
        self.decision_making_methods: dict[str, str]  = {} # Committee
        self.conditions = []
        self.role_and_committee_voting_right_dict = {}
        self.role_and_committee_proposal_right_dict = {}
    
    def add_role(self, role):
        self.roles[role.id] = role

    def add_committee(self, committee):
        self.committees[committee.id] = committee

    def add_permission(self, permission):
        self.permissions[permission.id] = permission

    def __str__(self):
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

    def toJSON(self):
        obj = super().toJSON()
        obj["dao_name"] = self.dao_name
        obj["mission_statement"] = self.mission_statement
        obj["hierarchical_inheritance"] = self.hierarchical_inheritance
        obj["roles"] = {n: self.roles[n].toJSON() for n in self.roles}
        obj["committees"] = {n: self.committees[n].toJSON() for n in self.committees}
        obj["permissions"] = {n: self.permissions[n].toJSON() for n in self.permissions}
        obj["dao_control_graph"] = None # self.dao_control_graph -> ControlGraph
        # obj["metadata"] = self.metadata.toJSON()
        obj["assignment_conditions"] = {r: self.assignment_conditions[r] for r in self.assignment_conditions}
        obj["voting_conditions"] = {n: self.voting_conditions[n] for n in self.voting_conditions} 
        obj["proposal_conditions"] = {n: self.proposal_conditions[n] for n in self.proposal_conditions} 
        obj["decision_making_methods"] = {n: self.decision_making_methods[n] for n in self.decision_making_methods} 
        obj["conditions"] = self.conditions
        return obj
