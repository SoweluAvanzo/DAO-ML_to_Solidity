import src.utilities.extended_enum as ex_enum


class TranslationPhases(ex_enum.ExtendedEnum):
    INPUT_FETCHING = "input"
    MODEL_GENERATION = "model"
    TRANSLATION_CONVERSION_POSTPROCESSING = "post"
    OUTPUT = "output"


def str_to_phase(s: str) -> TranslationPhases:
    return TranslationPhases[s]
