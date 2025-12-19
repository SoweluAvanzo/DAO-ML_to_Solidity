import json


class StringableJsonable:
    def to_string_primitive_val(self, x) -> str:
        if isinstance(x, bool):
            return "true" if x else "false"
        elif isinstance(x, str):
            return f"\"{x}\""
        else:
            return str(x)

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
        indent_new = f"{ind}\t\t"
        lines = [f'{ind}{'{'}']
        items_left = len(self.__dict__)
        for k, v in self.__dict__.items():
            comma = "" if items_left == 1 else ","
            if isinstance(v, StringableJsonable):
                lines.append(
                    f"{ind}{k}: {v.to_string(indent=indent_new)}{comma}")
            elif isinstance(v, (list, tuple)):
                lines.append(f"{ind}{k}: [")
                items_left_2 = len(v)
                for e in v:
                    c = "" if items_left_2 == 1 else ","
                    lines.append(
                        f"{indent_new}{e.to_string(indent=indent_new) if isinstance(e, StringableJsonable) else self.to_string_primitive_val(e)}{c}"
                    )
                    items_left_2 -= 1
                lines.append(f"{ind}]{comma}")
            elif isinstance(v, dict):
                lines.append(f"{ind}{k}: {'{'}")
                items_left_2 = len(v)
                for k2, e in v.items():
                    c = "" if items_left_2 == 1 else ","
                    lines.append(
                        f"{indent_new}{k2}: {e.to_string(indent=indent_new) if isinstance(e, StringableJsonable) else self.to_string_primitive_val(e)}{c}"
                    )
                    items_left_2 -= 1
                lines.append(f"{ind}{'}'}{comma}")
            else:
                lines.append(
                    f"{ind}{k}: {self.to_string_primitive_val(v)}{comma}")
            items_left -= 1
        lines.append(f"{ind}{'}'}")
        return "\n".join(lines)

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
            k: v.to_json(**kwargs) if isinstance(v, StringableJsonable) else v
            for k, v in d
        } if can_recour \
            else self.__dict__

    def __repr__(self):
        return json.dumps(self.to_json())
