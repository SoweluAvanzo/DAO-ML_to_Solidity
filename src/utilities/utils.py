import regex as re
import src.files.file_utils as fu
import types
from typing import Generator


def is_string_or_list(t):
    if isinstance(t, str):
        return True
    elif isinstance(t, list):
        return False
    else:
        return None


def is_generator(obj):
    t = type(obj)
    return isinstance(obj, Generator) or t == Generator or \
        isinstance(obj, types.GeneratorType) or t == types.GeneratorType


def to_camel_case(s: str) -> str:
    parts = re.split(r'-|_', s)
    if len(parts) <= 1:
        return s
    return parts[0] + "".join(
        f"{str(p[0]).upper()}{p[1:]}" if len(p) > 1 else ''
        for p in parts[1:]
    )


def to_keyword(name: str, to_lower=True) -> str:
    sanitized_name: str = fu.sanitize_filename(name)
    return sanitized_name.lower() if to_lower else sanitized_name


#

ERRORS_KEYS = [
    "errors",
    "is_error",
    "is_exception",
    "exception"
]


class PrinterDebug:

    def print_msg(self, msg: str):
        """
        Overridable
        """
        print(msg)

    def print_error(self, msg):
        """
        Overridable
        """
        print(msg)

    def __call__(self, *args, **kwds):
        for err_keyword in ERRORS_KEYS:
            if err_keyword in kwds:
                self.print_error(args[0])
                return
        self.print_msg(args[0])


class MultiPrinterDebug(PrinterDebug):
    def __init__(self, delegators: list[PrinterDebug]):
        super().__init__()
        if (delegators is None) or (len(delegators) <= 0):
            raise Exception("No delegators provided")
        self.__delegators = delegators

    def print_msg(self, msg: str):
        for d in self.__delegators:
            d.print_msg(msg)

    def print_error(self, msg):
        for d in self.__delegators:
            d.print_error(msg)
