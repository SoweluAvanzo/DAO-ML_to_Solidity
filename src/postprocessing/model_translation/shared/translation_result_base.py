
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

    def can_be_outputted(self) -> bool:
        return True  # default

    def __repr__(self):
        return ""
