import json

from src.diagram_generator.diagram_generator_base import DiagramGeneratorBase
from src.input.input_base import InputBase
from src.model.diagram_manager import DiagramManager
from src.model.dao import DAO

class JSONDiagramGenerator(DiagramGeneratorBase):
    
    def generate(self, input:InputBase) -> DiagramManager:
        # TODO: is something more comple needed?
        # Example: run "class"/instances checks
        # 2025-04-06 YES: a validator is needed: runs through the loaded object to instantiate a "DiagramManager"
        obj = json.loads(input.get_input())
        return self.generate_diagram_from(obj)

    def generate_diagram_from(self, apparently_diagram_json: dict[str, any]):
        # TODO
        return apparently_diagram_json
    
    def generate_DAO_from(self, apparently_diagram_json: dict[str, any]) -> DAO:
        # TODO
        return None
    # TODO EVERYTHING ELSE ....