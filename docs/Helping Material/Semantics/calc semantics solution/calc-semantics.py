import antlr4 as ant
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcVisitor import CalcVisitor
import SymbolTable

class CalcSemanticVisitor(CalcVisitor):
    def __init__(self):
        super().__init__()
        self.st = SymbolTable.SymbolTable()
        self.st.enterScope()

    def visitCalculator(self, ctx:CalcParser.CalculatorContext):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx:CalcParser.ExprContext):
        if ctx.VAR():
            id = ctx.VAR().getText()
            if (self.st.lookup(id) == None):
                print('error on line', ctx.start.line, ': VAR(', id, ') not declared before use')
        return self.visitChildren(ctx)

    def visitStatement(self, ctx:CalcParser.StatementContext):
        id = ctx.VAR().getText()
        if (self.st.lookup(id) != None):
            print('error on line', ctx.start.line, ': VAR(', id, ') redeclared in same scope')
        self.st.addSymbol(SymbolTable.VarSymbol(id=id, type=-1, line=ctx.start.line, size=1))
        return self.visitChildren(ctx)

filein = open('testdata/test_11.calc', 'r')
lexer = CalcLexer(ant.InputStream(filein.read()))

#create a token stream from the lexer
stream = ant.CommonTokenStream(lexer)

#create a new parser with the token stream as input
parser = CalcParser(stream)
tree = parser.calculator()

#create a new calc visitor
semanticvisitor = CalcSemanticVisitor()
semanticvisitor.visit(tree)
