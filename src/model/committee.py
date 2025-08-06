import src.model.base_entity as base_entity
import src.model.aggregable_entity as aggregable_entity
import src.model.permission as permission
import src.model.role as role

#stores committee information with control relations and permissions
class Committee(aggregable_entity.AggregableEntity):
    #removed n_agent_min, n_agent_max
    def __init__(self, id, committee_description:str, voting_condition, proposal_condition, decision_making_method):
        super().__init__(id)
        self.committee_description = committee_description
        self.voting_condition = voting_condition
        self.proposal_condition = proposal_condition
        self.decision_making_method = decision_making_method
        self.member_entities:list[Committee] = []

    def get_name(self) -> str:
        return self.committee_description

    def add_member_entity(self, entity:base_entity.BaseEntity):
        self.member_entities.append(entity)
        print(f'Adding member entity {entity.get_id()} to committee {self.id}')

    def __str__(self):
        parts=[f', committee_description={self.committee_description}, voting_condition={self.voting_condition}, proposal_condition={self.proposal_condition}, decision_making_method={self.decision_making_method}']
        parts.append(f", member_entities<{len(self.member_entities)}>=[{','.join(e.get_id() for e in self.member_entities)}]")
        return super().__str__(parts)

    def toJSON(self):
        obj = super().toJSON()
        obj["committee_description"] = self.committee_description
        obj["voting_condition"] = self.voting_condition
        obj["proposal_condition"] = self.proposal_condition
        obj["decision_making_method"] = self.decision_making_method
        obj["member_entities"] = [c.get_id() for c in self.member_entities]
        return obj
