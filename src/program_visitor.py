from minic_parser.MiniCParser import MiniCParser

class ProgramVisitor:
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
        params = self.visit(ctx.parameters()) if ctx.parameters() else ""
        body = self.visit(ctx.block())
        return f"{type_spec} {func_name}({params}) {body}"

    def visitParameters(self, ctx: MiniCParser.ParametersContext):
        return self.visit_node_list(ctx.parameter(), ", ")

    def visitParameter(self, ctx: MiniCParser.ParameterContext):
        return f"{self.visit(ctx.typeSpecifier())} {ctx.IDENTIFIER().getText()}"
