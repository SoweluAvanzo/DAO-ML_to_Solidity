import sys

if __name__ is not None and "." in __name__:
    from .XMLLexer import XMLLexer
    from .XMLParser import XMLParser
    from .XMLParserVisitor import XMLParserVisitor
else:
    from XMLLexer import XMLLexer
    from XMLParser import XMLParser
from parse_xml import*
from translator import*

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = XMLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XMLParser(stream)
    tree = parser.document()

    visitor = DAO_ML_Visitor()
    traverse(tree, parser.ruleNames, 0)
    visitor.visit(tree)
    

    print("\n -----PRINTING VISITOR CONTENT----")
    print(visitor)
    print("\n -----PRINTING VISITOR CONTENT----")


if __name__ == '__main__':
    main(sys.argv)