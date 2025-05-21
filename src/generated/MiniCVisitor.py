# Generated from grammar/MiniC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#program.
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#declaration.
    def visitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MiniCParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MiniCParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameters.
    def visitParameters(self, ctx:MiniCParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameter.
    def visitParameter(self, ctx:MiniCParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#block.
    def visitBlock(self, ctx:MiniCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statement.
    def visitStatement(self, ctx:MiniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MiniCParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#ifStatement.
    def visitIfStatement(self, ctx:MiniCParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#whileStatement.
    def visitWhileStatement(self, ctx:MiniCParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forStatement.
    def visitForStatement(self, ctx:MiniCParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forInitialization.
    def visitForInitialization(self, ctx:MiniCParser.ForInitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniCParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expression.
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#equalityExpression.
    def visitEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#relationalExpression.
    def visitRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#functionCall.
    def visitFunctionCall(self, ctx:MiniCParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#arguments.
    def visitArguments(self, ctx:MiniCParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#constant.
    def visitConstant(self, ctx:MiniCParser.ConstantContext):
        return self.visitChildren(ctx)



del MiniCParser