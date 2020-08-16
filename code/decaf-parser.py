import os
import antlr4 as ant
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafVisitor import DecafVisitor
import re

os.system("java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Decaf.g4 -visitor")


class CalcPrintVisitor(DecafVisitor):
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

    # Visit a parse tree produced by DecafParser#program.
    def visitProgram(self, ctx:DecafParser.ProgramContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#vardeclr.
    def visitVardeclr(self, ctx:DecafParser.VardeclrContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#field_declr.
    def visitField_declr(self, ctx:DecafParser.Field_declrContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#array_id.
    def visitArray_id(self, ctx:DecafParser.Array_idContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#field_var.
    def visitField_var(self, ctx:DecafParser.Field_varContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#var_id.
    def visitVar_id(self, ctx:DecafParser.Var_idContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#method_declr.
    def visitMethod_declr(self, ctx:DecafParser.Method_declrContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#return_type.
    def visitReturn_type(self, ctx:DecafParser.Return_typeContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#block.
    def visitBlock(self, ctx:DecafParser.BlockContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#statement.
    def visitStatement(self, ctx:DecafParser.StatementContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#method_call_inter.
    def visitMethod_call_inter(self, ctx:DecafParser.Method_call_interContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#method_call.
    def visitMethod_call(self, ctx:DecafParser.Method_callContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#expr.
    def visitExpr(self, ctx:DecafParser.ExprContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#location.
    def visitLocation(self, ctx:DecafParser.LocationContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#callout_arg.
    def visitCallout_arg(self, ctx:DecafParser.Callout_argContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#int_literal.
    def visitInt_literal(self, ctx:DecafParser.Int_literalContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#rel_op.
    def visitRel_op(self, ctx:DecafParser.Rel_opContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#eq_op.
    def visitEq_op(self, ctx:DecafParser.Eq_opContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#cond_op.
    def visitCond_op(self, ctx:DecafParser.Cond_opContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#literal.
    def visitLiteral(self, ctx:DecafParser.LiteralContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#bin_op.
    def visitBin_op(self, ctx:DecafParser.Bin_opContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#arith_op.
    def visitArith_op(self, ctx:DecafParser.Arith_opContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#var_type.
    def visitVar_type(self, ctx:DecafParser.Var_typeContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#assign_op.
    def visitAssign_op(self, ctx:DecafParser.Assign_opContext):
        return self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#method_name.
    def visitMethod_name(self, ctx:DecafParser.Method_nameContext):
        return self.printNode(ctx)


test_case_dir = os.path.join(os.getcwd(), "testdata", "parser")
while True:
    print("Enter test case name (or quit):")
    # if file not found: ask again
    try:
        test_case_name = input("> ")

        if test_case_name == "quit":
            break

        # open test case file
        test_case_path = os.path.join(test_case_dir, test_case_name)
        filein = open(test_case_path, 'r')
    except FileNotFoundError:
        print("Incorrect test case number. Try again.")
        continue

    input_text = filein.read()
    lexer = DecafLexer(ant.InputStream(input_text))
    stream = ant.CommonTokenStream(lexer)
    parser = DecafParser(stream)

    tree = parser.program()
    visitor = CalcPrintVisitor()
    visitor.visit(tree)
    print(visitor.text)

    """
        For convenience, automate the tree data pasting into the HTML file
    """
    # read the HTML file to output the tree details
    tree_printer_f = open("D3_parse_tree.html", 'r')
    tree_printer_f_text = tree_printer_f.read()
    tree_printer_f.close()

    # tree data to be replaced
    # find the comment tags with tree data in between and replace them with new data
    match = re.compile('(// tree data start)(.*)(// tree data end)', re.DOTALL)

    # replace and write to HTML FILE
    tree_printer_f = open("D3_parse_tree.html", 'w')
    new_data = "// tree data start\n var treeData = [" + visitor.text + "\n]\n// tree data end"
    new_code = match.sub(new_data, tree_printer_f_text)
    tree_printer_f.write(new_code)
    tree_printer_f.close()
    print("\nTree details written to HTML file successfully.")
    print("--------------------------------------------------")
