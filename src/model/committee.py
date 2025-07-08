import src.model.base_entity as base_entity
import src.model.permission as permission
import src.model.role as role

#stores committee information with control relations and permissions
class Committee(base_entity.BaseEntity):
    #removed n_agent_min, n_agent_max
    def __init__(self, id, committee_description, voting_condition, proposal_condition, decision_making_method):
        super().__init__(id)
        self.committee_description = committee_description
        self.voting_condition = voting_condition
        self.proposal_condition = proposal_condition
        self.decision_making_method = decision_making_method

        self.permissions:list[permission.Permission] = []
        self.controllers:list[str] = []
        self.aggregated:list[role.Role|Committee] =  []
        self.member_entities:list[Committee] = []
        self.federated_committees:list[Committee|role.Role] = []

    def get_name(self) -> str:
        return self.committee_description
    
    def add_permission(self, permission: permission.Permission):
        print(f'Adding permission {str(permission)} to committee {self.id}')
        self.permissions.append(permission)

    def add_controller(self, controller_id:str):
        self.controllers.append(controller_id)
        
    def add_aggregated(self, aggregated):
        self.aggregated.append(aggregated)

    def add_committee_membership(self, target_committee):
        self.federated_committees.append(target_committee)
        print(f'Adding committee {target_committee.get_id()} to committee {self.id}')
        #storing the relation that indicates that the given committee federates into a target committee
        
    def add_member_entity(self, entity:base_entity.BaseEntity):
        self.member_entities.append(entity)
        print(f'Adding member entity {entity.get_id()} to committee {self.id}')

    def __str__(self):
        parts=[f', committee_description={self.committee_description}, voting_condition={self.voting_condition}, proposal_condition={self.proposal_condition}, decision_making_method={self.decision_making_method}']
        is_not_first = False
        parts.append(", permissions=[")
        for p in self.permissions:
            parts.append(p.id)
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
        additional_parts = "".join(parts)
        parts = None
        return super().__str__(additional_parts)

    def toJSON(self):
        obj = super().toJSON()
        obj["committee_description"] = self.committee_description
        obj["voting_condition"] = self.voting_condition
        obj["proposal_condition"] = self.proposal_condition
        obj["decision_making_method"] = self.decision_making_method
        obj["permissions"] = [ p.id for p in self.permissions]
        obj["controllers"] = self.controllers
        obj["aggregated"] =  [agg.get_id() for agg in self.aggregated]
        obj["member_entities"] = [c.get_id() for c in self.member_entities]
        obj["federated_committees"] = [c.get_id() for c in self.federated_committees]
        return obj
