grammar Calc;

ADD : '+';
SUB : '-';
MULT : '*';
DIVIDE : '/';
EQUALS : '=';
SEMICOLON : ';';
LBRACE : '(';
RBRACE : ')';

fragment ALPHA : [a-zA-Z_];
VAR : ALPHA+;

fragment DIGIT : [0-9];
NUMBER : DIGIT+;

WS : [ \n\r\t]+ -> skip;

calculator : LBRACE statement* expr RBRACE;

expr : VAR
    | NUMBER
    | expr op expr
    | LBRACE expr RBRACE;

op : ADD | SUB | MULT | DIVIDE;

statement : VAR EQUALS expr SEMICOLON;
