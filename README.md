# Decaf
 
## Usage
After updating Decaf.g4, compile the language:
`java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Decaf.g4 -visitor`

If parser rules are updated, copy the methods from `DecafVisitor.py` to `decaf-parser.py` and replace `visitChildren` m
method with `printNode`.

Run lexer:  `python decaf-lexer.py`

Run Parser: `python decaf-parser.py`

