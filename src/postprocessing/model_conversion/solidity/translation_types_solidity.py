from enum import Enum

class TranslationTypesSolidity(Enum):
    SIMPLE = "simple"
    OPTIMIZED = "optimized" # should we distinguish between Jinja template and "line by line"?
    DIAMOND = "diamond"
    # others?