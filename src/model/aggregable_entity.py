import src.model.base_entity as base_entity
import src.model.permission as permission
# import src.model.role as role

# super class of both Committee and Role


class AggregableEntity(base_entity.BaseEntity):
    def __init__(self, id):
        super().__init__(id)
        self.permissions: dict[str, permission.Permission] = {}
        # set of IDs of things controlling this instance
        self.controllers: set[str] = set()
        self.aggregated: dict[str, AggregableEntity] = {}
        self.federated_committees: dict[str, AggregableEntity] = {}
        self.aggregation_level: int = 0
        self.federation_level: int = 0

    def get_name(self) -> str:
        raise Exception(
            f"get_name not implemented in {self.__class__.__name__}")

    def get_permissions(self) -> dict[str, permission.Permission]:
        return self.permissions

    def get_controllers(self) -> set[str]:
        return self.controllers

    def get_aggregated(self) -> dict[str, AggregableEntity]:
        return self.aggregated

    def get_federated_committees(self) -> dict[str, AggregableEntity]:
        return self.federated_committees

    def get_aggregation_level(self) -> int:
        return self.aggregation_level

    def get_federation_level(self) -> int:
        return self.federation_level

    #

    def add_permission(self, permission: permission.Permission):
        # print(f'Adding permission {str(permission)} to {self.__class__.__name__} {self.id}')
        self.permissions[permission.get_id()] = permission

    def add_controller(self, controller_id: str):
        self.controllers.add(controller_id)

    def add_aggregated(self, aggregated):
        if not isinstance(aggregated, AggregableEntity):
            raise Exception(
                f"Given aggregated is not an AggregableEntity: {type(aggregated)}")
        self.aggregated[aggregated.get_id()] = aggregated

    def add_committee_membership(self, target_committee):
        if not isinstance(target_committee, AggregableEntity):
            raise Exception(
                f"Given target_committee is not an AggregableEntity: {type(target_committee)}")
        self.federated_committees[target_committee.get_id()] = target_committee
        # print(f'Adding {type(target_committee)} {target_committee.get_id()} to {self.__class__.__name__} {self.id}')
        # storing the relation that indicates that the given committee federates into a target committee

    def __str__(self, more_stuff=None):
        parts = [] if more_stuff is None else (
            [more_stuff] if isinstance(more_stuff, str) else more_stuff)
        parts.append(f", permissions<{len(self.permissions)}>=[")
        parts.append(",".join(list(self.permissions.keys())))
        parts.append("]")
        parts.append(f", controllers<{len(self.controllers)}>=[")
        parts.append(",".join(str(c) for c in self.controllers))
        parts.append("]")
        parts.append(f", aggregated<{len(self.aggregated)}>=[")
        parts.append(",".join(self.aggregated.keys()))
        parts.append("]")
        parts.append(f", aggregation_level={self.aggregation_level}")
        parts.append(f", federation_level={self.federation_level}")
        return super().__str__(parts)

    def toJSON(self):
        obj = super().toJSON()
        obj["permissions"] = list(self.permissions.keys())
        obj["controllers"] = list(self.controllers)
        obj["aggregated"] = list(self.aggregated.keys())
        obj["federated_committees"] = list(self.federated_committees.keys())
        obj["aggregation_level"] = self.aggregation_level
        obj["federation_level"] = self.federation_level
        return obj
