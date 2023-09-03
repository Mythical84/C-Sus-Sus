# Generated from Csus.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CsusParser import CsusParser
else:
    from CsusParser import CsusParser

# This class defines a complete listener for a parse tree produced by CsusParser.
class CsusListener(ParseTreeListener):

    # Enter a parse tree produced by CsusParser#csus.
    def enterCsus(self, ctx:CsusParser.CsusContext):
        pass

    # Exit a parse tree produced by CsusParser#csus.
    def exitCsus(self, ctx:CsusParser.CsusContext):
        pass


    # Enter a parse tree produced by CsusParser#statement.
    def enterStatement(self, ctx:CsusParser.StatementContext):
        pass

    # Exit a parse tree produced by CsusParser#statement.
    def exitStatement(self, ctx:CsusParser.StatementContext):
        pass


    # Enter a parse tree produced by CsusParser#truth.
    def enterTruth(self, ctx:CsusParser.TruthContext):
        pass

    # Exit a parse tree produced by CsusParser#truth.
    def exitTruth(self, ctx:CsusParser.TruthContext):
        pass


    # Enter a parse tree produced by CsusParser#bracket_statement.
    def enterBracket_statement(self, ctx:CsusParser.Bracket_statementContext):
        pass

    # Exit a parse tree produced by CsusParser#bracket_statement.
    def exitBracket_statement(self, ctx:CsusParser.Bracket_statementContext):
        pass


    # Enter a parse tree produced by CsusParser#function.
    def enterFunction(self, ctx:CsusParser.FunctionContext):
        pass

    # Exit a parse tree produced by CsusParser#function.
    def exitFunction(self, ctx:CsusParser.FunctionContext):
        pass


    # Enter a parse tree produced by CsusParser#functioninput.
    def enterFunctioninput(self, ctx:CsusParser.FunctioninputContext):
        pass

    # Exit a parse tree produced by CsusParser#functioninput.
    def exitFunctioninput(self, ctx:CsusParser.FunctioninputContext):
        pass


    # Enter a parse tree produced by CsusParser#NegExpr.
    def enterNegExpr(self, ctx:CsusParser.NegExprContext):
        pass

    # Exit a parse tree produced by CsusParser#NegExpr.
    def exitNegExpr(self, ctx:CsusParser.NegExprContext):
        pass


    # Enter a parse tree produced by CsusParser#atomExpr.
    def enterAtomExpr(self, ctx:CsusParser.AtomExprContext):
        pass

    # Exit a parse tree produced by CsusParser#atomExpr.
    def exitAtomExpr(self, ctx:CsusParser.AtomExprContext):
        pass


    # Enter a parse tree produced by CsusParser#OpExpr.
    def enterOpExpr(self, ctx:CsusParser.OpExprContext):
        pass

    # Exit a parse tree produced by CsusParser#OpExpr.
    def exitOpExpr(self, ctx:CsusParser.OpExprContext):
        pass


    # Enter a parse tree produced by CsusParser#parenExpr.
    def enterParenExpr(self, ctx:CsusParser.ParenExprContext):
        pass

    # Exit a parse tree produced by CsusParser#parenExpr.
    def exitParenExpr(self, ctx:CsusParser.ParenExprContext):
        pass


    # Enter a parse tree produced by CsusParser#string.
    def enterString(self, ctx:CsusParser.StringContext):
        pass

    # Exit a parse tree produced by CsusParser#string.
    def exitString(self, ctx:CsusParser.StringContext):
        pass


    # Enter a parse tree produced by CsusParser#parens.
    def enterParens(self, ctx:CsusParser.ParensContext):
        pass

    # Exit a parse tree produced by CsusParser#parens.
    def exitParens(self, ctx:CsusParser.ParensContext):
        pass


    # Enter a parse tree produced by CsusParser#brackets.
    def enterBrackets(self, ctx:CsusParser.BracketsContext):
        pass

    # Exit a parse tree produced by CsusParser#brackets.
    def exitBrackets(self, ctx:CsusParser.BracketsContext):
        pass


    # Enter a parse tree produced by CsusParser#conditional.
    def enterConditional(self, ctx:CsusParser.ConditionalContext):
        pass

    # Exit a parse tree produced by CsusParser#conditional.
    def exitConditional(self, ctx:CsusParser.ConditionalContext):
        pass


    # Enter a parse tree produced by CsusParser#boolean.
    def enterBoolean(self, ctx:CsusParser.BooleanContext):
        pass

    # Exit a parse tree produced by CsusParser#boolean.
    def exitBoolean(self, ctx:CsusParser.BooleanContext):
        pass



del CsusParser