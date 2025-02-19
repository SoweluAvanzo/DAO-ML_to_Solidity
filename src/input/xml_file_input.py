
from src.input.txt_file_input import TextFileInput

class TextFileInputXML(TextFileInput):
    def __init__(self, filepath, xml_version="1.0"):
        super().__init__(filepath)
        self.xml_version = xml_version
        # TODO: altro?
    




    
        condition_validator = ConstraintValidator(xml_file, "data/XSD_DAO_ML.xsd")
        condition_validator.validate_dao_ml_diagram()
        input_stream = FileStream(xml_file)
        lexer = XMLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = XMLParser(stream)
        tree = parser.document()

        visitor = DAOVisitor2()

        # PARTE 2) Dato l'input, CREARE ISTANZA DI "DiagramManager"
        diagram_manager = DiagramManager()
        visitor.parseDiagramTree(tree, diagram_manager)