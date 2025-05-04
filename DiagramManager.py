import DAOclasses as dc
from collections import defaultdict
import networkx as nx
import utils as u

class DiagramManager:
    def __init__(self):
        self.rowDataOnly = True
        self.daoByID: map[str, dc.DAO] = {}
        self.relations_by_dao: map[str, list[tuple[dc.RelationType, str, str]]] = {}

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
    def get_dao_by(self, daoOrID):
        dao = None
        if isinstance(daoOrID, dc.DAO):
            dao = daoOrID
        elif isinstance(daoOrID, str):
            dao = self.daoByID[daoOrID]
        else:
            raise Exception("Unknown type of dao / dao's ID : " + daoOrID)
        return dao


    def addDao(self, dao):
        self.daoByID[dao.dao_id] = dao
        dao_id = dao.dao_id
        self.relations_by_dao[dao_id] = []
    
    def addRole(self, daoOrID, role: dc.Role):
        dao = self.get_dao_by(daoOrID)
        dao.add_role(role)

    def addCommittee(self, daoOrID, committee: dc.Committee):
        dao = self.get_dao_by(daoOrID)
        dao.add_committee(committee)

    def addPermission(self, daoOrID, permission: dc.Permission ):
        dao = self.get_dao_by(daoOrID)
        dao.add_permission(permission)
        

    def addRelation(self, daoOrID, relationType: dc.RelationType, fromID: str, content:str ):
        dao = self.get_dao_by(daoOrID)
        dao_id = dao.dao_id
        self.relations_by_dao[dao_id].append( (relationType, fromID, content) )
    #
    #
    #
    def createControlGraph(self):
        for dao in self.daoByID.values():
            cg_wrapper = dc.ControlGraph(dao)
            dao.dao_control_graph = cg_wrapper         
       
        
    def get_aggregated_permissions(self, role_or_committee):

        for aggregated in role_or_committee.aggregated:
            self.get_aggregated_permissions(aggregated)
            #the aggregator inherits permissions from the aggregated
            for permission in aggregated.permissions:
                if permission not in role_or_committee.permissions:
                    source_id = role_or_committee.role_id if isinstance(role_or_committee, dc.Role) else role_or_committee.committee_id
                    target_id = aggregated.role_id if isinstance(aggregated, dc.Role) else aggregated.committee_id
                    role_or_committee.add_permission(permission)   
            #the aggregator also inherits controllers from the aggregated
            for controller in aggregated.controllers:
                if controller not in role_or_committee.controllers:
                    role_or_committee.add_controller(controller)

    def processRawInstances(self):
        if not self.rowDataOnly:
            return
        # TODO: copia-e-incolla da "parse_xml.py", dal metodo "visitDao()", tutti quei cicli for
        # che processano le varie istanze (di Role, Committee, etc)

        # Assign permissions to roles and committees in DAO based on association relations
        for dao in self.daoByID.values():
            dao_id = dao.dao_id
            for relation in self.relations_by_dao[dao_id]:
                fromID = relation[1]
                content = relation[2]
                if relation[0] == dc.RelationType.CONTROL:
                    the_controller_ID = content
                    controlled_ID= fromID

                    if controlled_ID in dao.roles:
                        role = dao.roles[controlled_ID]
                        role.add_controller(the_controller_ID)
                    elif controlled_ID in dao.committees:
                        committee = dao.committees[controlled_ID]
                        committee.add_controller(the_controller_ID) 
                    else:
                        print(f"ERROR: the controller __{the_controller_ID}__ should control __{controlled_ID}__, but this last one has not been found")
                elif relation[0] == dc.RelationType.ASSOCIATION:
                    if fromID in dao.roles:
                        role = dao.roles[fromID]
                        if content in dao.permissions:
                            role.add_permission(dao.permissions[content])
                    elif fromID in dao.committees:
                        committee = dao.committees[fromID]
                        if content in dao.permissions:
                            committee.add_permission(dao.permissions[content])
                elif relation[0] == dc.RelationType.AGGREGATION:
                    if fromID in dao.roles:
                        role = dao.roles[fromID]
                        if content in dao.roles:
                        
                            role.add_aggregated(dao.roles[content])
                        elif content in dao.committees:
                            role.add_aggregated(dao.committees[content])
                    elif fromID in dao.committees:
                        committee = dao.committees[fromID]
                        if content in dao.committees:
                            committee.add_aggregated(dao.committees[content])
                        elif content in dao.roles:
                            committee.add_aggregated(dao.roles[content])
                elif relation[0] == dc.RelationType.FEDERATION:
                    if fromID in dao.roles:
                        role = dao.roles[fromID]
                        if content in dao.committees:
                            #the source role is part of the target committee
                            role.add_committee_membership(dao.committees[content])
                            #the target committee has the source role as a member
                            dao.committees[content].add_member_entity(role)
                        else:
                            print(f'ERROR: wrong federation type: Role {fromID} -> {content} \n')
                    elif fromID in dao.committees:
                        committee = dao.committees[fromID]
                        if content in dao.committees:
                            #the source committee is part of the target committee
                            committee.add_committee_membership(dao.committees[content])
                            #the target committee has the source committee as a member
                            dao.committees[content].add_member_entity(committee)
                        else:
                            print(f'ERROR: wrong federation type: Committee {fromID} -> {content} \n')
            dao.metadata.save_user_functionalities_group_size(dao.roles, dao.committees)
            # Assign voting and proposal permissions to committees
            for committee in dao.committees.values():
                # Assign voting and proposal permissions to committees
                voting_permission = self.create_governance_permission("Voting", committee)
                proposal_permission = self.create_governance_permission("Proposal", committee)
                dao.add_permission(voting_permission)
                dao.add_permission(proposal_permission)
                for role_or_committee in committee.member_entities:
                    if isinstance(role_or_committee, dc.Role or isinstance(role_or_committee, dc.Committee)):
                        if voting_permission not in role_or_committee.permissions:
                            role_or_committee.add_permission(voting_permission)
                            #adding to the dictionary of voting rights to access it in simple translator
                            dao.role_and_committee_voting_right_dict[role_or_committee.get_id()] = committee.get_id()
                        if proposal_permission not in role_or_committee.permissions:
                            role_or_committee.add_permission(proposal_permission)
                            dao.role_and_committee_proposal_right_dict[role_or_committee.get_id()] = committee.get_id()
            # Assign aggregated permissions to roles and committees in DAO based on aggregation relations
            for role in dao.roles.values():
                self.get_aggregated_permissions(role)
            for committee in dao.committees.values():
                self.get_aggregated_permissions(committee)
            #generate conditions for the DAO
            self.generate_conditions(dao)
            #generate owner role
            self.generateOwnerRole(dao)
        self.createControlGraph()
        
    
    def generateOwnerRole(self, dao):
        #create owner role
        owner_role_name = f"{dao.dao_name}Owner".replace(" ", "_")
        owner_role = dc.Role(role_id = owner_role_name, role_name= owner_role_name, role_assignment_method = "Non Assignable", n_agent_min =None, n_agent_max=None, agent_type=None)
        dao.owner_role = owner_role
        for permission in dao.permissions.values():
            owner_role.add_permission(permission)
        dao.add_role(owner_role)
        for role in dao.roles.values():
            role.add_controller(owner_role.role_id)
        for committee in dao.committees.values():
            committee.add_controller(owner_role.role_id)


    def create_governance_permission(self, type, committee):
        permission_id = committee.committee_id + type +"Right"
        allowed_action = committee.committee_description + " " + type + " Right"
        if type == "Voting":
            permission = dc.Permission(permission_id=permission_id, allowed_action= allowed_action, permission_type ="strategic", ref_gov_area = None, voting_right = True, proposal_right = False)

        elif type == "Proposal":
            permission = dc.Permission(permission_id=permission_id, allowed_action= allowed_action, permission_type ="strategic", ref_gov_area = None, voting_right = False, proposal_right = True)
        return permission
    
    def generate_conditions(self, dao: dc.DAO):
        #storing both the list of the conditions and the respective relations with the roles and committees (how conditions are used in the DAO)
        conditions = []
        for role in dao.roles.values():
            if role.role_assignment_method != None:
                dao.assignment_conditions[role.role_id]= role.role_assignment_method
                if role.role_assignment_method not in conditions:
                    conditions.append(role.role_assignment_method)

        for committee in dao.committees.values():
            if committee.voting_condition != None:
                dao.voting_conditions[committee.committee_id]= committee.voting_condition
                if committee.voting_condition not in conditions:
                    conditions.append(committee.voting_condition)
            if committee.voting_condition != None:
                dao.proposal_conditions[committee.committee_id]= committee.proposal_condition
                if committee.proposal_condition not in conditions:
                    conditions.append(committee.proposal_condition)
        dao.conditions = conditions

    def __str__(self):
        result = ["DAOs:"]
        for dao in self.daoByID.values():
            result.append(str(dao))
            result.append("\nRelations:")
            for role in self.relations_by_dao[dao.dao_id]:
                result.append(str(role))
        return "\n".join(result)
    