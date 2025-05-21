# Generated from grammar/MiniC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,254,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,1,1,1,3,1,67,
        8,1,1,2,1,2,1,2,1,2,3,2,73,8,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,3,
        4,83,8,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,91,8,5,10,5,12,5,94,9,5,1,6,
        1,6,1,6,1,7,1,7,5,7,101,8,7,10,7,12,7,104,9,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,3,8,116,8,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,128,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,3,12,141,8,12,1,12,1,12,3,12,145,8,12,1,12,1,
        12,1,12,1,13,1,13,3,13,152,8,13,3,13,154,8,13,1,14,1,14,3,14,158,
        8,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,3,16,167,8,16,1,17,1,17,
        1,17,5,17,172,8,17,10,17,12,17,175,9,17,1,18,1,18,1,18,5,18,180,
        8,18,10,18,12,18,183,9,18,1,19,1,19,1,19,5,19,188,8,19,10,19,12,
        19,191,9,19,1,20,1,20,1,20,5,20,196,8,20,10,20,12,20,199,9,20,1,
        21,1,21,1,21,5,21,204,8,21,10,21,12,21,207,9,21,1,22,1,22,1,22,5,
        22,212,8,22,10,22,12,22,215,9,22,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,3,23,226,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,
        24,235,8,24,1,25,1,25,1,25,3,25,240,8,25,1,25,1,25,1,26,1,26,1,26,
        5,26,247,8,26,10,26,12,26,250,9,26,1,27,1,27,1,27,0,0,28,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,0,6,1,0,6,8,2,0,23,23,26,26,2,0,21,22,24,25,1,0,31,32,1,0,
        33,35,2,0,9,9,11,13,260,0,59,1,0,0,0,2,66,1,0,0,0,4,68,1,0,0,0,6,
        76,1,0,0,0,8,78,1,0,0,0,10,87,1,0,0,0,12,95,1,0,0,0,14,98,1,0,0,
        0,16,115,1,0,0,0,18,117,1,0,0,0,20,120,1,0,0,0,22,129,1,0,0,0,24,
        135,1,0,0,0,26,153,1,0,0,0,28,155,1,0,0,0,30,161,1,0,0,0,32,163,
        1,0,0,0,34,168,1,0,0,0,36,176,1,0,0,0,38,184,1,0,0,0,40,192,1,0,
        0,0,42,200,1,0,0,0,44,208,1,0,0,0,46,225,1,0,0,0,48,234,1,0,0,0,
        50,236,1,0,0,0,52,243,1,0,0,0,54,251,1,0,0,0,56,58,3,2,1,0,57,56,
        1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,
        61,59,1,0,0,0,62,63,5,0,0,1,63,1,1,0,0,0,64,67,3,4,2,0,65,67,3,8,
        4,0,66,64,1,0,0,0,66,65,1,0,0,0,67,3,1,0,0,0,68,69,3,6,3,0,69,72,
        5,10,0,0,70,71,5,20,0,0,71,73,3,30,15,0,72,70,1,0,0,0,72,73,1,0,
        0,0,73,74,1,0,0,0,74,75,5,18,0,0,75,5,1,0,0,0,76,77,7,0,0,0,77,7,
        1,0,0,0,78,79,3,6,3,0,79,80,5,10,0,0,80,82,5,14,0,0,81,83,3,10,5,
        0,82,81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,85,5,15,0,0,85,86,
        3,14,7,0,86,9,1,0,0,0,87,92,3,12,6,0,88,89,5,19,0,0,89,91,3,12,6,
        0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,11,
        1,0,0,0,94,92,1,0,0,0,95,96,3,6,3,0,96,97,5,10,0,0,97,13,1,0,0,0,
        98,102,5,16,0,0,99,101,3,16,8,0,100,99,1,0,0,0,101,104,1,0,0,0,102,
        100,1,0,0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,102,1,0,0,0,105,
        106,5,17,0,0,106,15,1,0,0,0,107,116,3,4,2,0,108,116,3,18,9,0,109,
        116,3,20,10,0,110,116,3,22,11,0,111,116,3,24,12,0,112,116,3,28,14,
        0,113,116,3,14,7,0,114,116,5,18,0,0,115,107,1,0,0,0,115,108,1,0,
        0,0,115,109,1,0,0,0,115,110,1,0,0,0,115,111,1,0,0,0,115,112,1,0,
        0,0,115,113,1,0,0,0,115,114,1,0,0,0,116,17,1,0,0,0,117,118,3,30,
        15,0,118,119,5,18,0,0,119,19,1,0,0,0,120,121,5,1,0,0,121,122,5,14,
        0,0,122,123,3,30,15,0,123,124,5,15,0,0,124,127,3,16,8,0,125,126,
        5,2,0,0,126,128,3,16,8,0,127,125,1,0,0,0,127,128,1,0,0,0,128,21,
        1,0,0,0,129,130,5,3,0,0,130,131,5,14,0,0,131,132,3,30,15,0,132,133,
        5,15,0,0,133,134,3,16,8,0,134,23,1,0,0,0,135,136,5,4,0,0,136,137,
        5,14,0,0,137,138,3,26,13,0,138,140,5,18,0,0,139,141,3,30,15,0,140,
        139,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,144,5,18,0,0,143,
        145,3,30,15,0,144,143,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,
        147,5,15,0,0,147,148,3,16,8,0,148,25,1,0,0,0,149,154,3,4,2,0,150,
        152,3,30,15,0,151,150,1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,
        149,1,0,0,0,153,151,1,0,0,0,154,27,1,0,0,0,155,157,5,5,0,0,156,158,
        3,30,15,0,157,156,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,
        5,18,0,0,160,29,1,0,0,0,161,162,3,32,16,0,162,31,1,0,0,0,163,166,
        3,34,17,0,164,165,5,20,0,0,165,167,3,32,16,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,33,1,0,0,0,168,173,3,36,18,0,169,170,5,29,0,0,170,
        172,3,36,18,0,171,169,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,
        174,1,0,0,0,174,35,1,0,0,0,175,173,1,0,0,0,176,181,3,38,19,0,177,
        178,5,28,0,0,178,180,3,38,19,0,179,177,1,0,0,0,180,183,1,0,0,0,181,
        179,1,0,0,0,181,182,1,0,0,0,182,37,1,0,0,0,183,181,1,0,0,0,184,189,
        3,40,20,0,185,186,7,1,0,0,186,188,3,40,20,0,187,185,1,0,0,0,188,
        191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,39,1,0,0,0,191,189,
        1,0,0,0,192,197,3,42,21,0,193,194,7,2,0,0,194,196,3,42,21,0,195,
        193,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,
        41,1,0,0,0,199,197,1,0,0,0,200,205,3,44,22,0,201,202,7,3,0,0,202,
        204,3,44,22,0,203,201,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,
        206,1,0,0,0,206,43,1,0,0,0,207,205,1,0,0,0,208,213,3,46,23,0,209,
        210,7,4,0,0,210,212,3,46,23,0,211,209,1,0,0,0,212,215,1,0,0,0,213,
        211,1,0,0,0,213,214,1,0,0,0,214,45,1,0,0,0,215,213,1,0,0,0,216,217,
        5,31,0,0,217,226,3,46,23,0,218,219,5,32,0,0,219,226,3,46,23,0,220,
        221,5,30,0,0,221,226,3,46,23,0,222,223,5,27,0,0,223,226,3,48,24,
        0,224,226,3,48,24,0,225,216,1,0,0,0,225,218,1,0,0,0,225,220,1,0,
        0,0,225,222,1,0,0,0,225,224,1,0,0,0,226,47,1,0,0,0,227,235,5,10,
        0,0,228,235,3,54,27,0,229,230,5,14,0,0,230,231,3,30,15,0,231,232,
        5,15,0,0,232,235,1,0,0,0,233,235,3,50,25,0,234,227,1,0,0,0,234,228,
        1,0,0,0,234,229,1,0,0,0,234,233,1,0,0,0,235,49,1,0,0,0,236,237,5,
        10,0,0,237,239,5,14,0,0,238,240,3,52,26,0,239,238,1,0,0,0,239,240,
        1,0,0,0,240,241,1,0,0,0,241,242,5,15,0,0,242,51,1,0,0,0,243,248,
        3,30,15,0,244,245,5,19,0,0,245,247,3,30,15,0,246,244,1,0,0,0,247,
        250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,53,1,0,0,0,250,248,
        1,0,0,0,251,252,7,5,0,0,252,55,1,0,0,0,24,59,66,72,82,92,102,115,
        127,140,144,151,153,157,166,173,181,189,197,205,213,225,234,239,
        248
    ]

class MiniCParser ( Parser ):

    grammarFileName = "MiniC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'for'", 
                     "'return'", "'int'", "'char'", "'bool'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "'>'", 
                     "'<'", "'=='", "'<='", "'>='", "'!='", "'&'", "'&&'", 
                     "'||'", "'!'", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "FOR", "RETURN", 
                      "INT", "CHAR", "BOOL", "BOOL_LITERAL", "IDENTIFIER", 
                      "INT_LITERAL", "CHAR_LITERAL", "STRING_LITERAL", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "SEMI", "COMMA", "ASSIGN", 
                      "GT", "LT", "EQ", "LTE", "GTE", "NEQ", "AMPERSAND", 
                      "AND", "OR", "NOT", "PLUS", "MINUS", "MUL", "DIV", 
                      "MOD", "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_variableDeclaration = 2
    RULE_typeSpecifier = 3
    RULE_functionDeclaration = 4
    RULE_parameters = 5
    RULE_parameter = 6
    RULE_block = 7
    RULE_statement = 8
    RULE_expressionStatement = 9
    RULE_ifStatement = 10
    RULE_whileStatement = 11
    RULE_forStatement = 12
    RULE_forInitialization = 13
    RULE_returnStatement = 14
    RULE_expression = 15
    RULE_assignmentExpression = 16
    RULE_logicalOrExpression = 17
    RULE_logicalAndExpression = 18
    RULE_equalityExpression = 19
    RULE_relationalExpression = 20
    RULE_additiveExpression = 21
    RULE_multiplicativeExpression = 22
    RULE_unaryExpression = 23
    RULE_primaryExpression = 24
    RULE_functionCall = 25
    RULE_arguments = 26
    RULE_constant = 27

    ruleNames =  [ "program", "declaration", "variableDeclaration", "typeSpecifier", 
                   "functionDeclaration", "parameters", "parameter", "block", 
                   "statement", "expressionStatement", "ifStatement", "whileStatement", 
                   "forStatement", "forInitialization", "returnStatement", 
                   "expression", "assignmentExpression", "logicalOrExpression", 
                   "logicalAndExpression", "equalityExpression", "relationalExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "primaryExpression", "functionCall", "arguments", "constant" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    FOR=4
    RETURN=5
    INT=6
    CHAR=7
    BOOL=8
    BOOL_LITERAL=9
    IDENTIFIER=10
    INT_LITERAL=11
    CHAR_LITERAL=12
    STRING_LITERAL=13
    LPAREN=14
    RPAREN=15
    LBRACE=16
    RBRACE=17
    SEMI=18
    COMMA=19
    ASSIGN=20
    GT=21
    LT=22
    EQ=23
    LTE=24
    GTE=25
    NEQ=26
    AMPERSAND=27
    AND=28
    OR=29
    NOT=30
    PLUS=31
    MINUS=32
    MUL=33
    DIV=34
    MOD=35
    WS=36
    COMMENT=37
    BLOCK_COMMENT=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniCParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniCParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0):
                self.state = 56
                self.declaration()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(MiniCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MiniCParser.VariableDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(MiniCParser.FunctionDeclarationContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.functionDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniCParser.TypeSpecifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniCParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(MiniCParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(MiniCParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = MiniCParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.typeSpecifier()
            self.state = 69
            self.match(MiniCParser.IDENTIFIER)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 70
                self.match(MiniCParser.ASSIGN)
                self.state = 71
                self.expression()


            self.state = 74
            self.match(MiniCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniCParser.INT, 0)

        def CHAR(self):
            return self.getToken(MiniCParser.CHAR, 0)

        def BOOL(self):
            return self.getToken(MiniCParser.BOOL, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_typeSpecifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = MiniCParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniCParser.TypeSpecifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniCParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniCParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(MiniCParser.ParametersContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_functionDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = MiniCParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.typeSpecifier()
            self.state = 79
            self.match(MiniCParser.IDENTIFIER)
            self.state = 80
            self.match(MiniCParser.LPAREN)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0):
                self.state = 81
                self.parameters()


            self.state = 84
            self.match(MiniCParser.RPAREN)
            self.state = 85
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ParameterContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.COMMA)
            else:
                return self.getToken(MiniCParser.COMMA, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = MiniCParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.parameter()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 88
                self.match(MiniCParser.COMMA)
                self.state = 89
                self.parameter()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniCParser.TypeSpecifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniCParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.typeSpecifier()
            self.state = 96
            self.match(MiniCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniCParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(MiniCParser.LBRACE)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7650770938) != 0):
                self.state = 99
                self.statement()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self.match(MiniCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MiniCParser.VariableDeclarationContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniCParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MiniCParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniCParser.ForStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MiniCParser.ReturnStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniCParser.BlockContext,0)


        def SEMI(self):
            return self.getToken(MiniCParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.variableDeclaration()
                pass
            elif token in [9, 10, 11, 12, 13, 14, 27, 30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.expressionStatement()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.ifStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.whileStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
                self.forStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 112
                self.returnStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 113
                self.block()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 114
                self.match(MiniCParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniCParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_expressionStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = MiniCParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.expression()
            self.state = 118
            self.match(MiniCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniCParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MiniCParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniCParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(MiniCParser.IF)
            self.state = 121
            self.match(MiniCParser.LPAREN)
            self.state = 122
            self.expression()
            self.state = 123
            self.match(MiniCParser.RPAREN)
            self.state = 124
            self.statement()
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 125
                self.match(MiniCParser.ELSE)
                self.state = 126
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniCParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniCParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MiniCParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(MiniCParser.WHILE)
            self.state = 130
            self.match(MiniCParser.LPAREN)
            self.state = 131
            self.expression()
            self.state = 132
            self.match(MiniCParser.RPAREN)
            self.state = 133
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.init = None # ForInitializationContext
            self.cond = None # ExpressionContext
            self.upd = None # ExpressionContext
            self.body = None # StatementContext

        def FOR(self):
            return self.getToken(MiniCParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.SEMI)
            else:
                return self.getToken(MiniCParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def forInitialization(self):
            return self.getTypedRuleContext(MiniCParser.ForInitializationContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniCParser.StatementContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniCParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MiniCParser.FOR)
            self.state = 136
            self.match(MiniCParser.LPAREN)
            self.state = 137
            localctx.init = self.forInitialization()
            self.state = 138
            self.match(MiniCParser.SEMI)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7650442752) != 0):
                self.state = 139
                localctx.cond = self.expression()


            self.state = 142
            self.match(MiniCParser.SEMI)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7650442752) != 0):
                self.state = 143
                localctx.upd = self.expression()


            self.state = 146
            self.match(MiniCParser.RPAREN)
            self.state = 147
            localctx.body = self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.varInit = None # VariableDeclarationContext
            self.exprInit = None # ExpressionContext

        def variableDeclaration(self):
            return self.getTypedRuleContext(MiniCParser.VariableDeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_forInitialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitialization" ):
                return visitor.visitForInitialization(self)
            else:
                return visitor.visitChildren(self)




    def forInitialization(self):

        localctx = MiniCParser.ForInitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_forInitialization)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                localctx.varInit = self.variableDeclaration()
                pass
            elif token in [9, 10, 11, 12, 13, 14, 18, 27, 30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7650442752) != 0):
                    self.state = 150
                    localctx.exprInit = self.expression()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MiniCParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniCParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MiniCParser.RETURN)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7650442752) != 0):
                self.state = 156
                self.expression()


            self.state = 159
            self.match(MiniCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(MiniCParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.assignmentExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(MiniCParser.LogicalOrExpressionContext,0)


        def ASSIGN(self):
            return self.getToken(MiniCParser.ASSIGN, 0)

        def assignmentExpression(self):
            return self.getTypedRuleContext(MiniCParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_assignmentExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = MiniCParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignmentExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.logicalOrExpression()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 164
                self.match(MiniCParser.ASSIGN)
                self.state = 165
                self.assignmentExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.OR)
            else:
                return self.getToken(MiniCParser.OR, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_logicalOrExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = MiniCParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.logicalAndExpression()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 169
                self.match(MiniCParser.OR)
                self.state = 170
                self.logicalAndExpression()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.EqualityExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.AND)
            else:
                return self.getToken(MiniCParser.AND, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_logicalAndExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = MiniCParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.equalityExpression()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 177
                self.match(MiniCParser.AND)
                self.state = 178
                self.equalityExpression()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.RelationalExpressionContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.EQ)
            else:
                return self.getToken(MiniCParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.NEQ)
            else:
                return self.getToken(MiniCParser.NEQ, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_equalityExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = MiniCParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.relationalExpression()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==26:
                self.state = 185
                _la = self._input.LA(1)
                if not(_la==23 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                self.relationalExpression()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.AdditiveExpressionContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.LT)
            else:
                return self.getToken(MiniCParser.LT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.LTE)
            else:
                return self.getToken(MiniCParser.LTE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.GT)
            else:
                return self.getToken(MiniCParser.GT, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.GTE)
            else:
                return self.getToken(MiniCParser.GTE, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_relationalExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = MiniCParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.additiveExpression()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 56623104) != 0):
                self.state = 193
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56623104) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 194
                self.additiveExpression()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.PLUS)
            else:
                return self.getToken(MiniCParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.MINUS)
            else:
                return self.getToken(MiniCParser.MINUS, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_additiveExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = MiniCParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.multiplicativeExpression()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==32:
                self.state = 201
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 202
                self.multiplicativeExpression()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.UnaryExpressionContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.MUL)
            else:
                return self.getToken(MiniCParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.DIV)
            else:
                return self.getToken(MiniCParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.MOD)
            else:
                return self.getToken(MiniCParser.MOD, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_multiplicativeExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = MiniCParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.unaryExpression()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0):
                self.state = 209
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 210
                self.unaryExpression()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MiniCParser.PLUS, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(MiniCParser.UnaryExpressionContext,0)


        def MINUS(self):
            return self.getToken(MiniCParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MiniCParser.NOT, 0)

        def AMPERSAND(self):
            return self.getToken(MiniCParser.AMPERSAND, 0)

        def primaryExpression(self):
            return self.getTypedRuleContext(MiniCParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_unaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = MiniCParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unaryExpression)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(MiniCParser.PLUS)
                self.state = 217
                self.unaryExpression()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(MiniCParser.MINUS)
                self.state = 219
                self.unaryExpression()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(MiniCParser.NOT)
                self.state = 221
                self.unaryExpression()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.match(MiniCParser.AMPERSAND)
                self.state = 223
                self.primaryExpression()
                pass
            elif token in [9, 10, 11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 224
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniCParser.IDENTIFIER, 0)

        def constant(self):
            return self.getTypedRuleContext(MiniCParser.ConstantContext,0)


        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def functionCall(self):
            return self.getTypedRuleContext(MiniCParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_primaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = MiniCParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primaryExpression)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(MiniCParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
                self.match(MiniCParser.LPAREN)
                self.state = 230
                self.expression()
                self.state = 231
                self.match(MiniCParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniCParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(MiniCParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MiniCParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MiniCParser.IDENTIFIER)
            self.state = 237
            self.match(MiniCParser.LPAREN)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7650442752) != 0):
                self.state = 238
                self.arguments()


            self.state = 241
            self.match(MiniCParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.COMMA)
            else:
                return self.getToken(MiniCParser.COMMA, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = MiniCParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.expression()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 244
                self.match(MiniCParser.COMMA)
                self.state = 245
                self.expression()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(MiniCParser.INT_LITERAL, 0)

        def CHAR_LITERAL(self):
            return self.getToken(MiniCParser.CHAR_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(MiniCParser.BOOL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniCParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = MiniCParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14848) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





