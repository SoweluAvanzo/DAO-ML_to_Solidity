# NOTE: takes an XMLInput as InputBase and returns a DiagramManager instance
# must invoke the xml parser we already have impemented


from src.model.diagram_manager import DiagramManager
from src.input.input_base import InputBase
from src.diagram_generator.diagram_generator_base import DiagramGeneratorBase

class XMLDiagramGenerator(DiagramGeneratorBase):
    
    def generate(self, input:InputBase) -> DiagramManager:
        # INVOCARE QUI IL PARSER0
        