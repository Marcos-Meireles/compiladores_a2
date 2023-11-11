from tokens import Token, Num, Id

class SymTable():
    def __init__(self, symtable=None):
        self.__table = dict()
        self.symbolTable = symtable

    @property
    def table(self) -> dict:
        return self.__table

    def insert(self, token: Id, value=[]):
        try:
            self.__table[token.value] = token.tag
            return True
        except Exception as e:
            return False

    def find(self, token:Id):
        try:
            if self.__table[token.value] is not None:
                return self.__table[token.value]
            else:
                raise Exception("Variable not found")
        except Exception as e:
            print(e)
            return None