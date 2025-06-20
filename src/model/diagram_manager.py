import src.model.base_entity as base_entity_module
import src.model.dao as dao_module
import src.model.role as role_module
import src.model.committee as committee_module
import src.model.permission as permission_module
import src.model.enums.relation_type as rt
import src.model.enums.governance_permission as gp
import src.control_graph.control_graph_basic as cgb


class DiagramManager(base_entity_module.BaseEntity):
    def __init__(self, controGraphGenerator=None):
        super().__init__("DiagramManager_ID")
        self.uniqueID = "DiagramManager_ID"
        self.rowDataOnly = True
        self.daoByID: map[str, dao_module.DAO] = {}
        self.relations_by_dao: map[str, list[tuple[rt.RelationType, str, str]]] = {}
        self.controGraphGenerator = controGraphGenerator

    def get_dao_by(self, daoOrID):
        dao = None
        if isinstance(daoOrID, dao_module.DAO):
            dao = daoOrID
        elif isinstance(daoOrID, str):
            dao = self.daoByID[daoOrID]
        else:
            raise Exception("Unknown type of dao / dao's ID : " + daoOrID)
        return dao


    def addDao(self, dao: dao_module.DAO):
        self.daoByID[dao.get_id()] = dao
        dao_id = dao.get_id()
        self.relations_by_dao[dao_id] = []
    
    def addRole(self, daoOrID, role: role_module.Role):
        dao = self.get_dao_by(daoOrID)
        dao.add_role(role)

    def addCommittee(self, daoOrID, committee: committee_module.Committee):
        dao = self.get_dao_by(daoOrID)
        dao.add_committee(committee)

    def addPermission(self, daoOrID, permission: permission_module.Permission ):
        dao = self.get_dao_by(daoOrID)
        dao.add_permission(permission)
        

    def addRelation(self, daoOrID, relationType: rt.RelationType, fromID: str, content:str ):
        dao = self.get_dao_by(daoOrID)
        dao_id = dao.get_id()
        self.relations_by_dao[dao_id].append( (relationType, fromID, content) )
    

    #
    def createControlGraph(self, daoOrID):
        dao = self.get_dao_by(daoOrID)
        return cgb.ControlGraphBasic(dao) if self.controGraphGenerator is None else self.controGraphGenerator(dao)


    def get_aggregated_permissions(self, role_or_committee: role_module.Role | committee_module.Committee):
        pass #TODO


    def processRawInstances(self):
        #TODO: use gp.GovernancePermission
        pass #TODO


    def generateOwnerRole(self, dao: dao_module.DAO):
        pass #TODO


    def create_governance_permission(self, type, committee: committee_module.Committee):
        pass #TODO


    def generate_conditions(self, dao: dao_module.DAO):
        pass #TODO


    def __str__(self):
        result = ["DAOs:"]
        for dao in self.daoByID.values():
            result.append(str(dao))
            result.append("\nRelations:")
            for role in self.relations_by_dao[dao.get_id()]:
                result.append(str(role))
        return "\n".join(result)
    
    
    def toJSON(self):
        """ 
        self.uniqueID = "DiagramManager_ID"
        self.rowDataOnly = True
        self.daoByID: map[str, dao_module.DAO] = {}
        self.relations_by_dao: map[str, list[tuple[rt.RelationType, str, str]]] = {}
         """
        #self.controGraphGenerator

        relations_by_dao = {
                dao_id: [\
                    { \
                        "relationType": rel_data[0].name, \
                        "fromID": rel_data[1], \
                        "content": rel_data[2], \
                    }\
                    for rel_data in relations
                ]
                for dao_id, relations in self.relations_by_dao.items()
            }
        daoByID = {\
            dao_id: repr(dao) \
            for dao_id, dao in self.daoByID.items() \
        }
        return {
            "id": self.id,
            "uniqueID": self.uniqueID,
            "rowDataOnly": self.rowDataOnly,
            "relations_by_dao": relations_by_dao,
            "daoByID": daoByID,
            "controGraphGenerator": None
        }
