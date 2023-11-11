from reservados import termosReservados
from tokens import Token, Num, Id
from lerArquivo import LerArquivo
from tabelaSimbolos import SymTable
from analisadorLexico import *


class Sintatico():
    def __init__(self):
        self.__symtable: SymTable = SymTable()
        self.__copy_list: list = list()

        lista_lexico = ""
        for elementinho in Lexico().tokenization():
            if hasattr(elementinho, 'value'):
                self.__copy_list.append(elementinho)
            else:
                self.__copy_list.append(elementinho)

        for token in self.__copy_list:
            if hasattr(token, 'value'):
                lista_lexico += f"<{token.tag},{token.value} > "
            else:
                lista_lexico += f"<{token.tag}> "
        print(lista_lexico)

    def __peek(self, pos=0):
        return self.__copy_list[pos]

    def __next_context(self, position=0, context=None, symtable: SymTable = None):
        if context is None or position >= len(context):
            return 0

        context_counter = 0
        i = position
        while i < len(context):
            token = context[i]
            if token.tag == "id" and context[i + 1].tag == "=" and context[i + 2].tag is not None:
                insert_success = symtable.insert(token, self.__pick_value(context=context, position=i + 2))
                if not insert_success:
                    raise Exception("Variável já existente!!!")
            elif token.tag == "(":
                context_counter += 1
                symtable.symbolTable = SymTable()
                inner_counter, i = self.__next_context(position=i + 1, context=context, symtable=symtable.symbolTable)
                context_counter += inner_counter
            elif token.tag == ")":
                return context_counter, i
            i += 1
        return context_counter, i

    def __pick_value(self, context=None, position=0) -> list:
        for last_position, token in enumerate(context[position:]):
            if token.tag == ";":
                return context[position:last_position - 1]

    def __call__(self, *args, **kwds) -> None:
        context_counter = self.__next_context(context=self.__copy_list, symtable=self.__symtable)
        print(context_counter)
        symtables_counter, tokens_counter = context_counter

        if symtables_counter > 0 and tokens_counter > 0:
            symtable = self.__symtable
            while symtable.symbolTable is not None:
                print(symtable.table)
                symtable = symtable.symbolTable
