import src.utilities.extended_enum as ee


class TranslationTypesSolidity(ee.ExtendedEnum):
    SIMPLE = "simple"
    # should we distinguish between Jinja template and "line by line"?
    OPTIMIZED = "optimized"
    DIAMOND = "diamond"
    # others?
