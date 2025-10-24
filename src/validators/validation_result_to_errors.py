import src.pipeline.pipeline_item as pi

import src.validators.validation_result as validation_res


class ValidationResultToErrorsExtractor(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, key_validation_result: str = None):
        super().__init__(pipeline_item_data)
        self.key_validation_result = key_validation_result

    def run(self, inputs):
        err_validation = inputs[self.key_validation_result] if ((self.key_validation_result is not None) and (
            self.key_validation_result in inputs)) else self.get_ith_input(inputs, 0)
        if err_validation is None:
            return None
        if not isinstance(err_validation, validation_res.ValidationResult):
            err_text = f"Given error validation is not of ValidationResult type: {type(err_validation)}"
            print(err_text)
            return err_text
        errs = err_validation.errors
        print(
            f"validation results validation_result: {err_validation.validation_result}")
        print(f"validation results errors: {err_validation.errors}")
        print(f"validation results input: {err_validation.input}")
        return errs

    def repr_inner(self):
        return f"\"key_validation_result\":{self.key_validation_result}"
