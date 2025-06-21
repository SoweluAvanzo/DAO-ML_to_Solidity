# NOTE: takes an XMLInput as InputBase and returns a DiagramManager instance
# must invoke the xml parser we already have impemented
from src.model.diagram_manager import DiagramManager
from src.input.input_base import InputBase

# una delle classi più importanti: preleva un Input e lo trasforma producendo un DiagramManager
class DiagramGeneratorBase:
    def generate(self, input:InputBase) -> DiagramManager:
        raise Exception("Not implemented yet")
