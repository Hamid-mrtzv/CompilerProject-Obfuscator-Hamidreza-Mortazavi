from minic_parser.MiniCVisitor import MiniCVisitor
from indentation import IndentationMixin
from program_visitor import ProgramVisitor
from statement_visitor import StatementVisitor
from expression_visitor import ExpressionVisitor
from function_call_visitor import FunctionCallVisitor
from constant_visitor import ConstantVisitor

class CodeReconstructionVisitor(
    MiniCVisitor,
    IndentationMixin,
    ProgramVisitor,
    StatementVisitor,
    ExpressionVisitor,
    FunctionCallVisitor,
    ConstantVisitor,
):
    def __init__(self):
        super().__init__()
        IndentationMixin.__init__(self)
        self.code = []
