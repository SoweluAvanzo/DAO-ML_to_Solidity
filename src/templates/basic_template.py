import src.output.output_manager as om
import src.model.diagram_manager as dm

class BasicTemplate:
    def __init__(self, template_name="", filename=""):
        self.template_name = template_name
        self.filename = filename

    def render(self, diagram_manager:dm.DiagramManager, data=None, output_manager:om.OutputManager=None):
        pass
    
    def generate_default_fields(self, diagram_manager:dm.DiagramManager, data=None):
        return ""
    
    def generate_default_modifiers(self, diagram_manager:dm.DiagramManager, data=None):
        return ""
    
    def generate_default_constructor_parameters(self, diagram_manager:dm.DiagramManager, data=None):
        return ""
    
    def generate_default_constructor_body(self, diagram_manager:dm.DiagramManager, data=None, comma_required=False):
        return ""
    
    def generate_default_private_methods(self, diagram_manager:dm.DiagramManager, data=None):
        return ""
    
    def generate_default_public_methods(self, diagram_manager:dm.DiagramManager, data=None):
        return ""
    