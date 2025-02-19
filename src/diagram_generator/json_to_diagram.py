import json

from src.model.diagram_manager import DiagramManager
from src.input.input_base import InputBase
from src.diagram_generator.diagram_generator_base import DiagramGeneratorBase

class JSONDiagramGenerator(DiagramGeneratorBase):
    
    def generate(self, input:InputBase) -> DiagramManager:
        # TODO: is something more comple needed?
        # Example: run "class"/instances checks
        return json.loads(input.get_input())
        