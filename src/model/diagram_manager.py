import src.model.dao as dao_module
import src.model.role as role_module
import src.model.committee as committee_module
import src.model.permission as permission_module
import src.model.enums.relation_type as rt
import src.control_graph.control_graph_basic as cgb


class DiagramManager:
    def __init__(self, controGraphGenerator=None):
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
    