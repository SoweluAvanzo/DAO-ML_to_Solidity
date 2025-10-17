from enum import Enum


class TranslationTypesSolidity(Enum):
    SIMPLE = "simple"
    # should we distinguish between Jinja template and "line by line"?
    OPTIMIZED = "optimized"
    DIAMOND = "diamond"
    # others?
