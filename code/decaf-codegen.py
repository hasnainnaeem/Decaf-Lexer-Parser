import os
import antlr4 as ant
from SymbolTable import SymbolTable, VarSymbol, MethodSymbol

os.system("java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Decaf.g4 -visitor")

from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafVisitor import DecafVisitor

def raiseErr(message, ctx):
    print("Error on line " + str(ctx.start.line) + ": " + message + "\n")

    exit(1)

class DecafCodeGenVisitor(DecafVisitor):
    def __init__(self):
        super().__init__()
        self.st = SymbolTable()
        self.head = '.data\n'
        self.body = '.global main\n'

    def visitProgram(self, ctx:DecafParser.ProgramContext):
        #enters a new scope, visits all child nodes, then exits the scope
        self.st.enterScope()
        return_val = self.visitChildren(ctx)
        self.st.exitScope()
        return return_val

    # Visit a parse tree produced by DecafParser#var_id.
    def visitVar_id(self, ctx: DecafParser.Var_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#array_id.
    def visitArray_id(self, ctx: DecafParser.Array_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#field_declr.
    def visitField_declr(self, ctx: DecafParser.Field_declrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#field_var.
    def visitField_var(self, ctx: DecafParser.Field_varContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#method_declr.
    def visitMethod_declr(self, ctx: DecafParser.Method_declrContext):

        methodtype =  ctx.getChild(0).getChild(0)
        methodid =  ctx.getChild(1).getChild(0)
        #methodparams = ctx.getChild(4).getChild(0)
        self.st.addSymbol(MethodSymbol(methodid, methodtype, 0, ""))
        self.body += "\n" + str(methodid) + ":\n"
        retval =  self.visitChildren(ctx)
        self.body += "\nret\n"
        return retval

    # Visit a parse tree produced by DecafParser#return_type.
    def visitReturn_type(self, ctx: DecafParser.Return_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#block.
    def visitBlock(self, ctx: DecafParser.BlockContext):
        self.st.enterScope()
        return_val = self.visitChildren(ctx)
        self.st.exitScope()
        return return_val

    def visitStatement(self, ctx:DecafParser.StatementContext):
        #1. recognise statement type (minimal example below)
        #2. write code generation procedure for each special case
        if ctx.assign_op():
            pass

    # Visit a parse tree produced by DecafParser#vardeclr.
    def visitVardeclr(self, ctx: DecafParser.VardeclrContext):
        vtype = None
        vid = None
        for i in ctx.children:
            tkn = i.getText() 
            if tkn == 'int' or tkn == 'boolean':
                vtype = tkn
            elif tkn == ',' or tkn  == ';':
                continue
            elif tkn != None:
                vid = tkn
                if self.st.probe(vid) != None:
                    raiseErr("Variable " + vid + " already declared in scope.", ctx)
                
                self.st.addSymbol(VarSymbol(vid, vtype, 0, 8, 0))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#method_call_inter.
    def visitMethod_call_inter(self, ctx: DecafParser.Method_call_interContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#method_call.
    def visitMethod_call(self, ctx: DecafParser.Method_callContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#expr.
    def visitExpr(self, ctx: DecafParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#location.
    def visitLocation(self, ctx: DecafParser.LocationContext):
        vid = str(ctx.getChild(0).getChild(0))
        if self.st.lookup(vid) == None:
            raiseErr("Variable " + vid + " not declared.", ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#callout_arg.
    def visitCallout_arg(self, ctx: DecafParser.Callout_argContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#int_literal.
    def visitInt_literal(self, ctx: DecafParser.Int_literalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#rel_op.
    def visitRel_op(self, ctx: DecafParser.Rel_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#eq_op.
    def visitEq_op(self, ctx: DecafParser.Eq_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#cond_op.
    def visitCond_op(self, ctx: DecafParser.Cond_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#literal.
    def visitLiteral(self, ctx: DecafParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#bin_op.
    def visitBin_op(self, ctx: DecafParser.Bin_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#arith_op.
    def visitArith_op(self, ctx: DecafParser.Arith_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#var_type.
    def visitVar_type(self, ctx: DecafParser.Var_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#assign_op.
    def visitAssign_op(self, ctx: DecafParser.Assign_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#method_name.
    def visitMethod_name(self, ctx: DecafParser.Method_nameContext):
      #  self.st.addSymbol(MethodSymbol(ctx.getChild(0))
        return_val = self.visitChildren(ctx)


        return return_val

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
