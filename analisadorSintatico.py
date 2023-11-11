from reservados import termosReservados, operadores
from tokens import Token, Num, Id
from lerArquivo import LerArquivo
from tabelaSimbolos import hashTable
from analisadorLexico import *

class Parser:
    def __init__(self):
        self.scanner = Lexico()
        self.lookahead = None
        self.symtable = None

    def match(self, tag):
        if self.lookahead.tag == tag:
            self.lookahead = self.scanner.tokenization()
        else:
            raise Exception("Erro de sintaxe")
