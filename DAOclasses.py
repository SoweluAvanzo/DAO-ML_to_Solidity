
import networkx as nx
import matplotlib.pyplot as plt
#stores DAO information and metadata
class DAO:
    def __init__(self, dao_id, dao_name, mission_statement, hierarchical_inheritance):
        self.dao_id = dao_id
        self.dao_name = dao_name
        self.mission_statement = mission_statement
        self.hierarchical_inheritance = hierarchical_inheritance
        self.roles = []
        self.committees = []
        self.permissions = []
        self.dao_control_graph = nx.DiGraph()
    
    def add_role(self, role):
        self.roles.append(role)

    def add_committee(self, committee):
        self.committees.append(committee)

    def add_permission(self, permission):
        self.permissions.append(permission)

    def __str__(self):
        result = [
            "DAOs:",
            f'\tdao_id={self.dao_id}',
            f'\tdao_name={self.dao_name}',
            f'\tmission_statement={self.mission_statement}',
            f'\thierarchical_inheritance={self.hierarchical_inheritance}'
        ]
        #for dao in self.daos.values():
        #    result.append(str(dao))
        result.append("\nRoles:")
        for role in self.roles:
            result.append("\t\t" + str(role))
        result.append("\nCommittees:")
        for committee in self.committees:
            result.append("\t\t" + str(committee))
        result.append("\nPermissions:")
        for permission in self.permissions:
            result.append("\t\t" + str(permission))
        return "\n".join(result)


#stores role information with control relations and associated permissions
class Role:
    def __init__(self, role_id, role_name, role_assignment_method, agent_type):
        self.role_id = role_id
        self.role_name = role_name
        self.role_assignment_method = role_assignment_method
        self.agent_type = agent_type
        self.permissions = []
        self.controllers = []
        self.aggregated =  []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def add_controller(self, controller_id):
        self.controllers.append(controller_id)
    
    def add_aggregated(self, aggregated_id):
        self.aggregated.append(aggregated_id)

    def __str__(self):
        return f'Role(role_id={self.role_id}, role_name={self.role_name}, role_assignment_method={self.role_assignment_method}, agent_type={self.agent_type}, permissions={self.permissions}, controllers={self.controllers})'

#stores committee information with control relations and permissions
class Committee:
    def __init__(self, committee_id, committee_description, n_agent_min, n_agent_max, appointment_method):
        self.committee_id = committee_id
        self.committee_description = committee_description
        self.n_agent_min = n_agent_min
        self.n_agent_max = n_agent_max
        self.appointment_method = appointment_method
        self.permissions = []
        self.controllers = []
        self.aggregated =  []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def add_controller(self, controller_id):
        self.controllers.append(controller_id)
        
    def add_aggregated(self, aggregated_id):
        self.aggregated.append(aggregated_id)

    def __str__(self):
        return f'Committee(committee_id={self.committee_id}, committee_description={self.committee_description}, n_agent_min={self.n_agent_min}, n_agent_max={self.n_agent_max}, appointment_method={self.appointment_method}, permissions={self.permissions}, controllers={self.controllers})'

#stores permission metadata
class Permission:
    def __init__(self, permission_id, allowed_action, permission_type):
        self.permission_id = permission_id
        self.allowed_action = allowed_action
        self.permission_type = permission_type

    def __str__(self):
        return f'Permission(permission_id={self.permission_id}, allowed_action={self.allowed_action}, permission_type={self.permission_type})'
