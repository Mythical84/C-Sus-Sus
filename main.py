import CsusLexer, CsusParser, Visitor
from antlr4 import InputStream, CommonTokenStream

text = '''
print();
'''

chars = InputStream(text)
lexer = CsusLexer.CsusLexer(chars)
tokens = CommonTokenStream(lexer)
parser = CsusParser.CsusParser(tokens)

parser.buildParseTrees = True
tree = parser.csus()
visitor = Visitor.Visitor()
answer = visitor.visit(tree)
