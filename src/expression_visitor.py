from minic_parser.MiniCParser import MiniCParser

class ExpressionVisitor:
    def visitExpression(self, ctx: MiniCParser.ExpressionContext):
        return self.visit(ctx.assignmentExpression())

    def visitAssignmentExpression(self, ctx: MiniCParser.AssignmentExpressionContext):
        if ctx.ASSIGN():
            left = self.visit(ctx.logicalOrExpression())
            right = self.visit(ctx.assignmentExpression())
            return f"{left} = {right}"
        return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx: MiniCParser.LogicalOrExpressionContext):
        result = self.visit(ctx.logicalAndExpression(0))
        for i in range(1, len(ctx.logicalAndExpression())):
            result += f" || {self.visit(ctx.logicalAndExpression(i))}"
        return result

    def visitLogicalAndExpression(self, ctx: MiniCParser.LogicalAndExpressionContext):
        result = self.visit(ctx.equalityExpression(0))
        for i in range(1, len(ctx.equalityExpression())):
            result += f" && {self.visit(ctx.equalityExpression(i))}"
        return result

    def visitEqualityExpression(self, ctx: MiniCParser.EqualityExpressionContext):
        result = self.visit(ctx.relationalExpression(0))
        idx = 1
        while idx < len(ctx.relationalExpression()):
            op_node = ctx.getChild(idx * 2 - 1)
            op_text = op_node.getText()
            result += f" {op_text} {self.visit(ctx.relationalExpression(idx))}"
            idx += 1
        return result

    def visitRelationalExpression(self, ctx: MiniCParser.RelationalExpressionContext):
        result = self.visit(ctx.additiveExpression(0))
        idx = 1
        while idx < len(ctx.additiveExpression()):
            op_node = ctx.getChild(idx * 2 - 1)
            op_text = op_node.getText()
            result += f" {op_text} {self.visit(ctx.additiveExpression(idx))}"
            idx += 1
        return result

    def visitAdditiveExpression(self, ctx: MiniCParser.AdditiveExpressionContext):
        result = self.visit(ctx.multiplicativeExpression(0))
        idx = 1
        while idx < len(ctx.multiplicativeExpression()):
            op_node = ctx.getChild(idx * 2 - 1)
            op_text = op_node.getText()
            result += f" {op_text} {self.visit(ctx.multiplicativeExpression(idx))}"
            idx += 1
        return result

    def visitMultiplicativeExpression(self, ctx: MiniCParser.MultiplicativeExpressionContext):
        result = self.visit(ctx.unaryExpression(0))
        idx = 1
        while idx < len(ctx.unaryExpression()):
            op_node = ctx.getChild(idx * 2 - 1)
            op_text = op_node.getText()
            result += f" {op_text} {self.visit(ctx.unaryExpression(idx))}"
            idx += 1
        return result

    def visitUnaryExpression(self, ctx: MiniCParser.UnaryExpressionContext):
        if ctx.PLUS():
            return f"+{self.visit(ctx.unaryExpression())}"
        if ctx.MINUS():
            return f"-{self.visit(ctx.unaryExpression())}"
        if ctx.NOT():
            return f"!{self.visit(ctx.unaryExpression())}"
        if ctx.AMPERSAND():
            return f"&{self.visit(ctx.primaryExpression())}"
        return self.visit(ctx.primaryExpression())

    def visitPrimaryExpression(self, ctx: MiniCParser.PrimaryExpressionContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        if ctx.constant():
            return self.visit(ctx.constant())
        if ctx.LPAREN():
            return f"({self.visit(ctx.expression())})"
        if ctx.functionCall():
            return self.visit(ctx.functionCall())
        return ""
