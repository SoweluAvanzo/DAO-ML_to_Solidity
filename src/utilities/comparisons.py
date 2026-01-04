
global PRIMITIVE_TYPES
PRIMITIVE_TYPES = (bool, str, int, float)


def check_differences(current_field_base, current_field_new, field_path: str = None, field_path_filterer=None) -> list[str]:
    # global PRIMITIVE_TYPES
    """ Returns a list of errors and mismatches
    Args:
        bd (dm.DiagramManager): base Diagram (XML) to compare onto
        nd (dm.DiagramManager): new Diagram (JSON) to be compared
        field_path (str, optional): sequence of field names from the root obhect to the current field. Defaults to "".
        current_field_base (_type_, optional): _description_. Defaults to None.
        current_field_new (_type_, optional): _description_. Defaults to None.

    Returns:
        bool: _description_
    """
    if current_field_base == current_field_new:
        return None
    if field_path is None:
        field_path = ""
    if (field_path_filterer is not None) and field_path_filterer(current_field_base, current_field_new, field_path):
        return None
    if (current_field_base is None) and (current_field_new is None):
        return None  # i.e., both None -> no errors at all b
    if current_field_base is None:
        return [
            f"current_field base (in path: {field_path}) is None but the new is not ({type(current_field_new)})"
        ]
    if current_field_new is None:
        return [
            f"current_field new (in path: {field_path}) is None but the base is not ({type(current_field_base)})"
        ]
    type_base = type(current_field_base)
    type_new = type(current_field_new)
    # currently, only strict type comparison is implemented (rather than the flexible polymorph-aware "isinstance" allows)
    if (type_base != type_new) or ( \
        # is a class?
        ((type == type_base) or (type == type_new)
         or ("class" in f"{type_base}") or ("class" in f"{type_new}"))
        and (type_base.__name__ != type_new.__name__)
    ):
        return [
            f"in path: {field_path}, Type mismatch: << base = {type_base} >> ; << new = {type_new} >>"
        ]
    errors: list[str] = []
    # types should be equal ...
    if type_base in PRIMITIVE_TYPES:
        # all OK?
        return None if current_field_base == current_field_new \
            else [
                f"in path: {field_path}, primitive value (type: {type_base}) mismatch: << base = {current_field_base} >> ; << now = {current_field_new} >>"
            ]
    # iterable_of_key_vals = None  # for list, the key is the index
    keys: list = None  # indexes for list, string keys for dicts
    are_keys_strings = True  # else, integers (array's indexes)
    fields_base = None  # the list, the dict or the class's dicts-of-fields
    fields_new = None
    fields_collection_name: str = None
    index_field = 0
    if type_base == list:
        keys = range(len(current_field_base))  # set it already
        are_keys_strings = False
        fields_base = current_field_base
        fields_new = current_field_new
        fields_collection_name = "lists"
    elif (type_base == type) or ((type_base != dict) and ("class" in f"{type_base}")):
        fields_base = current_field_base.__dict__
        fields_new = current_field_new.__dict__
        fields_collection_name = "set of classes' fields"
    elif type_base == dict:
        fields_base = current_field_base
        fields_new = current_field_new
        fields_collection_name = "dictionaries"
    else:
        raise Exception(
            f"in path: {field_path}, unrecognized type: {type_base} (and type_new: {type_new}) (... is == type?: {type == type_base})")
    if keys is None:
        keys = list(fields_base.keys())
    if len(fields_base) != len(fields_new):
        error_text: list[str] = [
            f"in path: {field_path}, the {fields_collection_name} have different lengths: base = {len(fields_base)} ; new {len(fields_new)} :"
        ]
        if type_base == list:
            error_text.append(f"\t ({len(fields_base)}) base:")
            error_text.extend(f"\t - {x}" for x in fields_base)
            error_text.append(f"\t ({len(fields_new)}) new")
            error_text.extend(f"\t - {x}" for x in fields_new)
        else:
            error_text.append(f"\t ({len(fields_base)}) base:")
            error_text.extend(f"\t - {k}: {x}" for k, x in fields_base.items())
            error_text.append(f"\t ({len(fields_new)}) new")
            error_text.extend(f"\t - {k}: {x}" for k, x in fields_new.items())
        return ["\n".join(error_text)]
    # TODO finally, recursively iterate over the fields
    for k in keys:
        if are_keys_strings and (k not in fields_new):
            errors.append(
                f"in path: {field_path}, \\ the {index_field}-th key '{k}' in the base object is not present in the new object"
            )
        else:
            # RECURSION
            rec_field_path = k if field_path == "" else (
                f"{field_path}.{k}" if are_keys_strings else f"{field_path}[{k}]"
            )
            print(f"recursion in path {rec_field_path}")
            rec_errors: list[str] = check_differences(
                fields_base[k], fields_new[k],
                field_path=rec_field_path,
                field_path_filterer=field_path_filterer
            )
            if (rec_errors is not None) and (len(rec_errors) > 0):
                # there are errors -> collect them
                errors.extend(rec_errors)
        index_field += 1
        # field_path == ""
    if are_keys_strings:
        fields_new_keys: list[str] = list(fields_new.keys())
        fields_new_missing_in_base: list[tuple[str, int]] = [
            (fields_new_keys[i], i)
            for i in range(len(fields_new_keys))
            if fields_new_keys[i] not in fields_base
        ]
        if len(fields_new_missing_in_base) > 0:
            errors.extend(
                f"in path: {field_path}, / the {f_i[1]}-th key '{f_i[0]}' in the new object is not present in the base object"
                for f_i in fields_new_missing_in_base
            )
    # end
    return errors if len(errors) > 0 else None


def deep_copy(x, path=None):
    t = type(x)
    if path is None:
        path = ""
    if t in PRIMITIVE_TYPES:
        return x
    if t == list:
        return [
            deep_copy(x[i], f"{path}[{i}]")
            for i in range(len(x))
        ]
    dictionary: dict = None
    if t == type:
        dictionary = x.__dict__
    elif t == dict:
        dictionary = x
    else:
        raise Exception(f"In path '{path}', unexpected type to copy: {t}")
    return {
        k: deep_copy(dictionary[k], f"{path}.{k}")
        for k in dictionary.keys()
    }
