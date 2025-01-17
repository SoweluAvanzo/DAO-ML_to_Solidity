import src.model.base_entity as base_entity

class Permission(base_entity.BaseEntity):
    def __init__(self, permission_id, allowed_action, permission_type, ref_gov_area = None, voting_right = False, proposal_right = False):
        super().__init__(permission_id)
        self.allowed_action = allowed_action
        self.permission_type = permission_type
        self.ref_gov_area = ref_gov_area
        self.voting_right = voting_right
        self.proposal_right = proposal_right

    def __str__(self):
        return super().__str__(f' allowed_action={self.allowed_action}, permission_type={self.permission_type}, ref_gov_area={self.ref_gov_area}')

    def toJSON(self):
        obj = super().toJSON()
        obj["allowed_action"] = self.allowed_action
        obj["permission_type"] = self.permission_type
        obj["ref_gov_area"] = self.ref_gov_area
        obj["voting_right"] = self.voting_right
        obj["proposal_right"] = self.proposal_right
        return obj
