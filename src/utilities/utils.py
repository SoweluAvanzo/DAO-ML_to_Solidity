import regex as re
import src.files.file_utils as fu
import src.utilities.errors as e_c


class ToStringable:
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
        return f"{'{'} {field_spacer.join(f"{k}: {v.to_string() if isinstance(v, ToStringable) else v}" for k, v in self.__dict__.items())} {'}'}"

    def __str__(self):
        return self.to_string(indent=2)


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
