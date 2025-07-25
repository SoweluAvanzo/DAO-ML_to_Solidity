import src.model.aggregable_entity as aggregable_entity
import src.model.permission as permission
import src.model.committee as committee

class Role(aggregable_entity.AggregableEntity):
    def __init__(self, role_id, role_name, role_assignment_method, n_agent_min, n_agent_max, agent_type):
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
        obj["n_agent_min"] = self.n_agent_min
        obj["n_agent_max"] = self.n_agent_max
        obj["agent_type"] = self.agent_type
        return obj
