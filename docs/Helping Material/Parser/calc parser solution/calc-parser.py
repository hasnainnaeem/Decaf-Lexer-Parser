import antlr4 as ant
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcVisitor import CalcVisitor


class CalcPrintVisitor(CalcVisitor):
    def __init__(self):
        super().__init__()
        self.text = ""

    def printNode(self, ctx):
        self.text = self.text + '{\"name\": \"' + parser.ruleNames[
            ctx.getRuleIndex()] + '\",' + '\"value\":2,' + '\"children\":['
        self.visitChildren(ctx)
        self.text = self.text + ']},'

    def visitTerminal(self, ctx):
        self.text = self.text + '{\"name\": \"' + ctx.getText().replace('\\', '\\\\').replace('\"', '\\\"') + '\"},'

    # visit parse tree produced by CalcParser#calculator
    def visitCalculator(self, ctx: CalcParser.CalculatorContext):
        self.printNode(ctx)

    # visit parse tree produced by CalcParser#expr
    def visitExpr(self, ctx: CalcParser.ExprContext):
        self.printNode(ctx)

    # visit parse tree produced by CalcParser#op
    def visitOp(self, ctx: CalcParser.OpContext):
        self.printNode(ctx)


filein = open('testdata/test_08.calc', 'r')
lexer = CalcLexer(ant.InputStream(filein.read()))

# create a token stream from the lexer
stream = ant.CommonTokenStream(lexer)

# create a new parser with the token stream as input
parser = CalcParser(stream)
tree = parser.calculator()

# create a new calc visitor
visitor = CalcPrintVisitor()
visitor.visit(tree)
print(visitor.text)
