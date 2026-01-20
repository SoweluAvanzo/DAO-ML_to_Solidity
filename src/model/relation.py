
import src.utilities.stringable_jsonable as s_j

import src.model.enums.relation_type as rt


class Relation(s_j.StringableJsonable):
    def __init__(self,
                 dao_id: str,
                 relation_type: rt.RelationType,
                 from_id: str,
                 content: str
                 ):
        self.dao_id = dao_id
        self.relation_type = relation_type
        self.from_id = from_id
        self.content = content

    def to_string_primitive_val(self, x) -> str:
        if isinstance(x, rt.RelationType):
            return x.name
        return super().to_string_primitive_val(x)

    def to_json(self, **kwargs) -> dict:
        return {
            "dao_id": self.dao_id,
            "relation_type": self.relation_type.name,
            "from_id": self.from_id,
            "content": self.content
        }
