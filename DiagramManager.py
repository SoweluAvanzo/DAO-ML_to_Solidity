import DAOclasses as dc
from collections import defaultdict
import networkx as nx

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
    def get_dao_by(self, daoOrID: str|dc.DAO) -> dc.DAO:
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
    
    def addRole(self, daoOrID: str|dc.DAO, role: dc.Role):
        dao = self.get_dao_by(daoOrID)
        dao.add_role(role)

    def addCommittee(self, daoOrID: str|dc.DAO, committee: dc.Committee):
        dao = self.get_dao_by(daoOrID)
        dao.add_committee(committee)

    def addPermission(self, daoOrID: str|dc.DAO, permission: dc.Permission ):
        dao = self.get_dao_by(daoOrID)
        dao.add_permission(permission)
        

    def addRelation(self, daoOrID: str|dc.DAO, relationType: dc.RelationType, fromID: str, content:str ):
        dao = self.get_dao_by(daoOrID)
        dao_id = dao.dao_id
        self.relations_by_dao[dao_id].append( (relationType, fromID, content) )
    #
    #
    #
    def createControlGraph(self):
        # crea il control graph, tramite una istanza di una classe __che dovremmo ancora definire__
        for dao in self.daoByID.values():
            dao_id = dao.dao_id
            cg_wrapper = dc.ControlGraph(dao)
            print(f'Control Graph {cg_wrapper.control_graph} created for DAO: {dao_id} \n')
            dao.dao_control_graph = cg_wrapper         
        # for role in dao.roles.values():
        #         for controller in role.controllers:
        #             dao.dao_control_graph.add_edge(role.role_id,controller)
        #     for committee in dao.committees.values():
        #         for controller in committee.controllers:
        #             dao.dao_control_graph.add_edge(committee.committee_id,controller)
        #     print(f'Control graph generated for DAO {dao_id} \nPrinting edges and nodes \n')
        #     #assignment of control graph to DAO object
        #     # print edges
        #     for node in dao.dao_control_graph.nodes:
        #         print(f'Node: {node} \n')
        #     for edge in dao.dao_control_graph.edges:
        #         print(f'Edge: {edge} \n')
        #     #print paths
        #     for loop in nx.simple_cycles(dao.dao_control_graph):
        #         print(f'Loop: {loop} \n') 
        

    def processRawInstances(self):
        if not self.rowDataOnly:
            return
        # TODO: copia-e-incolla da "parse_xml.py", dal metodo "visitDao()", tutti quei cicli for
        # che processano le varie istanze (di Role, Committee, etc)

        # Assign permissions to roles and committees in DAO based on association relations
        for dao in self.daoByID.values():
            dao_id = dao.dao_id
            for relation in self.relations_by_dao[dao_id]:
                print(f'Relation: {relation} \n')
                fromID = relation[1]
                content = relation[2]
                if relation[0] == dc.RelationType.CONTROL:
                    the_controller_ID = content
                    the_slaaaaaaaaaave_ID= fromID

                    print(f'Control relation found: {the_controller_ID} -> {the_slaaaaaaaaaave_ID} \n')
                    if the_slaaaaaaaaaave_ID in dao.roles:
                        role = dao.roles[the_slaaaaaaaaaave_ID]
                        print(f'Role found: {role.role_id} , controlled by {the_controller_ID} \n')
                        role.add_controller(the_controller_ID)
                    elif the_slaaaaaaaaaave_ID in dao.committees:
                        committee = dao.committees[the_slaaaaaaaaaave_ID]
                        print(f'Committee found: {committee.committee_id} , controlled by {the_controller_ID} \n')
                        committee.add_controller(the_controller_ID) 
                    else:
                        print(f"ERROR: the controller __{the_controller_ID}__ should control __{the_slaaaaaaaaaave_ID}__, but this last one has not been found")
                elif relation[0] == dc.RelationType.ASSOCIATION:
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
                elif relation[0] == dc.RelationType.AGGREGATION:
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
        print(f' in process raw instances DAO: {dao_id} is processed. \n DAO Conent: {dao} \n')            
        self.createControlGraph()

            # Assign controllers to roles and committees in DAO based on control relations
            # for role in self.roles.values():
            #     for controller in self.control_relations[role.role_id]:
            #         role.add_controller(controller)
            #         print(f'Controller {controller} assigned to Role {role.role_id} \n')
            # for committee in self.committees.values():
            #     for controller in self.control_relations[committee.committee_id]:
            #         committee.add_controller(controller)
            #         print(f'Controller {controller} assigned to Committee {committee.committee_id} \n')

            # # Assign aggregated roles and committees to roles and committees in DAO based on aggregation relations
            # for role in self.roles.values():
            #     for aggregated in self.aggregations[role.role_id]:
            #         role.add_aggregated(aggregated)
            #         print(f'Role {role.role_id} aggregates into: {aggregated} \n')
            # for committee in self.committees.values():
            #     for aggregated in self.aggregations[committee.committee_id]:
            #         committee.add_aggregated(aggregated)
            #         print(f' Committee "{role.role_id}" aggregates into  {aggregated}\n')
            
            # Assign controllers to roles and committees in DAO based on control relations
            # for role in self.roles.values():
            #     for controller_id in self.control_relations[role.role_id]:
            #         if controller_id in self.roles:
            #             role.add_controller(self.roles[controller_id])
            #             print(f'Controller {controller_id} assigned to Role {role.role_id} \n')
            #         elif controller_id in self.committees:
            #             role.add_controller(self.committees[controller_id])
            #             print(f'Controller {controller_id} assigned to Role {role.role_id} \n')
            # for committee in self.committees.values():
            #     for controller_id in self.control_relations[committee.committee_id]:
            #         if controller_id in self.roles:
            #             committee.add_controller(self.roles[controller_id])
            #             print(f'Controller {controller_id} assigned to Committee {committee.committee_id} \n')
            #         elif controller_id in self.committees:
            #             committee.add_controller(self.committees[controller_id])
            #             print(f'Controller {controller_id} assigned to Committee {committee.committee_id} \n')

            #assignemnt of roles and committees defined to the DAO

            
            #control graph generation based on control relations stored
           
            #code generation
            #translator = SolidityTranslator(self.daos[dao_id])
            #translator.save_to_file()

        # alla fine, ...


    def __str__(self):
        result = ["DAOs:"]
        for dao in self.daoByID.values():
            result.append(str(dao))
            result.append("\nRelations:")
            for role in self.relations_by_dao[dao.dao_id]:
                result.append(str(role))

        return "\n".join(result)
    