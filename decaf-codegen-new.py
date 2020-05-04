import antlr4 as ant
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafVisitor import DecafVisitor
import SymbolTable

class DecafCodeGenVisitor(DecafVisitor):
    def __init__(self):
        super().__init__()
        #1. create a new symbol table
        #2. initialise the assembly code head
        #3. initialise the assembly code body

    def visitProgram(self, ctx:DecafParser.ProgramContext):
        #enters a new scope, visits all child nodes, then exits the scope
        self.st.enterScope()
        return_val = self.visitChildren(ctx)
        self.st.exitScope()
        return return_val

    def visitMethod_decl(self, ctx:DecafParser.Method_declContext):
        #1. build upon your semantic analysis solution, to add symbol details like memory location
        #2. add method label to assembly body
        #3. visit all child nodes
        #4. add return instruction to assembly body
        return self.visitChildren(ctx)

    def visitField_decl(self, ctx:DecafParser.Field_declContext):
        #1. get global field data (field_name, type, line number)
        #2. set memory type
        #3. loop over all fields in list, creating symbols, adding each symbol to the symbol table
        return self.visitChildren(ctx)

    def visitExpr(self, ctx:DecafParser.ExprContext):
        #1. recognise expression type (minimal example below)
        #2. write code generation procedure for each special case
        if ctx.location():
            pass
        elif ctx.literal():
            pass
        elif ctx.expr():
            pass

    def visitStatement(self, ctx:DecafParser.StatementContext):
        #1. recognise statement type (minimal example below)
        #2. write code generation procedure for each special case
        if ctx.assign_op():
            pass

#open a dcf source file to analyse and generate code from
filein = open('my_test_file.dcf', 'r')
lexer = DecafLexer(ant.InputStream(filein.read()))

#create a token stream from the lexer
stream = ant.CommonTokenStream(lexer)

#create a new parser with the token stream as input
parser = DecafParser(stream)
tree = parser.program()

#create a new calc visitor
treevisitor = DecafCodeGenVisitor()
treevisitor.visit(tree)

#print the generated assembly code
print(treevisitor.head+treevisitor.body)
