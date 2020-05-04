grammar Calc;

ADD : '+';
SUB : '-';
DIV : '/';
MUL : '*';
LBRACE : '(';
RBRACE : ')';
EQ : '=';
SEMI : ';';

fragment ALPHA : [a-zA-Z_];
VAR : ALPHA+;

fragment DIGIT : [0-9];
NUMBER : DIGIT+;

WS : [ \t\r\n]+ -> skip;

calculator : LBRACE statement* expr RBRACE;

expr :  VAR
      | NUMBER
      | expr (MUL | DIV) expr
      | expr (ADD | SUB) expr
      | LBRACE expr RBRACE;

statement : VAR EQ expr SEMI;
