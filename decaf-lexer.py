import os
import antlr4 as ant

os.system("java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Decaf.g4 -visitor")

from DecafLexer import DecafLexer


test_case_dir = os.path.join(os.getcwd(), "testdata", "lexer")
while True:
    print("Enter test case name (or quit):")
    # if file not found: ask again
    try:
        test_case_name = input("> ")

        if test_case_name == "quit":
            break

        # open test case file
        test_case_path = os.path.join(test_case_dir, test_case_name)
        filein = open(test_case_path, 'r')
    except FileNotFoundError:
        print("Incorrect test case number. Try again.")
        continue

    lexer = DecafLexer(ant.InputStream(filein.read()))
    while True:
        token = lexer.nextToken()
        if token.type != -1:
            print(lexer.symbolicNames[token.type])
        else:
            break
