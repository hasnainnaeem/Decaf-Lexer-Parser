import os
import antlr4 as ant
from SymbolTable import SymbolTable, VarSymbol, MethodSymbol

os.system("java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Decaf.g4 -visitor")

from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafVisitor import DecafVisitor

class DecafCodeGenVisitor(DecafVisitor):
    def __init__(self):
        super().__init__()
        self.st = SymbolTable()
        self.head = '.data\n'
        self.body = '.global main\n'

source = 'testdata/codegen/00-empty'
filein = open(source + '.dcf', 'r')
lexer = DecafLexer(ant.InputStream(filein.read()))

#create a token stream from the lexer
stream = ant.CommonTokenStream(lexer)

#create a new parser with the token stream as input
parser = DecafParser(stream)
tree = parser.program()

#create a new calc visitor
codegen_visitor = DecafCodeGenVisitor()
codegen_visitor.visit(tree)

#output code
code = codegen_visitor.head + codegen_visitor.body
print(code)