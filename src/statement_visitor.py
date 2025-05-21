from minic_parser.MiniCParser import MiniCParser

class StatementVisitor:
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
        init_str = self.visit(ctx.init) if ctx.init else ""
        condition_str = self.visit(ctx.cond) if ctx.cond else ""
        update_str = self.visit(ctx.upd) if ctx.upd else ""
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
        expr_str = f" {self.visit(ctx.expression())}" if ctx.expression() else ""
        return f"{self.get_indent()}return{expr_str};"
