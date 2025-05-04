# import DAOclasses as dc
from collections import defaultdict
import networkx as nx

import model.dao as ddao
import model.role as role
import model.committee as committee
import model.permission as permission
import model.enums.relation_type as rt
# import model.control_graph_generic as control_graph_generic
import control_graph.control_graph_base as control_graph_impl

class DiagramManager2:
    def __init__(self):
        self.rowDataOnly = True
        self.daoByID: map[str, ddao.DAO] = {}
        self.relations_by_dao: map[str, list[tuple[rt.RelationType, str, str]]] = {}

    def reset(self):
        self.daoByID = {}
        self.relations_by_dao = {}

    '''
    def addDiagram(self, input, cleanPrevious = True):
        if cleanPrevious:
            self.reset()
        # attualmente, "input" sara' il XML-visitor, in futuro sara'
        # un wrapper che itera e fornisce le varie strutture
    '''
    def get_dao_by(self, daoOrID: str|ddao.DAO) -> ddao.DAO:
        dao = None
        if isinstance(daoOrID, ddao.DAO):
            dao = daoOrID
        elif isinstance(daoOrID, str):
            dao = self.daoByID[daoOrID]
        else:
            raise Exception("Unknown type of dao / dao's ID : " + daoOrID)
        return dao


    def addDao(self, dao):
        self.daoByID[dao.id] = dao
        self.relations_by_dao[dao.id] = []
    
    def addRole(self, daoOrID: str|ddao.DAO, role: role.Role):
        dao = self.get_dao_by(daoOrID)
        dao.add_role(role)

    def addCommittee(self, daoOrID: str|ddao.DAO, committee: committee.Committee):
        dao = self.get_dao_by(daoOrID)
        dao.add_committee(committee)

    def addPermission(self, daoOrID: str|ddao.DAO, permission: permission.Permission ):
        dao = self.get_dao_by(daoOrID)
        dao.add_permission(permission)
        

    def addRelation(self, daoOrID: str|ddao.DAO, relationType: rt.RelationType, fromID: str, content:str ):
        dao = self.get_dao_by(daoOrID)
        id = dao.id
        self.relations_by_dao[id].append( (relationType, fromID, content) )
    #
    #
    #
    def createControlGraph(self):
        # crea il control graph, tramite una istanza di una classe __che dovremmo ancora definire__
        for dao in self.daoByID.values():
            if not isinstance(dao, ddao.DAO):
                raise Exception("given dao is not an instance of DAO")
            id = dao.id
            cg_wrapper = control_graph_impl.ControlGraphBase(dao)
            print(f'Control Graph {cg_wrapper} created for DAO: {id} \n')
            dao.dao_control_graph = cg_wrapper         
        # for role in dao.roles.values():
        #         for controller in role.controllers:
        #             dao.dao_control_graph.add_edge(role.id,controller)
        #     for committee in dao.committees.values():
        #         for controller in committee.controllers:
        #             dao.dao_control_graph.add_edge(committee.id,controller)
        #     print(f'Control graph generated for DAO {id} \nPrinting edges and nodes \n')
        #     #assignment of control graph to DAO object
        #     # print edges
        #     for node in dao.dao_control_graph.nodes:
        #         print(f'Node: {node} \n')
        #     for edge in dao.dao_control_graph.edges:
        #         print(f'Edge: {edge} \n')
        #     #print paths
        #     for loop in nx.simple_cycles(dao.dao_control_graph):
        #         print(f'Loop: {loop} \n') 
        
    def get_aggregated_permissions(self, role_or_committee):
        # if not role_or_committee.aggregated:
        #     return
        for aggregated in role_or_committee.aggregated:
            self.get_aggregated_permissions(aggregated)
            #the aggregator inherits permissions from the aggregated
            for permission in aggregated.permissions:
                if permission not in role_or_committee.permissions:
                    source_id = role_or_committee.id if isinstance(role_or_committee, role.Role) else role_or_committee.id
                    target_id = aggregated.id if isinstance(aggregated, role.Role) else aggregated.id
                    print(f"added Permission:  {permission.id} to {source_id}, which was aggregated from {target_id} \n")
                    role_or_committee.add_permission(permission)   
            #the aggregator also inherits controllers from the aggregated
            print(f'Aggregated: {aggregated} has list of controllers of controllers: {aggregated.controllers}\n')
            for controller in aggregated.controllers:
                print(f'Controller: {controller} in list of controllers of {aggregated}, that is: {aggregated.controllers}\n')
                if controller not in role_or_committee.controllers:
                    role_or_committee.add_controller(controller)
                    #print(f"added Controller:  {controller} to {role_or_committee} from aggregator {aggregated}\n")
                # else:
                #     print(f"Controller:  {controller} already in list of controllers of {role_or_committee} \n")

    def processRawInstances(self):
        if not self.rowDataOnly:
            return
        # TODO: copia-e-incolla da "parse_xml.py", dal metodo "visitDao()", tutti quei cicli for
        # che processano le varie istanze (di Role, Committee, etc)

        # Assign permissions to roles and committees in DAO based on association relations
        for dao in self.daoByID.values():
            id = dao.id
            for relation in self.relations_by_dao[id]:
                print(f'PROCESS RAW INSTANCES: Relation: {relation} \n')
                fromID = relation[1]
                content = relation[2]
                if relation[0] == rt.RelationType.CONTROL:
                    the_controller_ID = content
                    controlled_ID= fromID

                    print(f'Control relation found: {the_controller_ID} -> {controlled_ID} \n')
                    if controlled_ID in dao.roles:
                        role = dao.roles[controlled_ID]
                        print(f'Role found: {role.id} , controlled by {the_controller_ID} \n')
                        role.add_controller(the_controller_ID)
                    elif controlled_ID in dao.committees:
                        committee = dao.committees[controlled_ID]
                        print(f'Committee found: {committee.id} , controlled by {the_controller_ID} \n')
                        committee.add_controller(the_controller_ID) 
                    else:
                        print(f"ERROR: the controller __{the_controller_ID}__ should control __{controlled_ID}__, but this last one has not been found")
                elif relation[0] == rt.RelationType.ASSOCIATION:
                    if fromID in dao.roles:
                        role = dao.roles[fromID]
                        if content in dao.permissions:
                            role.add_permission(dao.permissions[content])
                            print(f'Permission {content} assigned to Role {fromID} \n')
                    elif fromID in dao.committees:
                        committee = dao.committees[fromID]
                        if content in dao.permissions:
                            committee.add_permission(dao.permissions[content])
                            print(f'Permission {content} assigned to Committee {fromID}\n')
                elif relation[0] == rt.RelationType.AGGREGATION:
                    print(f'Aggregation relation found: {fromID} -> {content} \n')
                    if fromID in dao.roles:
                        role = dao.roles[fromID]
                        if content in dao.roles:
                        
                            role.add_aggregated(dao.roles[content])
                        elif content in dao.committees:
                            role.add_aggregated(dao.committees[content])
                            print(f'Role {fromID} aggregates into: {content} \n')
                    elif fromID in dao.committees:
                        committee = dao.committees[fromID]
                        if content in dao.committees:
                            committee.add_aggregated(dao.committees[content])
                        elif content in dao.roles:
                            committee.add_aggregated(dao.roles[content])
                            print(f' Committee "{fromID}" aggregates into  {content}\n')
                elif relation[0] == rt.RelationType.FEDERATION:
                    if fromID in dao.roles:
                        role = dao.roles[fromID]
                        if content in dao.committees:
                            #the source role is part of the target committee
                            role.add_committee_membership(dao.committees[content])
                            #the target committee has the source role as a member
                            dao.committees[content].add_member_entity(role)
                            print(f'Role {fromID} federates into: {content} \n')
                        else:
                            print(f'ERROR: wrong federation type: Role {fromID} -> {content} \n')
                    elif fromID in dao.committees:
                        committee = dao.committees[fromID]
                        if content in dao.committees:
                            #the source committee is part of the target committee
                            committee.add_committee_membership(dao.committees[content])
                            #the target committee has the source committee as a member
                            dao.committees[content].add_member_entity(committee)
                            print(f'Committee {fromID} federates into: {content} \n')
                        else:
                            print(f'ERROR: wrong federation type: Committee {fromID} -> {content} \n')
            dao.metadata.save_user_functionalities_group_size(dao.roles, dao.committees)
            # Assign voting and proposal permissions to committees
            for committee in dao.committees.values():
                # Assign voting and proposal permissions to committees
                voting_permission = self.create_governance_permission("Voting", committee)
                proposal_permission = self.create_governance_permission("Proposal", committee)
                dao.add_permission(voting_permission)
                print(f'Voting Permission {voting_permission.id} created for Committee {committee.id} \n')
                dao.add_permission(proposal_permission)
                print(f'Proposal Permission {proposal_permission.id} created for Committee {committee.id} \n')
                for role_or_committee in committee.member_entities:
                    print(f'Role or Committee: {role_or_committee.get_id()} is member of Committee {committee.get_id()}\n')
                    if isinstance(role_or_committee, role.Role or isinstance(role_or_committee, committee.Committee)):
                        if voting_permission not in role_or_committee.permissions:
                            role_or_committee.add_permission(voting_permission)
                            #adding to the dictionary of voting rights to access it in simple translator
                            dao.role_and_committee_voting_right_dict[role_or_committee.get_id()] = committee.get_id()
                            print(f'Governance Permission {voting_permission.id} assigned to {role_or_committee.id} \n')
                        if proposal_permission not in role_or_committee.permissions:
                            role_or_committee.add_permission(proposal_permission)
                            dao.role_and_committee_proposal_right_dict[role_or_committee.get_id()] = committee.get_id()
                            print(f'Governance Permission {proposal_permission.id} assigned to {role_or_committee.id} \n')
            # Assign aggregated permissions to roles and committees in DAO based on aggregation relations
            for role in dao.roles.values():
                self.get_aggregated_permissions(role)
            for committee in dao.committees.values():
                self.get_aggregated_permissions(committee)
            #generate conditions for the DAO
            self.generate_conditions(dao)
            #generate owner role
            self.generateOwnerRole(dao)
        print(f' in process raw instances DAO: {id} is processed. \n DAO Conent: {dao} \n')            
        self.createControlGraph()
        
    def generateOwnerRole(self, dao):
        #create owner role
        owner_role = role.Role(role_id = dao.id + "Owner", role_name= dao.id + " Owner", role_assignment_method = "Non Assignable", n_agent_min =None, n_agent_max=None, agent_type=None)
        for permission in dao.permissions.values():
            owner_role.add_permission(permission)
        dao.add_role(owner_role)

            # Assign controllers to roles and committees in DAO based on control relations
            # for role in self.roles.values():
            #     for controller in self.control_relations[role.id]:
            #         role.add_controller(controller)
            #         print(f'Controller {controller} assigned to Role {role.id} \n')
            # for committee in self.committees.values():
            #     for controller in self.control_relations[committee.id]:
            #         committee.add_controller(controller)
            #         print(f'Controller {controller} assigned to Committee {committee.id} \n')

            # # Assign aggregated roles and committees to roles and committees in DAO based on aggregation relations
            # for role in self.roles.values():
            #     for aggregated in self.aggregations[role.id]:
            #         role.add_aggregated(aggregated)
            #         print(f'Role {role.id} aggregates into: {aggregated} \n')
            # for committee in self.committees.values():
            #     for aggregated in self.aggregations[committee.id]:
            #         committee.add_aggregated(aggregated)
            #         print(f' Committee "{role.id}" aggregates into  {aggregated}\n')
            
            # Assign controllers to roles and committees in DAO based on control relations
            # for role in self.roles.values():
            #     for controller_id in self.control_relations[role.id]:
            #         if controller_id in self.roles:
            #             role.add_controller(self.roles[controller_id])
            #             print(f'Controller {controller_id} assigned to Role {role.id} \n')
            #         elif controller_id in self.committees:
            #             role.add_controller(self.committees[controller_id])
            #             print(f'Controller {controller_id} assigned to Role {role.id} \n')
            # for committee in self.committees.values():
            #     for controller_id in self.control_relations[committee.id]:
            #         if controller_id in self.roles:
            #             committee.add_controller(self.roles[controller_id])
            #             print(f'Controller {controller_id} assigned to Committee {committee.id} \n')
            #         elif controller_id in self.committees:
            #             committee.add_controller(self.committees[controller_id])
            #             print(f'Controller {controller_id} assigned to Committee {committee.id} \n')

            #assignemnt of roles and committees defined to the DAO

            
            #control graph generation based on control relations stored
           
            #code generation
            #translator = SolidityTranslator(self.daos[id])
            #translator.save_to_file()

        # alla fine, ...

    def create_governance_permission(self, type, committee):
        permission_id = committee.id + type +"Right"
        allowed_action = committee.committee_description + " " + type + " Right"
        if type == "Voting":
            permission = permission.Permission(permission_id=permission_id, allowed_action= allowed_action, permission_type ="strategic", ref_gov_area = None, voting_right = True, proposal_right = False)
            print(f'Proposal Permission {permission_id} created for Committee {committee.id} \n')

        elif type == "Proposal":
            permission = permission.Permission(permission_id=permission_id, allowed_action= allowed_action, permission_type ="strategic", ref_gov_area = None, voting_right = False, proposal_right = True)
            print(f'Proposal Permission {permission_id} created for Committee {committee.id} \n')
        return permission
    
    def generate_conditions(self, dao: ddao.DAO):
        #storing both the list of the conditions and the respective relations with the roles and committees (how conditions are used in the DAO)
        conditions = []
        for role in dao.roles.values():
            if role.role_assignment_method != None:
                dao.assignment_conditions[role.id]= role.role_assignment_method
                if role.role_assignment_method not in conditions:
                    conditions.append(role.role_assignment_method)

        for committee in dao.committees.values():
            if committee.voting_condition != None:
                dao.voting_conditions[committee.id]= committee.voting_condition
                if committee.voting_condition not in conditions:
                    conditions.append(committee.voting_condition)
            if committee.voting_condition != None:
                dao.proposal_conditions[committee.id]= committee.proposal_condition
                if committee.proposal_condition not in conditions:
                    conditions.append(committee.proposal_condition)
        dao.conditions = conditions
        print(f'Conditions generated for DAO {dao.id} : {conditions} \n')
        
       


    def __str__(self):
        result = ["DAOs:"]
        for dao in self.daoByID.values():
            result.append(str(dao))
            result.append("\nRelations:")
            for role in self.relations_by_dao[dao.id]:
                result.append(str(role))

        return "\n".join(result)
    