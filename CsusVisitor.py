# Generated from Csus.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CsusParser import CsusParser
else:
    from CsusParser import CsusParser

# This class defines a complete generic visitor for a parse tree produced by CsusParser.

class CsusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CsusParser#csus.
    def visitCsus(self, ctx:CsusParser.CsusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#statement.
    def visitStatement(self, ctx:CsusParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#truth.
    def visitTruth(self, ctx:CsusParser.TruthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#bracket_statement.
    def visitBracket_statement(self, ctx:CsusParser.Bracket_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#function.
    def visitFunction(self, ctx:CsusParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#functioninput.
    def visitFunctioninput(self, ctx:CsusParser.FunctioninputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#NegExpr.
    def visitNegExpr(self, ctx:CsusParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#atomExpr.
    def visitAtomExpr(self, ctx:CsusParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#OpExpr.
    def visitOpExpr(self, ctx:CsusParser.OpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#parenExpr.
    def visitParenExpr(self, ctx:CsusParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#string.
    def visitString(self, ctx:CsusParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#parens.
    def visitParens(self, ctx:CsusParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#brackets.
    def visitBrackets(self, ctx:CsusParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#conditional.
    def visitConditional(self, ctx:CsusParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CsusParser#boolean.
    def visitBoolean(self, ctx:CsusParser.BooleanContext):
        return self.visitChildren(ctx)



del CsusParser