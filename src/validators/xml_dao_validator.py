
import src.validators.base_validator as bv
import src.pipeline.pipeline_item as pi

class XMLDaoValidator(bv.ValidatorBase):
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)
    
    def validate(self, input:any) -> bool:
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

        return False
