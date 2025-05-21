grammar MiniC;

program: (declaration)* EOF;

declaration
    : variableDeclaration
    | functionDeclaration
    ;

variableDeclaration
    : typeSpecifier IDENTIFIER (ASSIGN expression)? SEMI
    ;

typeSpecifier
    : INT | CHAR | BOOL
    ;

functionDeclaration
    : typeSpecifier IDENTIFIER LPAREN parameters? RPAREN block
    ;

parameters
    : parameter (COMMA parameter)*
    ;

parameter
    : typeSpecifier IDENTIFIER
    ;

block
    : LBRACE (statement)* RBRACE
    ;

statement
    : variableDeclaration
    | expressionStatement
    | ifStatement
    | whileStatement
    | forStatement      
    | returnStatement
    | block
    | SEMI
    ;

expressionStatement
    : expression SEMI
    ;

ifStatement
    : IF LPAREN expression RPAREN statement (ELSE statement)?
    ;

whileStatement
    : WHILE LPAREN expression RPAREN statement
    ;

forStatement
    : FOR LPAREN init=forInitialization SEMI cond=expression? SEMI upd=expression? RPAREN body=statement
    ;

forInitialization  
    : varInit=variableDeclaration   
    | exprInit=expression?         
    ;                               

returnStatement
    : RETURN expression? SEMI
    ;

expression
    : assignmentExpression
    ;

assignmentExpression
    : logicalOrExpression (ASSIGN assignmentExpression)?
    ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : equalityExpression (AND equalityExpression)*
    ;

equalityExpression
    : relationalExpression ((EQ | NEQ) relationalExpression)*
    ;

relationalExpression
    : additiveExpression ((LT | LTE | GT | GTE) additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression ((MUL | DIV | MOD) unaryExpression)*
    ;

unaryExpression
    : PLUS unaryExpression
    | MINUS unaryExpression
    | NOT unaryExpression
    | AMPERSAND primaryExpression
    | primaryExpression
    ;

primaryExpression
    : IDENTIFIER
    | constant
    | LPAREN expression RPAREN
    | functionCall
    ;

functionCall
    : IDENTIFIER LPAREN arguments? RPAREN
    ;

arguments
    : expression (COMMA expression)*
    ;

constant
    : INT_LITERAL
    | CHAR_LITERAL
    | BOOL_LITERAL
    | STRING_LITERAL
    ;

IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';
RETURN  : 'return';
INT     : 'int';
CHAR    : 'char';
BOOL    : 'bool';

BOOL_LITERAL    : 'true' | 'false';
IDENTIFIER      : [a-zA-Z_] [a-zA-Z0-9_]*;
INT_LITERAL     : [0-9]+;

CHAR_LITERAL    : '\'' ( '\\' . | ~[\\'] ) '\''; 
STRING_LITERAL  : '"' ( '\\' . | ~[\\"] )*? '"';


LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
SEMI    : ';';
COMMA   : ',';
ASSIGN  : '=';
GT      : '>';
LT      : '<';
EQ      : '==';
LTE     : '<=';
GTE     : '>=';
NEQ     : '!=';
AMPERSAND : '&';    
AND     : '&&';
OR      : '||';
NOT     : '!';
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';
MOD     : '%';

WS          : [ \t\r\n]+ -> skip;
COMMENT     : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;