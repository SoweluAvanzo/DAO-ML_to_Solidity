import src.utilities.extended_enum as ext_enum


class RelationType(ext_enum.ExtendedEnum):
    ASSOCIATION = 1
    CONTROL = 2
    AGGREGATION = 3
    FEDERATION = 4
