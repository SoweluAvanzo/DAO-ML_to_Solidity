import src.model.base_entity as base_entity


class GovernanceArea(base_entity.BaseEntity):
    def __init__(self, gov_area_ID: str, gov_area_description: str, implementation: str):
        super.__init__(self, gov_area_ID)
        self.gov_area_ID = gov_area_ID
        self.gov_area_description = gov_area_description
        self.implementation = implementation

    def get_id(self) -> str:
        return self.gov_area_ID

    def get_name(self) -> str:
        return self.gov_area_description

    def __str__(self):
        return f'GovernanceArea(gov_area_ID={self.gov_area_ID}, gov_area_description={self.gov_area_description}, implementation={self.implementation})'

    def toJSON(self):
        return {
            "gov_area_ID": self.gov_area_ID,
            "gov_area_description": self.gov_area_description,
            "implementation": self.implementation,
        }
