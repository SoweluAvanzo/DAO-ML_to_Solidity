import src.pipeline.pipeline_item as pi
import src.validators.base_validator as bv


class JSONValidator(bv.BaseValidator):

    # TODO: deve ricevere un oggetto (JSON/dict) e verificare che rispetti il modello denro il model

    def validate(self, input_to_validate: dict) -> bool:
        raise Exception("TODO : NOT IMPLEMENTED YET (31-12-2025)")
