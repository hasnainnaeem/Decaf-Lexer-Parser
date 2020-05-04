# Decaf
 
## Important Notes
- `DecafL.g4` defines the rules for Lexer only.
- `Decaf.g4` defines the rules for Lexer and Parser.
-  Using `Decaf.g4` may cause errors without any apparent reason. Which are not actually errors. 
So, to test the lexer, use `DecafL.g4` file with Lexer rules only.

## Installation
- Install ANTLR python library:
`pip install antlr4-python3-runtime`
- Install Pycharm or VSCode plugins for ANTLR 4.

Checkout this tutorial for ANTLR:
[ANTLR Mega Tutorial](https://tomassetti.me/antlr-mega-tutorial/)

## Usage
After updating Decaf.g4, compile the language:
`java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Decaf.g4 -visitor`

If parser rules are updated, copy the methods from `DecafVisitor.py` to `decaf-parser.py` and replace `visitChildren` m
method with `printNode`.

Run lexer:  `python decaf-lexer.py`

Run Parser: `python decaf-parser.py`

