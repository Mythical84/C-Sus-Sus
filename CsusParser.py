# Generated from Csus.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,5,
        0,29,8,0,10,0,12,0,32,9,0,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,3,2,41,
        8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,4,5,54,8,5,11,5,
        12,5,55,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,68,8,6,1,6,1,
        6,1,6,1,6,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,4,9,93,8,9,11,9,12,9,94,1,9,1,9,1,
        10,1,10,1,10,1,10,1,11,1,11,1,11,0,1,12,12,0,2,4,6,8,10,12,14,16,
        18,20,22,0,6,1,0,1,2,1,0,3,8,1,0,25,26,1,0,23,24,1,0,15,16,1,0,17,
        18,103,0,30,1,0,0,0,2,36,1,0,0,0,4,40,1,0,0,0,6,42,1,0,0,0,8,46,
        1,0,0,0,10,49,1,0,0,0,12,67,1,0,0,0,14,80,1,0,0,0,16,84,1,0,0,0,
        18,88,1,0,0,0,20,98,1,0,0,0,22,102,1,0,0,0,24,25,3,2,1,0,25,26,5,
        21,0,0,26,29,1,0,0,0,27,29,3,6,3,0,28,24,1,0,0,0,28,27,1,0,0,0,29,
        32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,1,1,0,0,0,32,30,1,0,0,
        0,33,37,3,8,4,0,34,37,3,12,6,0,35,37,3,14,7,0,36,33,1,0,0,0,36,34,
        1,0,0,0,36,35,1,0,0,0,37,3,1,0,0,0,38,41,3,22,11,0,39,41,3,20,10,
        0,40,38,1,0,0,0,40,39,1,0,0,0,41,5,1,0,0,0,42,43,7,0,0,0,43,44,3,
        16,8,0,44,45,3,18,9,0,45,7,1,0,0,0,46,47,7,1,0,0,47,48,3,10,5,0,
        48,9,1,0,0,0,49,53,5,9,0,0,50,51,3,2,1,0,51,52,5,10,0,0,52,54,1,
        0,0,0,53,50,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,
        57,1,0,0,0,57,58,5,11,0,0,58,11,1,0,0,0,59,60,6,6,-1,0,60,61,5,9,
        0,0,61,62,3,12,6,0,62,63,5,11,0,0,63,68,1,0,0,0,64,65,5,24,0,0,65,
        68,3,12,6,4,66,68,5,20,0,0,67,59,1,0,0,0,67,64,1,0,0,0,67,66,1,0,
        0,0,68,77,1,0,0,0,69,70,10,3,0,0,70,71,7,2,0,0,71,76,3,12,6,4,72,
        73,10,2,0,0,73,74,7,3,0,0,74,76,3,12,6,3,75,69,1,0,0,0,75,72,1,0,
        0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,13,1,0,0,0,79,77,
        1,0,0,0,80,81,5,12,0,0,81,82,5,19,0,0,82,83,5,12,0,0,83,15,1,0,0,
        0,84,85,5,9,0,0,85,86,3,4,2,0,86,87,5,11,0,0,87,17,1,0,0,0,88,92,
        5,13,0,0,89,90,3,2,1,0,90,91,5,21,0,0,91,93,1,0,0,0,92,89,1,0,0,
        0,93,94,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,
        5,14,0,0,97,19,1,0,0,0,98,99,3,2,1,0,99,100,7,4,0,0,100,101,3,2,
        1,0,101,21,1,0,0,0,102,103,7,5,0,0,103,23,1,0,0,0,9,28,30,36,40,
        55,67,75,77,94
    ]

class CsusParser ( Parser ):

    grammarFileName = "Csus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'while'", "'print'", "'input'", 
                     "'getPointer'", "'addPointer'", "'subPointer'", "'createVar'", 
                     "'('", "','", "')'", "'\"'", "'{'", "'}'", "'='", "'~'", 
                     "'true'", "'false'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STR", "NUM", 
                      "SEMI", "WS", "ADD", "SUB", "MUL", "DIV" ]

    RULE_csus = 0
    RULE_statement = 1
    RULE_truth = 2
    RULE_bracket_statement = 3
    RULE_function = 4
    RULE_functioninput = 5
    RULE_expr = 6
    RULE_string = 7
    RULE_parens = 8
    RULE_brackets = 9
    RULE_conditional = 10
    RULE_boolean = 11

    ruleNames =  [ "csus", "statement", "truth", "bracket_statement", "function", 
                   "functioninput", "expr", "string", "parens", "brackets", 
                   "conditional", "boolean" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    STR=19
    NUM=20
    SEMI=21
    WS=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CsusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CsusParser.StatementContext)
            else:
                return self.getTypedRuleContext(CsusParser.StatementContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CsusParser.SEMI)
            else:
                return self.getToken(CsusParser.SEMI, i)

        def bracket_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CsusParser.Bracket_statementContext)
            else:
                return self.getTypedRuleContext(CsusParser.Bracket_statementContext,i)


        def getRuleIndex(self):
            return CsusParser.RULE_csus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsus" ):
                listener.enterCsus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsus" ):
                listener.exitCsus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCsus" ):
                return visitor.visitCsus(self)
            else:
                return visitor.visitChildren(self)




    def csus(self):

        localctx = CsusParser.CsusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_csus)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17830910) != 0):
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5, 6, 7, 8, 9, 12, 20, 24]:
                    self.state = 24
                    self.statement()
                    self.state = 25
                    self.match(CsusParser.SEMI)
                    pass
                elif token in [1, 2]:
                    self.state = 27
                    self.bracket_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(CsusParser.FunctionContext,0)


        def expr(self):
            return self.getTypedRuleContext(CsusParser.ExprContext,0)


        def string(self):
            return self.getTypedRuleContext(CsusParser.StringContext,0)


        def getRuleIndex(self):
            return CsusParser.RULE_statement

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

        localctx = CsusParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.function()
                pass
            elif token in [9, 20, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.expr(0)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.string()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TruthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean(self):
            return self.getTypedRuleContext(CsusParser.BooleanContext,0)


        def conditional(self):
            return self.getTypedRuleContext(CsusParser.ConditionalContext,0)


        def getRuleIndex(self):
            return CsusParser.RULE_truth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTruth" ):
                listener.enterTruth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTruth" ):
                listener.exitTruth(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTruth" ):
                return visitor.visitTruth(self)
            else:
                return visitor.visitChildren(self)




    def truth(self):

        localctx = CsusParser.TruthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_truth)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.boolean()
                pass
            elif token in [3, 4, 5, 6, 7, 8, 9, 12, 20, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.conditional()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bracket_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.paren = None # ParensContext
            self.brac = None # BracketsContext

        def parens(self):
            return self.getTypedRuleContext(CsusParser.ParensContext,0)


        def brackets(self):
            return self.getTypedRuleContext(CsusParser.BracketsContext,0)


        def getRuleIndex(self):
            return CsusParser.RULE_bracket_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracket_statement" ):
                listener.enterBracket_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracket_statement" ):
                listener.exitBracket_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracket_statement" ):
                return visitor.visitBracket_statement(self)
            else:
                return visitor.visitChildren(self)




    def bracket_statement(self):

        localctx = CsusParser.Bracket_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bracket_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            localctx.label = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                localctx.label = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 43
            localctx.paren = self.parens()
            self.state = 44
            localctx.brac = self.brackets()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.paren = None # FunctioninputContext

        def functioninput(self):
            return self.getTypedRuleContext(CsusParser.FunctioninputContext,0)


        def getRuleIndex(self):
            return CsusParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = CsusParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            localctx.name = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
                localctx.name = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 47
            localctx.paren = self.functioninput()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioninputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CsusParser.StatementContext)
            else:
                return self.getTypedRuleContext(CsusParser.StatementContext,i)


        def getRuleIndex(self):
            return CsusParser.RULE_functioninput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioninput" ):
                listener.enterFunctioninput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioninput" ):
                listener.exitFunctioninput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioninput" ):
                return visitor.visitFunctioninput(self)
            else:
                return visitor.visitChildren(self)




    def functioninput(self):

        localctx = CsusParser.FunctioninputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functioninput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(CsusParser.T__8)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.statement()
                self.state = 51
                self.match(CsusParser.T__9)
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17830904) != 0)):
                    break

            self.state = 57
            self.match(CsusParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CsusParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NegExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CsusParser.ExprContext
            super().__init__(parser)
            self.exp = None # ExprContext
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(CsusParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(CsusParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegExpr" ):
                listener.enterNegExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegExpr" ):
                listener.exitNegExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CsusParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(CsusParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class OpExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CsusParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.op = None # Token
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CsusParser.ExprContext)
            else:
                return self.getTypedRuleContext(CsusParser.ExprContext,i)

        def MUL(self):
            return self.getToken(CsusParser.MUL, 0)
        def DIV(self):
            return self.getToken(CsusParser.DIV, 0)
        def ADD(self):
            return self.getToken(CsusParser.ADD, 0)
        def SUB(self):
            return self.getToken(CsusParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpExpr" ):
                listener.enterOpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpExpr" ):
                listener.exitOpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpExpr" ):
                return visitor.visitOpExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CsusParser.ExprContext
            super().__init__(parser)
            self.exp = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CsusParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CsusParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = CsusParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 60
                self.match(CsusParser.T__8)
                self.state = 61
                localctx.exp = self.expr(0)
                self.state = 62
                self.match(CsusParser.T__10)
                pass
            elif token in [24]:
                localctx = CsusParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(CsusParser.SUB)
                self.state = 65
                localctx.exp = self.expr(4)
                pass
            elif token in [20]:
                localctx = CsusParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                localctx.atom = self.match(CsusParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = CsusParser.OpExprContext(self, CsusParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        localctx.rhs = self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = CsusParser.OpExprContext(self, CsusParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        localctx.rhs = self.expr(3)
                        pass

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(CsusParser.STR, 0)

        def getRuleIndex(self):
            return CsusParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = CsusParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(CsusParser.T__11)
            self.state = 81
            self.match(CsusParser.STR)
            self.state = 82
            self.match(CsusParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None # TruthContext

        def truth(self):
            return self.getTypedRuleContext(CsusParser.TruthContext,0)


        def getRuleIndex(self):
            return CsusParser.RULE_parens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)




    def parens(self):

        localctx = CsusParser.ParensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(CsusParser.T__8)
            self.state = 85
            localctx.t = self.truth()
            self.state = 86
            self.match(CsusParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BracketsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CsusParser.StatementContext)
            else:
                return self.getTypedRuleContext(CsusParser.StatementContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CsusParser.SEMI)
            else:
                return self.getToken(CsusParser.SEMI, i)

        def getRuleIndex(self):
            return CsusParser.RULE_brackets

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackets" ):
                listener.enterBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackets" ):
                listener.exitBrackets(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrackets" ):
                return visitor.visitBrackets(self)
            else:
                return visitor.visitChildren(self)




    def brackets(self):

        localctx = CsusParser.BracketsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_brackets)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(CsusParser.T__12)
            self.state = 92 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 89
                self.statement()
                self.state = 90
                self.match(CsusParser.SEMI)
                self.state = 94 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17830904) != 0)):
                    break

            self.state = 96
            self.match(CsusParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # StatementContext
            self.cond = None # Token
            self.right = None # StatementContext

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CsusParser.StatementContext)
            else:
                return self.getTypedRuleContext(CsusParser.StatementContext,i)


        def getRuleIndex(self):
            return CsusParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = CsusParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            localctx.left = self.statement()
            self.state = 99
            localctx.cond = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                localctx.cond = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 100
            localctx.right = self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CsusParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = CsusParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




