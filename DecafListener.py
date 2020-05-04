# Generated from Decaf.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete listener for a parse tree produced by DecafParser.
class DecafListener(ParseTreeListener):

    # Enter a parse tree produced by DecafParser#program.
    def enterProgram(self, ctx:DecafParser.ProgramContext):
        pass

    # Exit a parse tree produced by DecafParser#program.
    def exitProgram(self, ctx:DecafParser.ProgramContext):
        pass


    # Enter a parse tree produced by DecafParser#var_id.
    def enterVar_id(self, ctx:DecafParser.Var_idContext):
        pass

    # Exit a parse tree produced by DecafParser#var_id.
    def exitVar_id(self, ctx:DecafParser.Var_idContext):
        pass


    # Enter a parse tree produced by DecafParser#array_id.
    def enterArray_id(self, ctx:DecafParser.Array_idContext):
        pass

    # Exit a parse tree produced by DecafParser#array_id.
    def exitArray_id(self, ctx:DecafParser.Array_idContext):
        pass


    # Enter a parse tree produced by DecafParser#equal_op.
    def enterEqual_op(self, ctx:DecafParser.Equal_opContext):
        pass

    # Exit a parse tree produced by DecafParser#equal_op.
    def exitEqual_op(self, ctx:DecafParser.Equal_opContext):
        pass


    # Enter a parse tree produced by DecafParser#if_kw.
    def enterIf_kw(self, ctx:DecafParser.If_kwContext):
        pass

    # Exit a parse tree produced by DecafParser#if_kw.
    def exitIf_kw(self, ctx:DecafParser.If_kwContext):
        pass


    # Enter a parse tree produced by DecafParser#else_kw.
    def enterElse_kw(self, ctx:DecafParser.Else_kwContext):
        pass

    # Exit a parse tree produced by DecafParser#else_kw.
    def exitElse_kw(self, ctx:DecafParser.Else_kwContext):
        pass


    # Enter a parse tree produced by DecafParser#for_kw.
    def enterFor_kw(self, ctx:DecafParser.For_kwContext):
        pass

    # Exit a parse tree produced by DecafParser#for_kw.
    def exitFor_kw(self, ctx:DecafParser.For_kwContext):
        pass


    # Enter a parse tree produced by DecafParser#lround.
    def enterLround(self, ctx:DecafParser.LroundContext):
        pass

    # Exit a parse tree produced by DecafParser#lround.
    def exitLround(self, ctx:DecafParser.LroundContext):
        pass


    # Enter a parse tree produced by DecafParser#rround.
    def enterRround(self, ctx:DecafParser.RroundContext):
        pass

    # Exit a parse tree produced by DecafParser#rround.
    def exitRround(self, ctx:DecafParser.RroundContext):
        pass


    # Enter a parse tree produced by DecafParser#lcurly.
    def enterLcurly(self, ctx:DecafParser.LcurlyContext):
        pass

    # Exit a parse tree produced by DecafParser#lcurly.
    def exitLcurly(self, ctx:DecafParser.LcurlyContext):
        pass


    # Enter a parse tree produced by DecafParser#rcurly.
    def enterRcurly(self, ctx:DecafParser.RcurlyContext):
        pass

    # Exit a parse tree produced by DecafParser#rcurly.
    def exitRcurly(self, ctx:DecafParser.RcurlyContext):
        pass


    # Enter a parse tree produced by DecafParser#void.
    def enterVoid(self, ctx:DecafParser.VoidContext):
        pass

    # Exit a parse tree produced by DecafParser#void.
    def exitVoid(self, ctx:DecafParser.VoidContext):
        pass


    # Enter a parse tree produced by DecafParser#not_sym.
    def enterNot_sym(self, ctx:DecafParser.Not_symContext):
        pass

    # Exit a parse tree produced by DecafParser#not_sym.
    def exitNot_sym(self, ctx:DecafParser.Not_symContext):
        pass


    # Enter a parse tree produced by DecafParser#sub_sym.
    def enterSub_sym(self, ctx:DecafParser.Sub_symContext):
        pass

    # Exit a parse tree produced by DecafParser#sub_sym.
    def exitSub_sym(self, ctx:DecafParser.Sub_symContext):
        pass


    # Enter a parse tree produced by DecafParser#return_kw.
    def enterReturn_kw(self, ctx:DecafParser.Return_kwContext):
        pass

    # Exit a parse tree produced by DecafParser#return_kw.
    def exitReturn_kw(self, ctx:DecafParser.Return_kwContext):
        pass


    # Enter a parse tree produced by DecafParser#callout_kw.
    def enterCallout_kw(self, ctx:DecafParser.Callout_kwContext):
        pass

    # Exit a parse tree produced by DecafParser#callout_kw.
    def exitCallout_kw(self, ctx:DecafParser.Callout_kwContext):
        pass


    # Enter a parse tree produced by DecafParser#break_kw.
    def enterBreak_kw(self, ctx:DecafParser.Break_kwContext):
        pass

    # Exit a parse tree produced by DecafParser#break_kw.
    def exitBreak_kw(self, ctx:DecafParser.Break_kwContext):
        pass


    # Enter a parse tree produced by DecafParser#class_kw.
    def enterClass_kw(self, ctx:DecafParser.Class_kwContext):
        pass

    # Exit a parse tree produced by DecafParser#class_kw.
    def exitClass_kw(self, ctx:DecafParser.Class_kwContext):
        pass


    # Enter a parse tree produced by DecafParser#program_kw.
    def enterProgram_kw(self, ctx:DecafParser.Program_kwContext):
        pass

    # Exit a parse tree produced by DecafParser#program_kw.
    def exitProgram_kw(self, ctx:DecafParser.Program_kwContext):
        pass


    # Enter a parse tree produced by DecafParser#field_declr.
    def enterField_declr(self, ctx:DecafParser.Field_declrContext):
        pass

    # Exit a parse tree produced by DecafParser#field_declr.
    def exitField_declr(self, ctx:DecafParser.Field_declrContext):
        pass


    # Enter a parse tree produced by DecafParser#field_var.
    def enterField_var(self, ctx:DecafParser.Field_varContext):
        pass

    # Exit a parse tree produced by DecafParser#field_var.
    def exitField_var(self, ctx:DecafParser.Field_varContext):
        pass


    # Enter a parse tree produced by DecafParser#method_declr.
    def enterMethod_declr(self, ctx:DecafParser.Method_declrContext):
        pass

    # Exit a parse tree produced by DecafParser#method_declr.
    def exitMethod_declr(self, ctx:DecafParser.Method_declrContext):
        pass


    # Enter a parse tree produced by DecafParser#return_type.
    def enterReturn_type(self, ctx:DecafParser.Return_typeContext):
        pass

    # Exit a parse tree produced by DecafParser#return_type.
    def exitReturn_type(self, ctx:DecafParser.Return_typeContext):
        pass


    # Enter a parse tree produced by DecafParser#block.
    def enterBlock(self, ctx:DecafParser.BlockContext):
        pass

    # Exit a parse tree produced by DecafParser#block.
    def exitBlock(self, ctx:DecafParser.BlockContext):
        pass


    # Enter a parse tree produced by DecafParser#statement.
    def enterStatement(self, ctx:DecafParser.StatementContext):
        pass

    # Exit a parse tree produced by DecafParser#statement.
    def exitStatement(self, ctx:DecafParser.StatementContext):
        pass


    # Enter a parse tree produced by DecafParser#vardeclr.
    def enterVardeclr(self, ctx:DecafParser.VardeclrContext):
        pass

    # Exit a parse tree produced by DecafParser#vardeclr.
    def exitVardeclr(self, ctx:DecafParser.VardeclrContext):
        pass


    # Enter a parse tree produced by DecafParser#method_call_inter.
    def enterMethod_call_inter(self, ctx:DecafParser.Method_call_interContext):
        pass

    # Exit a parse tree produced by DecafParser#method_call_inter.
    def exitMethod_call_inter(self, ctx:DecafParser.Method_call_interContext):
        pass


    # Enter a parse tree produced by DecafParser#method_call.
    def enterMethod_call(self, ctx:DecafParser.Method_callContext):
        pass

    # Exit a parse tree produced by DecafParser#method_call.
    def exitMethod_call(self, ctx:DecafParser.Method_callContext):
        pass


    # Enter a parse tree produced by DecafParser#expr.
    def enterExpr(self, ctx:DecafParser.ExprContext):
        pass

    # Exit a parse tree produced by DecafParser#expr.
    def exitExpr(self, ctx:DecafParser.ExprContext):
        pass


    # Enter a parse tree produced by DecafParser#location.
    def enterLocation(self, ctx:DecafParser.LocationContext):
        pass

    # Exit a parse tree produced by DecafParser#location.
    def exitLocation(self, ctx:DecafParser.LocationContext):
        pass


    # Enter a parse tree produced by DecafParser#callout_arg.
    def enterCallout_arg(self, ctx:DecafParser.Callout_argContext):
        pass

    # Exit a parse tree produced by DecafParser#callout_arg.
    def exitCallout_arg(self, ctx:DecafParser.Callout_argContext):
        pass


    # Enter a parse tree produced by DecafParser#int_literal.
    def enterInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#int_literal.
    def exitInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#rel_op.
    def enterRel_op(self, ctx:DecafParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DecafParser#rel_op.
    def exitRel_op(self, ctx:DecafParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DecafParser#eq_op.
    def enterEq_op(self, ctx:DecafParser.Eq_opContext):
        pass

    # Exit a parse tree produced by DecafParser#eq_op.
    def exitEq_op(self, ctx:DecafParser.Eq_opContext):
        pass


    # Enter a parse tree produced by DecafParser#cond_op.
    def enterCond_op(self, ctx:DecafParser.Cond_opContext):
        pass

    # Exit a parse tree produced by DecafParser#cond_op.
    def exitCond_op(self, ctx:DecafParser.Cond_opContext):
        pass


    # Enter a parse tree produced by DecafParser#literal.
    def enterLiteral(self, ctx:DecafParser.LiteralContext):
        pass

    # Exit a parse tree produced by DecafParser#literal.
    def exitLiteral(self, ctx:DecafParser.LiteralContext):
        pass


    # Enter a parse tree produced by DecafParser#bin_op.
    def enterBin_op(self, ctx:DecafParser.Bin_opContext):
        pass

    # Exit a parse tree produced by DecafParser#bin_op.
    def exitBin_op(self, ctx:DecafParser.Bin_opContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op.
    def enterArith_op(self, ctx:DecafParser.Arith_opContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op.
    def exitArith_op(self, ctx:DecafParser.Arith_opContext):
        pass


    # Enter a parse tree produced by DecafParser#var_type.
    def enterVar_type(self, ctx:DecafParser.Var_typeContext):
        pass

    # Exit a parse tree produced by DecafParser#var_type.
    def exitVar_type(self, ctx:DecafParser.Var_typeContext):
        pass


    # Enter a parse tree produced by DecafParser#assign_op.
    def enterAssign_op(self, ctx:DecafParser.Assign_opContext):
        pass

    # Exit a parse tree produced by DecafParser#assign_op.
    def exitAssign_op(self, ctx:DecafParser.Assign_opContext):
        pass


    # Enter a parse tree produced by DecafParser#method_name.
    def enterMethod_name(self, ctx:DecafParser.Method_nameContext):
        pass

    # Exit a parse tree produced by DecafParser#method_name.
    def exitMethod_name(self, ctx:DecafParser.Method_nameContext):
        pass


