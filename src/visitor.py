from antlr4.tree.Tree import TerminalNode
from generated.MiniCParser import MiniCParser
from generated.MiniCVisitor import MiniCVisitor


class CodeReconstructionVisitor(MiniCVisitor):
    def __init__(self):
        self.indent_level = 0
        self.code = []  
    def get_indent(self):
        return "    " * self.indent_level  

    def visit_node_list(self, nodes, separator=""):
        return separator.join([self.visit(node) for node in nodes if node is not None])

    def visitProgram(self, ctx: MiniCParser.ProgramContext):
        return self.visit_node_list(ctx.declaration(), "\n")

    def visitDeclaration(self, ctx: MiniCParser.DeclarationContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.functionDeclaration():
            return self.visit(ctx.functionDeclaration())
        return ""  

    def visitVariableDeclaration(self, ctx: MiniCParser.VariableDeclarationContext):
        type_spec = self.visit(ctx.typeSpecifier())
        identifier = ctx.IDENTIFIER().getText()
        init_expr = ""
        if ctx.expression():
            init_expr = f" = {self.visit(ctx.expression())}"
        return f"{self.get_indent()}{type_spec} {identifier}{init_expr};"

    def visitTypeSpecifier(self, ctx: MiniCParser.TypeSpecifierContext):
        return ctx.getText()

    def visitFunctionDeclaration(self, ctx: MiniCParser.FunctionDeclarationContext):
        type_spec = self.visit(ctx.typeSpecifier())
        func_name = ctx.IDENTIFIER().getText()
        params = ""
        if ctx.parameters():
            params = self.visit(ctx.parameters())
        body = self.visit(ctx.block())
        return f"{type_spec} {func_name}({params}) {body}"

    def visitParameters(self, ctx: MiniCParser.ParametersContext):
        return self.visit_node_list(ctx.parameter(), ", ")

    def visitParameter(self, ctx: MiniCParser.ParameterContext):
        return f"{self.visit(ctx.typeSpecifier())} {ctx.IDENTIFIER().getText()}"

    def visitBlock(self, ctx: MiniCParser.BlockContext):
        self.indent_level += 1
        statements = "\n".join([self.visit(stmt) for stmt in ctx.statement()])
        self.indent_level -= 1
        if not statements.strip():  
            return f"{{\n{self.get_indent()}}}"
        return f"{{\n{statements}\n{self.get_indent()}}}"

    def visitStatement(self, ctx: MiniCParser.StatementContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.expressionStatement():
            return self.visit(ctx.expressionStatement())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.block():  
            return self.get_indent() + self.visit(ctx.block())
        elif ctx.SEMI():  
            return f"{self.get_indent()};"
        return ""  

    def visitExpressionStatement(self, ctx: MiniCParser.ExpressionStatementContext):
        return f"{self.get_indent()}{self.visit(ctx.expression())};"

    def visitIfStatement(self, ctx: MiniCParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.statement(0))  
        else_stmt_str = ""
        if ctx.ELSE():
            else_stmt_str = f"\n{self.get_indent()}else {self.visit(ctx.statement(1))}"

        if not then_stmt.strip().startswith(self.get_indent() + "{"):  
            then_stmt = (
                f"\n{self.get_indent()}{then_stmt.strip()}"
                if "\n" in then_stmt.strip()
                else f" {then_stmt.strip()}"
            )

        return f"{self.get_indent()}if ({condition}){then_stmt}{else_stmt_str}"

    def visitWhileStatement(self, ctx: MiniCParser.WhileStatementContext):
        condition = self.visit(ctx.expression())
        body_stmt = self.visit(ctx.statement())
        if not body_stmt.strip().startswith(self.get_indent() + "{"):
            body_stmt = (
                f"\n{self.get_indent()}{body_stmt.strip()}"
                if "\n" in body_stmt.strip()
                else f" {body_stmt.strip()}"
            )
        return f"{self.get_indent()}while ({condition}){body_stmt}"


    def visitForStatement(self, ctx: MiniCParser.ForStatementContext):
        init_str = ""
        if ctx.init: 
            init_str = self.visit(ctx.init)  

        condition_str = ""
        if ctx.cond: 
            condition_str = self.visit(ctx.cond)

        update_str = ""
        if ctx.upd: 
            update_str = self.visit(ctx.upd)

        body_stmt_str = self.visit(ctx.body)  

        current_indent_str = self.get_indent()
        if (
            not body_stmt_str.strip().startswith(current_indent_str + "{")
            and "\n" not in body_stmt_str.strip()
            and body_stmt_str.strip() != ";"
        ):
            body_stmt_str = f"\n{current_indent_str}    {body_stmt_str.strip()}"
        elif body_stmt_str.strip() == ";":
            body_stmt_str = f"\n{current_indent_str}    ;"

        return f"{current_indent_str}for ({init_str}; {condition_str}; {update_str}){body_stmt_str}"

    def visitForInitialization(self, ctx: MiniCParser.ForInitializationContext):
        if ctx.varInit:  
            var_decl_ctx = ctx.varInit  
            type_spec = self.visit(var_decl_ctx.typeSpecifier())
            identifier = var_decl_ctx.IDENTIFIER().getText()
            init_expr_val = ""
            if var_decl_ctx.expression():  
                init_expr_val = f" = {self.visit(var_decl_ctx.expression())}"
            return f"{type_spec} {identifier}{init_expr_val}"
        elif ctx.exprInit:  
            return self.visit(ctx.exprInit)
        return "" 

    def visitReturnStatement(self, ctx: MiniCParser.ReturnStatementContext):
        expr_str = ""
        if ctx.expression():
            expr_str = f" {self.visit(ctx.expression())}"
        return f"{self.get_indent()}return{expr_str};"

    def visitExpression(self, ctx: MiniCParser.ExpressionContext):
        return self.visit(ctx.assignmentExpression())

    def visitAssignmentExpression(self, ctx: MiniCParser.AssignmentExpressionContext):
        if ctx.ASSIGN():
            left = self.visit(ctx.logicalOrExpression())  
            right = self.visit(
                ctx.assignmentExpression()
            )  
            return f"{left} = {right}"
        return self.visit(
            ctx.logicalOrExpression()
        ) 

    def visitLogicalOrExpression(self, ctx: MiniCParser.LogicalOrExpressionContext):
        if len(ctx.logicalAndExpression()) > 1:
            return f"{self.visit(ctx.logicalAndExpression(0))} || {self.visit(ctx.logicalOrExpression().logicalAndExpression(1))}"  

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
        if len(ctx.relationalExpression()) > 1:
            op = (
                "==" if ctx.EQ() else "!="
            )  

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

    def visitMultiplicativeExpression(
        self, ctx: MiniCParser.MultiplicativeExpressionContext
    ):
        result = self.visit(ctx.unaryExpression(0))
        idx = 1
        while idx < len(ctx.unaryExpression()):
            op_node = ctx.getChild(idx * 2 - 1) 
            op_text = op_node.getText()
            result += f" {op_text} {self.visit(ctx.unaryExpression(idx))}"
            idx += 1
        return result

    def visitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        if ctx.PLUS(): return f"+{self.visit(ctx.unaryExpression())}"
        if ctx.MINUS(): return f"-{self.visit(ctx.unaryExpression())}"
        if ctx.NOT(): return f"!{self.visit(ctx.unaryExpression())}"
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

    def visitFunctionCall(self, ctx: MiniCParser.FunctionCallContext):
        func_name = ctx.IDENTIFIER().getText()
        args_str = ""
        if ctx.arguments():
            args_str = self.visit(ctx.arguments())
        return f"{func_name}({args_str})"

    def visitArguments(self, ctx: MiniCParser.ArgumentsContext):
        return self.visit_node_list(ctx.expression(), ", ")

    def visitConstant(self, ctx: MiniCParser.ConstantContext):
        return ctx.getText() 
