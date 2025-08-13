import src.model.base_entity as base_entity
import src.model.permission as permission
#import src.model.role as role

# super class of both Committee and Role
class AggregableEntity(base_entity.BaseEntity):
    def __init__(self, id):
        super().__init__(id)
        self.permissions:list[permission.Permission] = []
        self.controllers:list[str] = []
        self.aggregated:list[AggregableEntity] =  []
        self.federated_committees:list[AggregableEntity] = []

    def get_name(self) -> str:
        raise Exception(f"get_name not implemented in {self.__class__.__name__}")
        
    def add_permission(self, permission: permission.Permission):
        print(f'Adding permission {str(permission)} to {self.__class__.__name__} {self.id}')
        self.permissions.append(permission)

    def add_controller(self, controller_id:str):
        self.controllers.append(controller_id)
        
    def add_aggregated(self, aggregated):
        if not isinstance(aggregated, AggregableEntity):
            raise Exception(f"Given aggregated is not an AggregableEntity: {type(aggregated)}")
        self.aggregated.append(aggregated)

    def add_committee_membership(self, target_committee):
        if not isinstance(target_committee, AggregableEntity):
            raise Exception(f"Given target_committee is not an AggregableEntity: {type(target_committee)}")
        self.federated_committees.append(target_committee)
        print(f'Adding {type(target_committee)} {target_committee.get_id()} to {self.__class__.__name__} {self.id}')
        #storing the relation that indicates that the given committee federates into a target committee
        
    def __str__(self, more_stuff=None):
        parts = [] if more_stuff is None else ([more_stuff] if isinstance(more_stuff, str) else more_stuff)
        parts.append(f", permissions<{len(self.permissions)}>=[")
        parts.append(",".join(p.get_id() for p in self.permissions))
        parts.append("]")
        parts.append(f", controllers<{len(self.controllers)}>=[")
        parts.append(",".join(str(c) for c in self.controllers))
        parts.append("]")
        parts.append(f", aggregated<{len(self.aggregated)}>=[")
        parts.append(",".join(str(a) for a in self.aggregated))
        parts.append("]")
        return super().__str__(parts)

    def toJSON(self):
        obj = super().toJSON()
        obj["permissions"] = [ p.get_id() for p in self.permissions]
        obj["controllers"] = self.controllers
        obj["aggregated"] =  [ agg.get_id() for agg in self.aggregated ]
        obj["federated_committees"] = [c.get_id() for c in self.federated_committees] 
        return obj
