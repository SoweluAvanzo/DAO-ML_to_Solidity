import json

import src.postprocessing.model_conversion.shared.conversion_result_base as crb
import src.model.base_entity as base_entity_module

class ConvertedSubpart(crb.ModelConversionResultBase):
    def __init__(self, entity: base_entity_module.BaseEntity, entity_specific_data:dict, \
            is_convertible:bool=True \
        ):
        self.entity: base_entity_module.BaseEntity = entity
        self.entity_specific_data = entity_specific_data
        self.is_convertible = is_convertible

    def can_be_converted(self) -> bool:
        """
        Override-designed
        Defines if this class (or instance) can be converted: some classes are just holders
        of sub-parts needing to te converted, therefore they (usually) do NOT need to be
        converted.
        """
        return self.is_convertible

    def get_id(self) -> str:
        return self.entity.get_id()
    
    def get_alternative_name(self):
        return ""
    
    def get_name(self):
        n = self.get_alternative_name()
        if n is not None and n.strip() != "":
            return n.strip()
        if self.entity is None:
            return ""
        return self.entity.get_name()
    
    def get_specific_data_name(self):
        return ""
    
    def toJSON(self):
        return {
            f"{type(self.entity)}": self.entity.get_id(), # "get_id()" instead of "toJSON()" to not clutter the output
            f"{self.get_specific_data_name()}": {k:self.entity_specific_data[k] for k in self.entity_specific_data.keys() if not callable(self.entity_specific_data[k])}
        }
    def __repr__(self):
        return json.dumps(self.toJSON())