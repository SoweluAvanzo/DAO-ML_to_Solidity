
def check_differences(current_field_base, current_field_new, field_path: str = None) -> list[str]:
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
        ((type == type_base) or (type == type_new))
        and (type_base.__name__ != type_new.__name__)
    ):
        return [
            f"Type mismatch: << base = {type_base} >> ; << new = {type_new} >>"
        ]
    errors: list[str] = []
    # types should be equal ...
    if type_base in (bool, str, int, float):
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
    elif type_base == type:
        fields_base = current_field_base.__dict__
        fields_new = current_field_new.__dict__
        fields_collection_name = "set of classes' fields"
    elif type_base == dict:
        fields_base = current_field_base
        fields_new = current_field_new
        fields_collection_name = "dictionaries"
    if keys is None:
        keys = list(fields_base.keys())
    if len(fields_base) != len(fields_new):
        raise Exception(
            f"in path: {field_path}, the {fields_collection_name} have different lengths: base = {len(fields_base)} ; new {len(fields_new)}")
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
            rec_errors: list[str] = check_differences(
                fields_base[k], fields_new[k], rec_field_path
            )
            if (rec_errors is not None) and (len(rec_errors) > 0):
                # there are errors -> collect them
                errors.extend(rec_errors)
        index_field += 1
        # field_path == ""
    if are_keys_strings:
        fields_new_missing_in_base: list[str] = [
            k
            for k in fields_new.keys()
            if k not in fields_base
        ]
        if len(fields_new_missing_in_base) > 0:
            errors.extend(
                f"in path: {field_path}, / the {i}-th key '{fields_new_missing_in_base[i]}' in the new object is not present in the base object"
                for i in range(len(fields_new_missing_in_base))
            )
    # end
    return errors if len(errors) > 0 else None
