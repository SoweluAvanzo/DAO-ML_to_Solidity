
import networkx as nx
#stores DAO information and metadata
from enum import Enum

class RelationType(Enum):
    ASSOCIATION = 1
    CONTROL = 2
    AGGREGATION = 3
    FEDERATION = 4

class BaseEntity:
    def __init__(self, id):
        self.id = id
    def get_id(self):
        return self.id

#stores permission metadata
class Permission: #(BaseEntity):
    def __init__(self, permission_id, allowed_action, permission_type, ref_gov_area = None, voting_right = False, proposal_right = False):
        #super.__init__(self, permission_id)
        self.permission_id = permission_id
        self.allowed_action = allowed_action
        self.permission_type = permission_type
        self.ref_gov_area = ref_gov_area
        self.voting_right = voting_right
        self.proposal_right = proposal_right

    def __str__(self):
        return f'Permission(permission_id={self.permission_id}, allowed_action={self.allowed_action}, permission_type={self.permission_type}, ref_gov_area={self.ref_gov_area})'

    def toJSON(self):
        return {
            "permission_id": self.permission_id,
            "allowed_action": self.allowed_action,
            "permission_type": self.permission_type,
            "ref_gov_area": self.ref_gov_area,
            "voting_right": self.voting_right,
            "proposal_right": self.proposal_right,
        }


#stores role information with control relations and associated permissions
class Role:
    def __init__(self, role_id, role_name, role_assignment_method, n_agent_min, n_agent_max, agent_type):
        self.role_id = role_id
        self.role_name = role_name
        self.role_assignment_method = role_assignment_method
        self.n_agent_min = n_agent_min
        self.n_agent_max = n_agent_max
        self.agent_type = agent_type
    
        self.permissions: list[Permission] = []
        self.controllers:list[str] = [] # just the ID
        self.aggregated:list[Role|Committee] =  []
        self.federated_committees:list[Committee] = []
        
    def get_id(self):
        return self.role_id

    def add_permission(self, permission: Permission):
        #print(f'Adding permission {str(permission)} to role {self.role_id}')
        self.permissions.append(permission)

    def add_controller(self, controller_id:str):
        self.controllers.append(controller_id)
    
    def add_aggregated(self, aggregated):
        self.aggregated.append(aggregated)

    def add_committee_membership(self, target_committee:any):
        self.federated_committees.append(target_committee)

    def __str__(self):
        parts = [f'Role(role_id={self.role_id}, role_name={self.role_name}, role_assignment_method={self.role_assignment_method}, n_agent_min={self.n_agent_min}, n_agent_max={self.n_agent_max} agent_type={self.agent_type}']
        is_not_first = False
        parts.append(f", permissions<{len(self.permissions)}>=[")
        for p in self.permissions:
            parts.append(p.permission_id)
            if is_not_first:
                parts.append(", ")
            else:
                is_not_first = True
        parts.append("]")
        is_not_first = False
        parts.append(f", controllers<{len(self.controllers)}>=[")
        for c in self.controllers:
            if is_not_first:
                parts.append(", ")
            else:
                is_not_first = True
            parts.append(str(c))
        parts.append("]")
        is_not_first = False
        parts.append(f", aggregated<{len(self.aggregated)}>=[")
        for a in self.aggregated:
            if is_not_first:
                parts.append(", ")
            else:
                is_not_first = True
            parts.append(str(a))
        parts.append("]")
        return "".join(parts)

    def toJSON(self):
        return { \
            "role_id":self.role_id, \
            "role_name":self.role_name, \
            "role_assignment_method":self.role_assignment_method, \
            "n_agent_min":self.n_agent_min, \
            "n_agent_max":self.n_agent_max, \
            "agent_type":self.agent_type, \
            "permissions":[ p.permission_id for p in self.permissions], \
            "controllers":self.controllers, \
            "aggregated": [ agg.get_id() for agg in self.aggregated ], \
            "federated_committees":[c.committee_id for c in self.federated_committees] \
        }

#stores committee information with control relations and permissions
class Committee:
    #removed n_agent_min, n_agent_max
    def __init__(self, committee_id, committee_description, voting_condition, proposal_condition, decision_making_method):
        self.committee_id = committee_id
        self.committee_description = committee_description
        # self.n_agent_min = n_agent_min
        # self.n_agent_max = n_agent_max
        self.voting_condition = voting_condition
        self.proposal_condition = proposal_condition
        self.decision_making_method = decision_making_method

        self.permissions:list[Permission] = []
        self.controllers:list[str] = []
        self.aggregated:list[Role|Committee] =  []
        self.member_entities:list[Committee] = []
        self.federated_committees:list[Committee|Role] = []

    def get_id(self):
        return self.committee_id

    def add_permission(self, permission):
        #print(f'Adding permission {str(permission)} to committee {self.committee_id}')
        self.permissions.append(permission)

    def add_controller(self, controller_id:str):
        self.controllers.append(controller_id)
        
    def add_aggregated(self, aggregated):
        self.aggregated.append(aggregated)

    def add_committee_membership(self, target_committee):
        self.federated_committees.append(target_committee)
        #print(f'Adding committee {target_committee.get_id()} to committee {self.committee_id}')
        #storing the relation that indicates that the given committee federates into a target committee
        

    def add_member_entity(self, entity:any):
        self.member_entities.append(entity)
        #print(f'Adding member entity {entity.get_id()} to committee {self.committee_id}')
    

    def __str__(self):
        parts=[f'Committee(committee_id={self.committee_id}, committee_description={self.committee_description}, voting_condition={self.voting_condition}, proposal_condition={self.proposal_condition}, decision_making_method={self.decision_making_method}']
        is_not_first = False
        parts.append(", permissions=[")
        for p in self.permissions:
            parts.append(p.permission_id)
            if is_not_first:
                parts.append(", ")
            else:
                is_not_first = True
        parts.append("]")
        is_not_first = False
        parts.append(", controllers=[")
        for c in self.controllers:
            parts.append(c)
            if is_not_first:
                parts.append(", ")
            else:
                is_not_first = True
        parts.append("]")
        is_not_first = False
        parts.append(", aggregated=[")
        for a in self.aggregated:
            parts.append(a)
            if is_not_first:
                parts.append(", ")
            else:
                is_not_first = True
        parts.append("]")
        return "".join(parts)

    def toJSON(self):
        return { \
            "committee_id":self.committee_id, \
            "committee_description":self.committee_description, \
            "voting_condition":self.voting_condition, \
            "proposal_condition":self.proposal_condition, \
            "decision_making_method":self.decision_making_method, \
            "permissions":[ p.permission_id for p in self.permissions], \
            "controllers":self.controllers, \
            "aggregated": [agg.get_id() for agg in self.aggregated], \
            "member_entities":[c.get_id() for c in self.member_entities], \
            "federated_committees":[c.get_id() for c in self.federated_committees] \
        }
        
#graph structures

class GraphType(Enum):
    LIST = 0
    DAG = 1
    GRAPH = 2

class ControlGraph:
    def __init__(self, dao):
        self.dao: DAO = dao
        self.control_graph: nx.DiGraph = None
        self.graph_type: GraphType = None #is calculated before the transitive closure is applied in case of hierarchical inheritance
        self.is_cyclic = False #hypotesis
        self.create_control_graph()
    

    def create_control_graph(self):
        self.add_new_default_graph()
        for role in self.dao.roles.values():
            #self.control_graph.add_node(role.role_id, color="blue", size=10)
            for controller in role.controllers:
                self.control_graph.add_edge(role.role_id,controller)
        for committee in self.dao.committees.values():
            #self.control_graph.add_node(committee.committee_id, color="red", size=25)
            for controller in committee.controllers:
                self.control_graph.add_edge(committee.committee_id,controller)
            #print(f'Control graph generated for DAO {self.dao.dao_id} \nPrinting edges and nodes \n')
            #assignment of control graph to DAO object
            # print edges
            # for node in self.control_graph.nodes:
            #     print(f'Node: {node} \n')
            # for edge in self.control_graph.edges:
            #     print(f'Edge: {edge} \n')
            # print("now simple cycles!")
            #print paths
        #     for loop in nx.simple_cycles(self.control_graph):
        #         print(f'Loop: {loop} \n') 
        # print("now recalculate properties")
        self.recalculate_graph_properties()
        # print(f'Control graph updated and calculated properties. The graph type is {self.graph_type}, and it is {self.is_cyclic} that the graph is cyclic \nPrinting edges and nodes \n')

    def add_new_default_graph(self):
        self.control_graph = nx.DiGraph()

    def recalculate_graph_properties(self):
        self.graph_type = self.get_graph_type()
        if self.dao.hierarchical_inheritance == 1:
            self.control_graph =  nx.transitive_closure(self.control_graph)
        

    def get_graph_type(self):
        if nx.is_directed_acyclic_graph(self.control_graph):
            if self.is_list():
                print("the control graph is a list and doesn't contain cycles")
                return GraphType.LIST #the graph is a list and doesn't contain cycles
            else:
                return GraphType.DAG #the graph is a DAG, but not a list
        else:
            self.is_cyclic = True
            return GraphType.GRAPH #the graph contains cycles
        
    def is_list(self):
        return all(self.control_graph.out_degree(n) <= 1 for n in self.control_graph.nodes)
    
    
class UserFunctionalitiesGroupSize(Enum):
    SMALL = (32,5)
    MEDIUM = (64,6)
    LARGE = (128,7)
    EXTRA_LARGE = (256,8)
    def from_size(size):
        if size <= 32:
            return UserFunctionalitiesGroupSize.SMALL
        elif size <= 64:
            return UserFunctionalitiesGroupSize.MEDIUM
        elif size <= 128:
            return UserFunctionalitiesGroupSize.LARGE
        elif size <= 256:
            return UserFunctionalitiesGroupSize.EXTRA_LARGE
        else:
            return None
        
class DAOMetadata:
    def __init__(self):
        self.user_functionalities_group_size = None
        self.size_user_functionalities_group = None

    def save_user_functionalities_group_size(self, roles, committees):
        self.size_user_functionalities_group = len(roles) + len(committees)
        self.user_functionalities_group_size = UserFunctionalitiesGroupSize.from_size(self.size_user_functionalities_group)
    
    def toJSON(self):
        return {
            "user_functionalities_group_size": self.user_functionalities_group_size,
            "size_user_functionalities_group": self.size_user_functionalities_group
        }

class DAO:
    def __init__(self, dao_id, dao_name, mission_statement, hierarchical_inheritance):
        self.dao_id = dao_id
        self.dao_name = dao_name
        self.mission_statement = mission_statement
        self.hierarchical_inheritance = hierarchical_inheritance
        self.owner_role: Role = None
        self.roles: dict[str, Role] = {}
        self.committees: dict[str, Committee] = {}
        self.permissions: dict[str, Permission] = {}
        self.dao_control_graph: ControlGraph
        self.metadata = DAOMetadata()
        self.assignment_conditions: dict[str, str] = {} # Role
        self.voting_conditions: dict[str, str]  = {} # Committee
        self.proposal_conditions: dict[str, str]  = {} # Committee
        self.decision_making_methods: dict[str, str]  = {} # Committee
        self.conditions = []
        self.role_and_committee_voting_right_dict = {}
        self.role_and_committee_proposal_right_dict = {}
        

    
    def add_role(self, role):
        self.roles[role.role_id] = role

    def add_committee(self, committee):
        self.committees[committee.committee_id] = committee

    def add_permission(self, permission):
        self.permissions[permission.permission_id] = permission

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
        for role in self.roles.values():
            result.append("\t\t" + str(role))
        result.append("\nCommittees:")
        for committee in self.committees:
            result.append("\t\t" + str(committee))
        result.append("\nPermissions:")
        for permission in self.permissions:
            result.append("\t\t" + str(permission))
        return "\n".join(result)

    def toJSON(self):
        dao_json = {
            "dao_id": self.dao_id,
            "dao_name": self.dao_name,
            "mission_statement": self.mission_statement,
            "hierarchical_inheritance": self.hierarchical_inheritance,
            "roles": {n: self.roles[n].toJSON() for n in self.roles},
            "committees": {n: self.committees[n].toJSON() for n in self.committees},
            "permissions": {n: self.permissions[n].toJSON() for n in self.permissions},
            "dao_control_graph": None, # self.dao_control_graph -> ControlGraph
            # "metadata": self.metadata.toJSON(),
            "assignment_conditions": {r: self.assignment_conditions[r] for r in self.assignment_conditions},
            "voting_conditions": {n: self.voting_conditions[n] for n in self.voting_conditions} ,
            "proposal_conditions": {n: self.proposal_conditions[n] for n in self.proposal_conditions} ,
            "decision_making_methods": {n: self.decision_making_methods[n] for n in self.decision_making_methods} ,
            "conditions": self.conditions
        }
        return dao_json


