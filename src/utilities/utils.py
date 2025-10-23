import regex as re
import src.files.file_utils as fu


def is_string_or_list(t):
    if isinstance(t, list):
        return False
    elif isinstance(t, str):
        return True
    else:
        return None


def to_camel_case(s: str) -> str:
    parts = re.split(r'-|_', s)
    if len(parts) <= 1:
        return s
    return parts[0] + "".join(
        f"{str(p[0]).upper()}{p[1:]}" if len(p) > 1 else ''
        for p in parts[1:]
    )


def to_keyword(name: str) -> str:
    return fu.sanitize_filename(name).lower()
