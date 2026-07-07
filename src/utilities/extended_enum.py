from enum import Enum
import src.utilities.stringable_jsonable as s_j


class ExtendedEnum(s_j.StringableJsonable, Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    def to_string(self, indent=None, **kwarg) -> str:
        return f"\"{type(self)}<name: {self.name}, value: {self.value}>\""

    def to_json(self, **kwargs) -> dict:
        return {
            "class_name": type(self),
            "name": self.name,
            "value": self.value
        }
