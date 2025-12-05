import json


class StringableJsonable:
    def to_string(self, indent=None, **kwarg) -> str:
        ind = None
        isint = False
        if isinstance(indent, int):
            ind = indent

            isint = True
        elif isinstance(indent, str):
            ind = indent
        else:  # None or something else
            isint = True
            ind = 2
        if isint:
            ind = '\t' * ind
        indent = f"{ind}\t\t"
        field_spacer = f',\n{ind}'
        return f"{'{'} {field_spacer.join(f"{k}: {v.to_string(indent=indent) if isinstance(v, StringableJsonable) else v}" for k, v in self.__dict__.items())} {'}'}"

    def __str__(self):
        return self.to_string(indent=2)

    def to_json(self, **kwargs) -> dict:
        d = self.__dict__.items()
        can_recour = False
        for k, v in d:
            if isinstance(v, StringableJsonable):
                can_recour = True
                break
        return {
            k: v.to_json() if isinstance(v, StringableJsonable) else v
            for k, v in d
        } if can_recour \
            else self.__dict__

    def __repr__(self):
        return json.dumps(self.to_json())
