grammar Decaf;


/*
 * Lexer Rules
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

ALPHA               : [a-zA-Z_];

CHAR_LITERAL        : APOSTROPHE ( . | '\t' | '\\' ) APOSTROPHE;

DECIMAL_LITERAL     : [0-9]+;

DIGIT               : [0-9];

HEX_LITERAL         : '0'[xX][0-9a-fA-F]+;

BOOL_LITERAL        : TRUE | FALSE;

STRING_LITERAL      : QUOTES .+? QUOTES ;

ALPHA_NUM           : ALPHA | DIGIT;

HEX_DIGIT           : DIGIT | [a-fA-F];

LINE_COMMENT        : '//' .*? '\n' -> skip; // skip single line comments starting from // and ending with new line

COMMENT             : '/*' .*? '*/' -> skip; // skip mutliple comments

//SPACE               : ' ' -> skip; // ignore spaces

NEWLINE				: ('\r'? '\n' | '\r')+ -> skip;


/*
 * Parser Rules
 */

program			    : class_kw program_kw LCURLY field_declr* method_declr* RCURLY;

var_id              : ID; // placed on top to prevent errors due to conflicting rules

array_id            : var_id LSQUARE int_literal RSQUARE;

// defining some keywords & symbols in the parser which were defined in lexer

equal_op            : EQUAL_OP;

if_kw               : IF;

else_kw             : ELSE;

for_kw              : FOR;

lround              : LROUND;

rround              : RROUND;

lcurly              : LCURLY;

rcurly              : RCURLY;

void                : VOID;

not_sym             : NOT;

sub_sym             : SUB;

return_kw           : RETURN;

callout_kw          : CALLOUT;

break_kw            : BREAK;

class_kw            : 'class';

program_kw          : 'Program';

// other parser rules

field_declr         : var_type field_var (COMMA field_var)* SEMICOLON;

field_var           : var_id | array_id;

method_declr        : return_type method_name lround ((var_type var_id) (COMMA var_type var_id)*)? rround block;

return_type         : (var_type | void);

block               : lcurly vardeclr* statement* rcurly;

statement           : location assign_op expr
                    | location assign_op expr SEMICOLON
                    | method_call
                    | if_kw lround expr rround block (else_kw block)?
                    | var_id equal_op expr SEMICOLON
                    | return_kw expr SEMICOLON
                    // ending value can be a variable or integer literal
                    | for_kw var_id (equal_op int_literal)? COMMA ((var_id (equal_op int_literal)?) | int_literal) block
                    | break_kw SEMICOLON;

vardeclr            : (var_type var_id) (COMMA var_type var_id)* SEMICOLON;

// intermediate rule for method call
method_call_inter   : method_name LROUND (expr (COMMA expr)*)? RROUND;

method_call         : method_call_inter
                    | method_call_inter SEMICOLON
                    | callout_kw lround STRING_LITERAL (COMMA callout_arg (COMMA callout_arg)*)? rround SEMICOLON;

expr                : location
                    | literal
                    | expr bin_op expr
                    | sub_sym expr
                    | method_call
                    | not_sym expr
                    | lround expr rround;

location            : var_id | array_id;

callout_arg         : expr | STRING_LITERAL;

int_literal         : DECIMAL_LITERAL | HEX_LITERAL;

rel_op              : GREATER_OP | LESS_OP | LESS_eq_op | GREATER_eq_op;

eq_op               : EQUALITY_OP | UNEQUALITY_OP;

cond_op             : AND | OR;

literal             : int_literal | CHAR_LITERAL | BOOL_LITERAL;

bin_op              : arith_op | rel_op | eq_op | cond_op;

arith_op            : ADD | SUB | MULTIPLY | DIVIDE | REMINDER;

var_type            : INT | BOOLEAN;

assign_op           : EQUAL_OP
                    | ADD_eq_op
                    | SUB_eq_op;

method_name         : ID;

// recognize the whitespace at the end to prevent string concatenation due to elemination of all sapces
WHITESPACE			: [ \t\r\n] -> skip ;
