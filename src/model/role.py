import src.model.base_entity as base_entity
import src.model.permission as permission
import src.model.committee as committee

class Role(base_entity.BaseEntity):
    def __init__(self, role_id, role_name, role_assignment_method, n_agent_min, n_agent_max, agent_type):
        super().__init__(role_id)
        self.role_name = role_name
        self.role_assignment_method = role_assignment_method
        self.n_agent_min = n_agent_min
        self.n_agent_max = n_agent_max
        self.agent_type = agent_type
    
        self.permissions: list[permission.Permission] = []
        self.controllers:list[str] = [] # just the ID
        self.aggregated:list[Role|committee.Committee] =  []
        self.federated_committees:list[committee.Committee] = []

    def add_permission(self, permission: permission.Permission):
        print(f'Adding permission {str(permission)} to role {self.id}')
        self.permissions.append(permission)

    def add_controller(self, controller_id:str):
        self.controllers.append(controller_id)
    
    def add_aggregated(self, aggregated):
        self.aggregated.append(aggregated)

    def add_committee_membership(self, target_committee:any):
        self.federated_committees.append(target_committee)

    def __str__(self):
        parts = [f', role_name={self.role_name}, role_assignment_method={self.role_assignment_method}, n_agent_min={self.n_agent_min}, n_agent_max={self.n_agent_max} agent_type={self.agent_type}']
        is_not_first = False
        parts.append(f", permissions<{len(self.permissions)}>=[")
        for p in self.permissions:
            parts.append(p.id)
            if is_not_first:
                parts.append(", ")
            else:
                is_not_first = True
        parts.append("]")
        is_not_first = False
        parts.append(f", controllers<{len(self.controllers)}>=[")
        for c in self.controllers:
            if is_not_first:
                parts.append(", ")
            else:
                is_not_first = True
            parts.append(str(c))
        parts.append("]")
        is_not_first = False
        parts.append(f", aggregated<{len(self.aggregated)}>=[")
        for a in self.aggregated:
            if is_not_first:
                parts.append(", ")
            else:
                is_not_first = True
            parts.append(str(a))
        parts.append("]")
        additional_parts = "".join(parts)
        parts = None
        return super().__str__(additional_parts)
    

    def toJSON(self):
        obj = super().toJSON()
        obj["role_name"] = self.role_name
        obj["role_assignment_method"] = self.role_assignment_method
        obj["n_agent_min"] = self.n_agent_min
        obj["n_agent_max"] = self.n_agent_max
        obj["agent_type"] = self.agent_type
        obj["permissions"] = [ p.id for p in self.permissions]
        obj["controllers"] = self.controllers
        obj["aggregated"] =  [ agg.get_id() for agg in self.aggregated ]
        obj["federated_committees"] = [c.id for c in self.federated_committees] 
        return obj
