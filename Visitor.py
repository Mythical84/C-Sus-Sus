from CsusVisitor import CsusVisitor
from CsusParser import CsusParser
import numpy as np
from memory import Memory

class Visitor(CsusVisitor):

    def __init__(self):
        self.memory = Memory()

    def visitOpExpr(self, ctx: CsusParser.OpExprContext):
        left = self.visit(ctx.lhs)
        right = self.visit(ctx.rhs)
        op = str(ctx.op.text)

        if op == "*":
            val = left * right
        elif op == "/":
            val = left / right
        elif op == "+":
            val = left + right
        elif op == "-":
            val = left - right
        else:
            raise ValueError("Unknown Operator")
        print(val)
        return val

    def visitParenExpr(self, ctx: CsusParser.ParenExprContext):
        return self.visit(ctx.exp)

    def visitCsus(self, ctx: CsusParser.CsusContext):
        return super().visitCsus(ctx)

    def visitAtomExpr(self, ctx: CsusParser.AtomExprContext):
        return int(ctx.getText())

    def visitBracket_statement(self, ctx: CsusParser.Bracket_statementContext):
        if ctx.label.text == "if":
            boolean = self.visit(ctx.paren.t)
            if boolean:
                self.visit(ctx.brac)
        else:
            boolean = self.visit(ctx.paren.t)
            while boolean:
                self.visit(ctx.brac)
                boolean = self.visit(ctx.paren.t)

    def visitBoolean(self, ctx: CsusParser.BooleanContext):
        if ctx.getText() == "true":
            return True
        else:
            return False

    def visitBrackets(self, ctx: CsusParser.BracketsContext):
        return self.visitChildren(ctx)

    def visitConditional(self, ctx: CsusParser.ConditionalContext):
        if ctx.cond.text == '=':
            if self.visit(ctx.left) == self.visit(ctx.right):
                return True
            else: return False
        elif ctx.cond.text == '~':
            if not ctx.left == ctx.right:
                return True
            else: return False

    def visitParens(self, ctx: CsusParser.ParensContext):
        return self.visitChildren(ctx)
    
    def visitTruth(self, ctx: CsusParser.TruthContext):
        return self.visitChildren(ctx)

    def visitFunction(self, ctx: CsusParser.FunctionContext):
        args = self.visit(ctx.paren)
        if ctx.name.text == 'print':
            for a in args:
                if not a[1:-1].isdigit():
                    a = a[1:-1]
                return print(a, end="")
        if ctx.name.text == 'input':
            if not args[0][1:-1].isdigit():
                args[0] = args[0][1:-1]
            return input(args[0])


    def visitFunctioninput(self, ctx: CsusParser.FunctioninputContext):
        args = ctx.getText()[1:-1].split(",")
        return args
