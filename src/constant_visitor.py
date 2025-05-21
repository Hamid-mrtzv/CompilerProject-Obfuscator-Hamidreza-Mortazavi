class ConstantVisitor:
    def visitConstant(self, ctx):
        return ctx.getText()
