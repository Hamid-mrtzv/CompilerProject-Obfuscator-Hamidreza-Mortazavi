from minic_parser.MiniCParser import MiniCParser

class FunctionCallVisitor:
    def visitFunctionCall(self, ctx: MiniCParser.FunctionCallContext):
        func_name = ctx.IDENTIFIER().getText()
        args_str = self.visit(ctx.arguments()) if ctx.arguments() else ""
        return f"{func_name}({args_str})"

    def visitArguments(self, ctx: MiniCParser.ArgumentsContext):
        return self.visit_node_list(ctx.expression(), ", ")
