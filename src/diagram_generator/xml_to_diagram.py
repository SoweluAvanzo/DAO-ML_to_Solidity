import xmlschema

# NOTE: takes an XMLInput as InputBase and returns a DiagramManager instance
# must invoke the xml parser we already have impemented


from src.model.diagram_manager import DiagramManager
from src.input.input_base import InputBase
from src.input.xml_file_input import TextFileInputXML
from src.diagram_generator.diagram_generator_base import DiagramGeneratorBase

# @deprecated
class XMLDiagramGenerator(DiagramGeneratorBase):
    def __init__(self, xml_schema:str|xmlschema.XMLSchema):
        self.xml_schema = None
        self.set_xml_schema(xml_schema)

    def set_xml_schema(self, xml_schema):
        self.xml_schema = xmlschema.XMLSchema(xml_schema) if isinstance(xml_schema, str) else xml_schema

    def generate(self, input:InputBase) -> DiagramManager:
        # INVOCARE QUI IL PARSER0
        if not isinstance(input, TextFileInputXML):
            raise TypeError(f"The provided Input to generate the XML-based diagram is no an isntace of {type(input).__name__}")



        # invocare il file "validators/xml_dao_validator"
