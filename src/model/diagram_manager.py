import src.model.base_entity as base_entity_module
import src.model.dao as dao_module
import src.model.role as role_module
import src.model.committee as committee_module
import src.model.permission as permission_module
import src.model.governance_area as governance_area_module
import src.model.enums.relation_type as rt
import src.model.enums.governance_permission as gp
import src.control_graph.control_graph_basic as cgb


class DiagramManager(base_entity_module.BaseEntity):
    def __init__(self, controGraphGenerator=None):
        super().__init__("DiagramManager_ID")
        self.uniqueID = "DiagramManager_ID"
        self.rowDataOnly = True
        self.daoByID: dict[str, dao_module.DAO] = {}
        self.relations_by_dao: dict[str,
                                    list[tuple[rt.RelationType, str, str]]] = {}
        self.controGraphGenerator = controGraphGenerator

    def get_name(self) -> str:
        return self.uniqueID

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

    def addPermission(self, daoOrID, permission: permission_module.Permission):
        dao = self.get_dao_by(daoOrID)
        dao.add_permission(permission)

    def addRelation(self, daoOrID, relationType: rt.RelationType, fromID: str, content: str):
        dao = self.get_dao_by(daoOrID)
        dao_id = dao.get_id()
        self.relations_by_dao[dao_id].append((relationType, fromID, content))

    def addGovernanceArea(self, daoOrID, governance_area: governance_area_module.GovernanceArea):
        dao = self.get_dao_by(daoOrID)
        dao.add_governance_area(governance_area)

    #

    def createControlGraph(self, daoOrID: str, dao: dao_module.DAO = None):
        if dao is None:
            if isinstance(daoOrID, str):
                dao = self.get_dao_by(daoOrID)
            elif isinstance(daoOrID, dao_module.DAO):
                dao = daoOrID
            else:
                raise Exception(
                    "Can't create Control Graph with no provided DAO")
        cg = cgb.ControlGraphBasic(
            dao) if self.controGraphGenerator is None else self.controGraphGenerator(dao)
        dao.dao_control_graph = cg
        return cg

    def get_aggregated_permissions(self, role_or_committee):
        """
        get and collect recursively all "decendants", all members
        of inclusion relations that this Diagram could have.
        """
        if not (isinstance(role_or_committee, role_module.Role) or isinstance(role_or_committee, committee_module.Committee)):
            raise Exception(
                f"The provided role_or_committe is not a Role nor a Committe: {type(role_or_committee)}")
        for aggregated in role_or_committee.aggregated:
            self.get_aggregated_permissions(aggregated)
            # the aggregator inherits permissions from the aggregated
            for permission in aggregated.permissions:
                if permission not in role_or_committee.permissions:
                    source_id = role_or_committee.get_id() if isinstance(
                        role_or_committee, role_module.Role) else role_or_committee.get_id()
                    target_id = aggregated.get_id() if isinstance(
                        aggregated, role_module.Role) else aggregated.get_id()
                    role_or_committee.add_permission(permission)
            # the aggregator also inherits controllers from the aggregated
            for controller in aggregated.controllers:
                if controller not in role_or_committee.controllers:
                    role_or_committee.add_controller(controller)

    def processRawInstances(self):
        print("\n running processRawInstances\n")
        # TODO 20/06/2025: use gp.GovernancePermission  Assign permissions to roles and committees in DAO based on association relations
        # TODO 20/06/2025: rafactor away this creation because it's not DiagramManager's responsibility to perfor all of this "management"
        for daooo in self.daoByID.values():
            dao: dao_module.DAO = daooo
            dao_id: str = dao.get_id()
            for relation in self.relations_by_dao[dao_id]:
                fromID = relation[1]
                content = relation[2]
                if relation[0] == rt.RelationType.CONTROL:
                    the_controller_ID = content
                    controlled_ID = fromID

                    if controlled_ID in dao.roles:
                        role = dao.roles[controlled_ID]
                        role.add_controller(the_controller_ID)
                    elif controlled_ID in dao.committees:
                        committee = dao.committees[controlled_ID]
                        committee.add_controller(the_controller_ID)
                    else:
                        print(
                            f"ERROR: the controller __{the_controller_ID}__ should control __{controlled_ID}__, but this last one has not been found")
                elif relation[0] == rt.RelationType.ASSOCIATION:
                    if fromID in dao.roles:
                        role = dao.roles[fromID]
                        if content in dao.permissions:
                            role.add_permission(dao.permissions[content])
                    elif fromID in dao.committees:
                        committee = dao.committees[fromID]
                        if content in dao.permissions:
                            committee.add_permission(dao.permissions[content])
                elif relation[0] == rt.RelationType.AGGREGATION:
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
                elif relation[0] == rt.RelationType.FEDERATION:
                    if fromID in dao.roles:
                        role = dao.roles[fromID]
                        if content in dao.committees:
                            # the source role is part of the target committee
                            role.add_committee_membership(
                                dao.committees[content])
                            # the target committee has the source role as a member
                            dao.committees[content].add_member_entity(role)
                        else:
                            print(
                                f'ERROR: wrong federation type: Role {fromID} -> {content} \n')
                    elif fromID in dao.committees:
                        committee = dao.committees[fromID]
                        if content in dao.committees:
                            # the source committee is part of the target committee
                            committee.add_committee_membership(
                                dao.committees[content])
                            # the target committee has the source committee as a member
                            dao.committees[content].add_member_entity(
                                committee)
                        else:
                            print(
                                f'ERROR: wrong federation type: Committee {fromID} -> {content} \n')
            dao.metadata.save_user_functionalities_group_size(
                dao.roles, dao.committees)
            # Assign voting and proposal permissions to committees
            for committee in dao.committees.values():
                # Assign voting and proposal permissions to committees
                voting_permission = self.create_governance_permission(
                    gp.GovernancePermission.VOTING, committee)
                proposal_permission = self.create_governance_permission(
                    gp.GovernancePermission.PROPOSAL, committee)
                dao.add_permission(voting_permission)
                dao.add_permission(proposal_permission)
                for role_or_committee in committee.member_entities:
                    if isinstance(role_or_committee, role_module.Role or isinstance(role_or_committee, committee_module.Committee)):
                        if voting_permission not in role_or_committee.permissions:
                            role_or_committee.add_permission(voting_permission)
                            # adding to the dictionary of voting rights to access it in simple translator
                            dao.role_and_committee_voting_right_dict[role_or_committee.get_id(
                            )] = committee.get_id()
                        if proposal_permission not in role_or_committee.permissions:
                            role_or_committee.add_permission(
                                proposal_permission)
                            dao.role_and_committee_proposal_right_dict[role_or_committee.get_id(
                            )] = committee.get_id()
            # Assign aggregated permissions to roles and committees in DAO based on aggregation relations
            for role in dao.roles.values():
                self.get_aggregated_permissions(role)
            for committee in dao.committees.values():
                self.get_aggregated_permissions(committee)
            # generate conditions for the DAO
            self.generate_conditions(dao)
            # generate owner role
            self.generateOwnerRole(dao)
            self.createControlGraph(dao_id, dao)

    def generateOwnerRole(self, dao: dao_module.DAO):
        # create owner role
        owner_role_name = f"{dao.dao_name}Owner".replace(" ", "_")
        owner_role = role_module.Role(role_id=owner_role_name, role_name=owner_role_name,
                                      role_assignment_method="Non Assignable", n_agent_min=None, n_agent_max=None, agent_type=None)
        dao.owner_role = owner_role
        for permission in dao.permissions.values():
            owner_role.add_permission(permission)
        dao.add_role(owner_role)
        for role in dao.roles.values():
            role.add_controller(owner_role.get_id())
        for committee in dao.committees.values():
            committee.add_controller(owner_role.get_id())

    def create_governance_permission(self, governance_permission_type: gp.GovernancePermission, committee: committee_module.Committee):
        permission_id = committee.get_id() + governance_permission_type.value + "Right"
        allowed_action = committee.committee_description + \
            " " + governance_permission_type.value + " Right"
        if governance_permission_type == gp.GovernancePermission.VOTING:
            permission = permission_module.Permission(permission_id=permission_id, allowed_action=allowed_action,
                                                      permission_type="strategic", ref_gov_area=None, voting_right=True, proposal_right=False)
        elif governance_permission_type == gp.GovernancePermission.PROPOSAL:
            permission = permission_module.Permission(permission_id=permission_id, allowed_action=allowed_action,
                                                      permission_type="strategic", ref_gov_area=None, voting_right=False, proposal_right=True)
        return permission

    def generate_conditions(self, dao: dao_module.DAO):
        # storing both the list of the conditions and the respective relations with the roles and committees (how conditions are used in the DAO)
        conditions = []
        for role in dao.roles.values():
            if role.role_assignment_method != None:
                dao.assignment_conditions[role.get_id(
                )] = role.role_assignment_method
                if role.role_assignment_method not in conditions:
                    conditions.append(role.role_assignment_method)

        for committee in dao.committees.values():
            if committee.voting_condition != None:
                dao.voting_conditions[committee.get_id(
                )] = committee.voting_condition
                if committee.voting_condition not in conditions:
                    conditions.append(committee.voting_condition)
            if committee.proposal_condition != None:
                dao.proposal_conditions[committee.get_id(
                )] = committee.proposal_condition
                if committee.proposal_condition not in conditions:
                    conditions.append(committee.proposal_condition)
        dao.conditions = conditions

    def __str__(self):
        result = ["DiagramManager", f"\t uniqueID: {self.uniqueID}", "DAOs:"]
        try:
            for dao in self.daoByID.values():
                result.append("Dao")
                result.append("\t" + str(dao))
                result.append("\nRelations:")
                for role in self.relations_by_dao[dao.get_id()]:
                    result.append("\t" + str(role))
            return "\n".join(result)
        except Exception as e:
            print("ERROR on D")
            # print(e)
            import traceback
            traceback.print_exception(e)

            return f"ERROR in DiagramManager to-string:\n{e}"

    def toJSON(self):
        """ 
        self.uniqueID = "DiagramManager_ID"
        self.rowDataOnly = True
        self.daoByID: map[str, dao_module.DAO] = {}
        self.relations_by_dao: map[str, list[tuple[rt.RelationType, str, str]]] = {}
         """
        # self.controGraphGenerator

        relations_by_dao = {
            dao_id: [
                {
                    "relationType": rel_data[0].name,
                    "fromID": rel_data[1],
                    "content": rel_data[2],
                }
                for rel_data in relations
            ]
            for dao_id, relations in self.relations_by_dao.items()
        }
        daoByID = {
            dao_id: dao.toJSON()
            for dao_id, dao in self.daoByID.items()
        }
        return {
            "id": self.id,
            "uniqueID": self.uniqueID,
            "rowDataOnly": self.rowDataOnly,
            "relations_by_dao": relations_by_dao,
            "daoByID": daoByID,
            "controGraphGenerator": None
        }
