
class ValidationResult:
    def __init__(self,
                 validation_result: bool = False,
                 errors: list[str] = None,
                 input_consumed: dict = None,
                 # input_string_list: list[str] = None,
                 additional_data=None
                 ):
        self.validation_result = validation_result
        self.errors = errors
        self.input_consumed = input_consumed
        self.additional_data = additional_data
