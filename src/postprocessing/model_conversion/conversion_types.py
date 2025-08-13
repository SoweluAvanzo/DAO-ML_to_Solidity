from enum import Enum

class ConversionTypes(Enum):
    SOLIDITY = 1
    ASM = 2
    PETRI_NETS = 3
    # there's a PetriNet-like graph representation modelling the flow's elements of a graph, which I don't remember the name
    # others?
