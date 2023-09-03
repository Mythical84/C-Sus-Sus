# Generated from /home/tyler/projects/c-sus-sus/Csus.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("k\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\3\3\3\3\3\3\5\3\'")
        buf.write("\n\3\3\4\3\4\5\4+\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\6\78\n\7\r\7\16\79\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\bF\n\b\3\b\3\b\3\b\3\b\3\b\3\b\7")
        buf.write("\bN\n\b\f\b\16\bQ\13\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\6\13_\n\13\r\13\16\13`\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\2\3\16\16\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\2\b\3\2\3\4\3\2\5\n\3\2\33\34\3\2\31\32")
        buf.write("\3\2\21\22\3\2\23\24\2i\2 \3\2\2\2\4&\3\2\2\2\6*\3\2\2")
        buf.write("\2\b,\3\2\2\2\n\60\3\2\2\2\f\63\3\2\2\2\16E\3\2\2\2\20")
        buf.write("R\3\2\2\2\22V\3\2\2\2\24Z\3\2\2\2\26d\3\2\2\2\30h\3\2")
        buf.write("\2\2\32\33\5\4\3\2\33\34\7\27\2\2\34\37\3\2\2\2\35\37")
        buf.write("\5\b\5\2\36\32\3\2\2\2\36\35\3\2\2\2\37\"\3\2\2\2 \36")
        buf.write("\3\2\2\2 !\3\2\2\2!\3\3\2\2\2\" \3\2\2\2#\'\5\n\6\2$\'")
        buf.write("\5\16\b\2%\'\5\20\t\2&#\3\2\2\2&$\3\2\2\2&%\3\2\2\2\'")
        buf.write("\5\3\2\2\2(+\5\30\r\2)+\5\26\f\2*(\3\2\2\2*)\3\2\2\2+")
        buf.write("\7\3\2\2\2,-\t\2\2\2-.\5\22\n\2./\5\24\13\2/\t\3\2\2\2")
        buf.write("\60\61\t\3\2\2\61\62\5\f\7\2\62\13\3\2\2\2\63\67\7\13")
        buf.write("\2\2\64\65\5\4\3\2\65\66\7\f\2\2\668\3\2\2\2\67\64\3\2")
        buf.write("\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:;\3\2\2\2;<\7\r\2")
        buf.write("\2<\r\3\2\2\2=>\b\b\1\2>?\7\13\2\2?@\5\16\b\2@A\7\r\2")
        buf.write("\2AF\3\2\2\2BC\7\32\2\2CF\5\16\b\6DF\7\26\2\2E=\3\2\2")
        buf.write("\2EB\3\2\2\2ED\3\2\2\2FO\3\2\2\2GH\f\5\2\2HI\t\4\2\2I")
        buf.write("N\5\16\b\6JK\f\4\2\2KL\t\5\2\2LN\5\16\b\5MG\3\2\2\2MJ")
        buf.write("\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\17\3\2\2\2QO\3")
        buf.write("\2\2\2RS\7\16\2\2ST\7\25\2\2TU\7\16\2\2U\21\3\2\2\2VW")
        buf.write("\7\13\2\2WX\5\6\4\2XY\7\r\2\2Y\23\3\2\2\2Z^\7\17\2\2[")
        buf.write("\\\5\4\3\2\\]\7\27\2\2]_\3\2\2\2^[\3\2\2\2_`\3\2\2\2`")
        buf.write("^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\7\20\2\2c\25\3\2\2\2d")
        buf.write("e\5\4\3\2ef\t\6\2\2fg\5\4\3\2g\27\3\2\2\2hi\t\7\2\2i\31")
        buf.write("\3\2\2\2\13\36 &*9EMO`")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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




    def csus(self):

        localctx = CsusParser.CsusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_csus)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CsusParser.T__0) | (1 << CsusParser.T__1) | (1 << CsusParser.T__2) | (1 << CsusParser.T__3) | (1 << CsusParser.T__4) | (1 << CsusParser.T__5) | (1 << CsusParser.T__6) | (1 << CsusParser.T__7) | (1 << CsusParser.T__8) | (1 << CsusParser.T__11) | (1 << CsusParser.NUM) | (1 << CsusParser.SUB))) != 0):
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CsusParser.T__2, CsusParser.T__3, CsusParser.T__4, CsusParser.T__5, CsusParser.T__6, CsusParser.T__7, CsusParser.T__8, CsusParser.T__11, CsusParser.NUM, CsusParser.SUB]:
                    self.state = 24
                    self.statement()
                    self.state = 25
                    self.match(CsusParser.SEMI)
                    pass
                elif token in [CsusParser.T__0, CsusParser.T__1]:
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




    def statement(self):

        localctx = CsusParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CsusParser.T__2, CsusParser.T__3, CsusParser.T__4, CsusParser.T__5, CsusParser.T__6, CsusParser.T__7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.function()
                pass
            elif token in [CsusParser.T__8, CsusParser.NUM, CsusParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.expr(0)
                pass
            elif token in [CsusParser.T__11]:
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




    def truth(self):

        localctx = CsusParser.TruthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_truth)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CsusParser.T__16, CsusParser.T__17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.boolean()
                pass
            elif token in [CsusParser.T__2, CsusParser.T__3, CsusParser.T__4, CsusParser.T__5, CsusParser.T__6, CsusParser.T__7, CsusParser.T__8, CsusParser.T__11, CsusParser.NUM, CsusParser.SUB]:
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




    def bracket_statement(self):

        localctx = CsusParser.Bracket_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bracket_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            localctx.label = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==CsusParser.T__0 or _la==CsusParser.T__1):
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




    def function(self):

        localctx = CsusParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            localctx.name = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CsusParser.T__2) | (1 << CsusParser.T__3) | (1 << CsusParser.T__4) | (1 << CsusParser.T__5) | (1 << CsusParser.T__6) | (1 << CsusParser.T__7))) != 0)):
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CsusParser.T__2) | (1 << CsusParser.T__3) | (1 << CsusParser.T__4) | (1 << CsusParser.T__5) | (1 << CsusParser.T__6) | (1 << CsusParser.T__7) | (1 << CsusParser.T__8) | (1 << CsusParser.T__11) | (1 << CsusParser.NUM) | (1 << CsusParser.SUB))) != 0)):
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



    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CsusParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(CsusParser.NUM, 0)


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


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CsusParser.ExprContext
            super().__init__(parser)
            self.exp = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CsusParser.ExprContext,0)




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
            if token in [CsusParser.T__8]:
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
            elif token in [CsusParser.SUB]:
                localctx = CsusParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(CsusParser.SUB)
                self.state = 65
                localctx.exp = self.expr(4)
                pass
            elif token in [CsusParser.NUM]:
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
                        if not(_la==CsusParser.MUL or _la==CsusParser.DIV):
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
                        if not(_la==CsusParser.ADD or _la==CsusParser.SUB):
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CsusParser.T__2) | (1 << CsusParser.T__3) | (1 << CsusParser.T__4) | (1 << CsusParser.T__5) | (1 << CsusParser.T__6) | (1 << CsusParser.T__7) | (1 << CsusParser.T__8) | (1 << CsusParser.T__11) | (1 << CsusParser.NUM) | (1 << CsusParser.SUB))) != 0)):
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
            if not(_la==CsusParser.T__14 or _la==CsusParser.T__15):
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




    def boolean(self):

        localctx = CsusParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not(_la==CsusParser.T__16 or _la==CsusParser.T__17):
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
         




