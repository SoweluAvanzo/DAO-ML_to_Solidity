import src.utilities.extended_enum as e_enum


class TranslationTypes(e_enum.ExtendedEnum):
    """
    Defines both the available translation types (except for Petri Nets, currently 2026-02-15)
    and the foldername of some resources (like, file output, or folder of templates).
    """
    SOLIDITY = "sol"
    ASM = "asm"
    TESTS_SOLIDITY = "tests_sol"
    PETRI_NETS = "petri"
    # there's a PetriNet-like graph representation modelling the flow's elements of a graph, which I don't remember the name
    # others?
