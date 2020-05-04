# Generated from Decaf.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete generic visitor for a parse tree produced by DecafParser.

class DecafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DecafParser#program.
    def visitProgram(self, ctx:DecafParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#var_id.
    def visitVar_id(self, ctx:DecafParser.Var_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#array_id.
    def visitArray_id(self, ctx:DecafParser.Array_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#equal_op.
    def visitEqual_op(self, ctx:DecafParser.Equal_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#if_kw.
    def visitIf_kw(self, ctx:DecafParser.If_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#else_kw.
    def visitElse_kw(self, ctx:DecafParser.Else_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#for_kw.
    def visitFor_kw(self, ctx:DecafParser.For_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#lround.
    def visitLround(self, ctx:DecafParser.LroundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#rround.
    def visitRround(self, ctx:DecafParser.RroundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#lcurly.
    def visitLcurly(self, ctx:DecafParser.LcurlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#rcurly.
    def visitRcurly(self, ctx:DecafParser.RcurlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#void.
    def visitVoid(self, ctx:DecafParser.VoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#not_sym.
    def visitNot_sym(self, ctx:DecafParser.Not_symContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#sub_sym.
    def visitSub_sym(self, ctx:DecafParser.Sub_symContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#return_kw.
    def visitReturn_kw(self, ctx:DecafParser.Return_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#callout_kw.
    def visitCallout_kw(self, ctx:DecafParser.Callout_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#break_kw.
    def visitBreak_kw(self, ctx:DecafParser.Break_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#class_kw.
    def visitClass_kw(self, ctx:DecafParser.Class_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#program_kw.
    def visitProgram_kw(self, ctx:DecafParser.Program_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#field_declr.
    def visitField_declr(self, ctx:DecafParser.Field_declrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#field_var.
    def visitField_var(self, ctx:DecafParser.Field_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_declr.
    def visitMethod_declr(self, ctx:DecafParser.Method_declrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#return_type.
    def visitReturn_type(self, ctx:DecafParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#block.
    def visitBlock(self, ctx:DecafParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#statement.
    def visitStatement(self, ctx:DecafParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#vardeclr.
    def visitVardeclr(self, ctx:DecafParser.VardeclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_call_inter.
    def visitMethod_call_inter(self, ctx:DecafParser.Method_call_interContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_call.
    def visitMethod_call(self, ctx:DecafParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#expr.
    def visitExpr(self, ctx:DecafParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#location.
    def visitLocation(self, ctx:DecafParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#callout_arg.
    def visitCallout_arg(self, ctx:DecafParser.Callout_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#int_literal.
    def visitInt_literal(self, ctx:DecafParser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#rel_op.
    def visitRel_op(self, ctx:DecafParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#eq_op.
    def visitEq_op(self, ctx:DecafParser.Eq_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cond_op.
    def visitCond_op(self, ctx:DecafParser.Cond_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#literal.
    def visitLiteral(self, ctx:DecafParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#bin_op.
    def visitBin_op(self, ctx:DecafParser.Bin_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arith_op.
    def visitArith_op(self, ctx:DecafParser.Arith_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#var_type.
    def visitVar_type(self, ctx:DecafParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#assign_op.
    def visitAssign_op(self, ctx:DecafParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_name.
    def visitMethod_name(self, ctx:DecafParser.Method_nameContext):
        return self.visitChildren(ctx)



del DecafParser