
class ModelConversionResultBase:
    """
    The base class of anything that is the result of a translation.
    """

    def get_id(self) -> str:
        return None

    def get_name(self):
        return ""

    def get_conversion_result(self):
        return None

    def __repr__(self):
        return ""
