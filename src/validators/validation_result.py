
class ValidationResult:
    def __init__(self,
                 validation_result: bool = False,
                 errors: list[str] = None,
                 input: dict = None,
                 input_string_list: list[str] = None,
                 additional_data=None
                 ):
        self.validation_result = validation_result
        self.errors = errors
        self.input = input
        self.input_string_list = input_string_list
        self.additional_data = additional_data
