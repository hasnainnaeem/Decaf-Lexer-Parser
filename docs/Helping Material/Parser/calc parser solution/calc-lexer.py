import antlr4 as ant
from CalcLexer import CalcLexer

filein = open('testdata/test_01.calc', 'r')
lexer = CalcLexer(ant.InputStream(filein.read()))

while True:
    token = lexer.nextToken()
    if (token.type != -1):
        print(lexer.symbolicNames[token.type])
    else:
        break
