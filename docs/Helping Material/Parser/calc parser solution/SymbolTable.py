__name__ = 'SymbolTable'

class SymbolTable:
    def __init__(self):
        self.scope = []

    def enterScope(self):
        self.scope.append([])

    def exitScope(self):
        self.scope.pop()

    def addSymbol(self, symbol):
        self.scope[-1].append(symbol)

    def popSymbol(self):
        self.scope[-1].pop()

    def probe(self, id):
        local_scope = self.scope[-1]
        for symbol in local_scope:
            if symbol.id == id:
                return symbol
        return None

    def lookup(self, id):
        for i in range(len(self.scope)):
            local_scope = self.scope[-(i + 1)]
            for symbol in local_scope:
                if symbol.id == id:
                    return symbol
        return None

class VarSymbol:
    def __init__(self, id, type, line, size):
        self.id = id
        self.type = type
        self.line = line
        self.size = size
        self.loc = 0

class MethodSymbol:
    def __init__(self, id, type, line, params):
        self.id = id
        self.type = type
        self.line = line
        self.params = params
        self.size = 0
