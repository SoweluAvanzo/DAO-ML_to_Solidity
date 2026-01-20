import src.model.aggregable_entity as aggregable_e
# import src.model.permission as permission
# import src.model.committee as committee


class Role(aggregable_e.AggregableEntity):
    def __init__(self, role_id: str, role_name: str, role_assignment_method: str, n_agent_min: int, n_agent_max: int, agent_type: str):
        super().__init__(role_id)
        self.role_name = role_name
        self.role_assignment_method = role_assignment_method
        self.n_agent_min = n_agent_min
        self.n_agent_max = n_agent_max
        self.agent_type = agent_type

    def get_name(self) -> str:
        return self.role_name

    def __str__(self):
        more_stuff = f', role_name={self.role_name}, role_assignment_method={self.role_assignment_method}, n_agent_min={self.n_agent_min}, n_agent_max={self.n_agent_max}, agent_type={self.agent_type}'
        return super().__str__(more_stuff)

    def toJSON(self):
        obj = super().toJSON()
        obj["role_name"] = self.role_name
        obj["role_assignment_method"] = self.role_assignment_method
        obj["n_agent_min"] = int(self.n_agent_min) \
            if self.n_agent_min is not None \
            else None
        obj["n_agent_max"] = int(self.n_agent_max) \
            if self.n_agent_max is not None \
            else None
        obj["agent_type"] = self.agent_type
        return obj
