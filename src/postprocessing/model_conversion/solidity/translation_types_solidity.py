from enum import Enum

class TranslationTypesSolidity(Enum):
    SIMPLE = 1
    OPTIMIZED = 2 # should we distinguish between Jinja template and "line by line"?
    DIAMOND = 3
    # others?