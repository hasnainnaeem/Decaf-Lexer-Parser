grammar DecafL;

/*
 * This file contains Lexer Rules Only
 */

// Keyword specification

IF                  : 'if';

ELSE                : 'else';

FOR                 : 'for';

RETURN              : 'return';

BREAK               : 'break';

CONTINUE            : 'continue';

BOOLEAN             : 'boolean';

CHAR                : 'char';

INT                 : 'int';

STRING              : 'string';

TRUE                : 'True';

FALSE               : 'False';

VOID                : 'void';

CALLOUT             : 'callout';

// Symbol Specification
SEMICOLON           : ';';

LCURLY              : '{';

RCURLY              : '}';

LSQUARE             : '[';

RSQUARE             : ']';

LROUND              : '(';

RROUND              : ')';

COMMA               : ',';

QUOTES              : '"';

APOSTROPHE          : '\'';

ADD                 : '+';

SUB                 : '-';

MULTIPLY            : '*';

DIVIDE              : '/';

REMINDER            : '%';

AND                 : '&&';

OR                  : '||';

NOT                 : '!';

GREATER_OP          : '>';

LESS_OP             : '<';

GREATER_eq_op       : '>=';

LESS_eq_op          : '<=';

EQUAL_OP            : '=';

ADD_eq_op           : '+=';

SUB_eq_op           : '-=';

EQUALITY_OP         : '==';

UNEQUALITY_OP       : '!=';


// Variable names & literal specification

ID                  : ALPHA ALPHA_NUM*; // for variable name

ALPHA      : [a-zA-Z_];

CHAR_LITERAL        : APOSTROPHE ( '\\' [btnfr"'\\] | ~[\r\n\\"] ) APOSTROPHE;

DECIMAL_LITERAL     : [0-9]+;

DIGIT      : [0-9];

HEX_LITERAL         : '0'[xX][0-9a-fA-F]+;

BOOL_LITERAL        : TRUE | FALSE;

STRING_LITERAL      : '"' ( '\\' [btnfr"'\\] | ~[\r\n\\"] )* '"';

ALPHA_NUM           : ALPHA | DIGIT;

HEX_DIGIT  : '0'[xX]([0-9] | [a-fA-F]);

LINE_COMMENT        : '//' .*? '\n' -> skip; // skip single line comments starting from // and ending with new line

COMMENT             : '/*' .*? '*/' -> skip; // skip mutliple comments

//SPACE               : ' ' -> skip; // ignore spaces

NEWLINE				: ('\r'? '\n' | '\r')+ -> skip;

WS : (' ' | '\n')+ -> skip;

decaf : LROUND RROUND;
