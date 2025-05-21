def transform_additive_expression(visitor, ctx):
    if not visitor.active_techniques.get("transform_expressions") or ctx.getChildCount() <= 1:
        return visitor.visitChildren(ctx)
    
    result = visitor.visit(ctx.multiplicativeExpression(0))
    idx = 1
    while idx < ctx.getChildCount():
        op = ctx.getChild(idx).getText()
        right = visitor.visit(ctx.getChild(idx + 1))
        result += f" - (0 - ({right}))" if op == '+' else f" + (0 - ({right}))"
        idx += 2
    return result
