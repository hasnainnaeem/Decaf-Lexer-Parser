# Generated from Calc.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\7\2\r\n\2\f")
        buf.write("\2\16\2\20\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\3\3\3\3\3\3\3\7\3\"\n\3\f\3\16\3%\13\3")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\2\3\4\6\2\4\6\b\2\3\3")
        buf.write("\2\3\6\2-\2\n\3\2\2\2\4\33\3\2\2\2\6&\3\2\2\2\b(\3\2\2")
        buf.write("\2\n\16\7\t\2\2\13\r\5\b\5\2\f\13\3\2\2\2\r\20\3\2\2\2")
        buf.write("\16\f\3\2\2\2\16\17\3\2\2\2\17\21\3\2\2\2\20\16\3\2\2")
        buf.write("\2\21\22\5\4\3\2\22\23\7\n\2\2\23\3\3\2\2\2\24\25\b\3")
        buf.write("\1\2\25\34\7\13\2\2\26\34\7\f\2\2\27\30\7\t\2\2\30\31")
        buf.write("\5\4\3\2\31\32\7\n\2\2\32\34\3\2\2\2\33\24\3\2\2\2\33")
        buf.write("\26\3\2\2\2\33\27\3\2\2\2\34#\3\2\2\2\35\36\f\4\2\2\36")
        buf.write("\37\5\6\4\2\37 \5\4\3\5 \"\3\2\2\2!\35\3\2\2\2\"%\3\2")
        buf.write("\2\2#!\3\2\2\2#$\3\2\2\2$\5\3\2\2\2%#\3\2\2\2&\'\t\2\2")
        buf.write("\2\'\7\3\2\2\2()\7\13\2\2)*\7\7\2\2*+\5\4\3\2+,\7\b\2")
        buf.write("\2,\t\3\2\2\2\5\16\33#")
        return buf.getvalue()


class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'='", "';'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ADD", "SUB", "MULT", "DIVIDE", "EQUALS", 
                      "SEMICOLON", "LBRACE", "RBRACE", "VAR", "NUMBER", 
                      "WS" ]

    RULE_calculator = 0
    RULE_expr = 1
    RULE_op = 2
    RULE_statement = 3

    ruleNames =  [ "calculator", "expr", "op", "statement" ]

    EOF = Token.EOF
    ADD=1
    SUB=2
    MULT=3
    DIVIDE=4
    EQUALS=5
    SEMICOLON=6
    LBRACE=7
    RBRACE=8
    VAR=9
    NUMBER=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CalculatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CalcParser.LBRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def RBRACE(self):
            return self.getToken(CalcParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.StatementContext)
            else:
                return self.getTypedRuleContext(CalcParser.StatementContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_calculator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalculator" ):
                listener.enterCalculator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalculator" ):
                listener.exitCalculator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculator" ):
                return visitor.visitCalculator(self)
            else:
                return visitor.visitChildren(self)




    def calculator(self):

        localctx = CalcParser.CalculatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_calculator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(CalcParser.LBRACE)
            self.state = 12
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 9
                    self.statement() 
                self.state = 14
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 15
            self.expr(0)
            self.state = 16
            self.match(CalcParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)

        def NUMBER(self):
            return self.getToken(CalcParser.NUMBER, 0)

        def LBRACE(self):
            return self.getToken(CalcParser.LBRACE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def RBRACE(self):
            return self.getToken(CalcParser.RBRACE, 0)

        def op(self):
            return self.getTypedRuleContext(CalcParser.OpContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcParser.VAR]:
                self.state = 19
                self.match(CalcParser.VAR)
                pass
            elif token in [CalcParser.NUMBER]:
                self.state = 20
                self.match(CalcParser.NUMBER)
                pass
            elif token in [CalcParser.LBRACE]:
                self.state = 21
                self.match(CalcParser.LBRACE)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(CalcParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CalcParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 27
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 28
                    self.op()
                    self.state = 29
                    self.expr(3) 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(CalcParser.ADD, 0)

        def SUB(self):
            return self.getToken(CalcParser.SUB, 0)

        def MULT(self):
            return self.getToken(CalcParser.MULT, 0)

        def DIVIDE(self):
            return self.getToken(CalcParser.DIVIDE, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = CalcParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcParser.ADD) | (1 << CalcParser.SUB) | (1 << CalcParser.MULT) | (1 << CalcParser.DIVIDE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)

        def EQUALS(self):
            return self.getToken(CalcParser.EQUALS, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(CalcParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CalcParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CalcParser.VAR)
            self.state = 39
            self.match(CalcParser.EQUALS)
            self.state = 40
            self.expr(0)
            self.state = 41
            self.match(CalcParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




