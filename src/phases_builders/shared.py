
import src.phases_builders.phases as phases

import src.phases_builders.phase_step_variants as psv

import src.utilities.errors as e_c


class PersistanceType(psv.PhaseSubstepVariants):
    FILE = "file"
    # PROGRAMMATIC_PROVIDER = "prog" # an external / runtine source, like constants or the value returned by a provider (or in-memory DB / map/dict)
    DATABASE = "db"

    # API="api" # of any kind: calling an HTTP API method, a WebSocket, an RSS-Feed, etc


REVERSE_MAPPING_PersistanceType = {
    v.value: v for v in PersistanceType}


class ModelPersistanceFormat(psv.PhaseSubstepVariants):
    XML = "xml"
    JSON = "json"
    # YAML="yaml"
    # BSON = "bson"
    # BINARY = "bytes"


REVERSE_MAPPING_ModelPersistanceFormat = {
    v.value: v for v in ModelPersistanceFormat}

#


class AdditionalDataSubPhase:
    def __init__(self, phase_step_variant: psv.PhaseSubstepVariants):
        if not isinstance(phase_step_variant, psv.PhaseSubstepVariants):
            raise Exception(
                f"Provided phase_step_variant is not an instance of PhaseSubstepVariants: {type(phase_step_variant)}")
        self.phase_step_variant = phase_step_variant


class PhaseVariantsAndData:
    def __init__(self, phase: phases.TranslationPhases):
        if not isinstance(phase, phases.TranslationPhases):
            raise Exception(
                f"Provided phase is not an instance of TranslationPhases: {type(phase)}")
        self.phase = phase
        self.phase_variant_data_by_pv_name: dict[str, AdditionalDataSubPhase] = {
        }

    def add_phase_variant_data(self, phase_step_variant_data: AdditionalDataSubPhase):
        if not isinstance(phase_step_variant_data, AdditionalDataSubPhase):
            raise Exception(
                f"Provided phase_step_variant_data is not an instance of AdditionalDataSubPhase: {type(phase_step_variant_data)}")
        self.phase_variant_data_by_pv_name[phase_step_variant_data.phase_step_variant.name] = phase_step_variant_data
        return True

    def add_phase_variant_and_data(self, phase_step_variant: psv.PhaseSubstepVariants, additional_data: dict = None):
        return self.add_phase_variant_data(AdditionalDataSubPhase(phase_step_variant, additional_data=additional_data))

#


class KeyUniqueProducer:
    def new_unique_key(self) -> str:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)


class KeyUniqueProducerSimpleSequential:
    """
    WARNING: no thread-safety implemented!
    """

    def __init__(self):
        self.counter = 0

    def new_unique_key(self) -> str:
        c = self.counter
        self.counter += 1
        return f"key_{c}"


#
