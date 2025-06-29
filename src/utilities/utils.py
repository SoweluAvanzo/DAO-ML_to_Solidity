
def is_string_or_list(t):
    if isinstance(t, list):
        return False
    elif isinstance(t, str):
        return True
    else:
        return None