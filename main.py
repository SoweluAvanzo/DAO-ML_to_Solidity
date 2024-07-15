import sys

# import parse_xml
from .xml_grammar.DAO_XML_lexer import serializedATN

def main(argv):
    '''
    input_stream = sys.FileStream(argv[1])
    lexer = DAO_XML_lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XMLParser(stream)
    tree = parser.document()

    visitor = DAO_ML_Visitor()
    traverse(tree, parser.ruleNames, 0)
    visitor.visit(tree)
    
    print(visitor)
    '''

    a = serializedATN()
    print(len(a))



if __name__ == '__main__':
    main(sys.argv)
