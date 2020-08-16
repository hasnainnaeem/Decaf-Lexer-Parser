# Decaf


## Important Notes
- Task 1 (Lexer) and Task 2 (Parser) are complete.
	- These tasks pass all the given tests as well as some additional tests.
	- Additionally, parser tree data pasting into HTML file is automated. Whenever script `decaf-parser` is executed for any testcase file, its tree is automatically constructed through HTML file.

-  Task 3, 4 are incomplete.


## Installation
- Install ANTLR python library:
`pip install antlr4-python3-runtime`
- Install Pycharm or VSCode plugins for ANTLR 4.


## Usage
- After updating Decaf.g4, compile the language:
`java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Decaf.g4 -visitor`

If parser rules are updated, copy the methods from `DecafVisitor.py` to `decaf-parser.py` and replace `visitChildren` m
method with `printNode`.

- Run lexer:  `python decaf-lexer.py`
- Run Parser: `python decaf-parser.py`


## ANTLR Guide
Checkout this tutorial for ANTLR:
[ANTLR Mega Tutorial](https://tomassetti.me/antlr-mega-tutorial/)
