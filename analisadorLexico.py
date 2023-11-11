from reservados import termosReservados
from tokens import Token, Num, Id
from lerArquivo import LerArquivo


class Lexico:
    def __init__(self):
        self.expr = LerArquivo().ler_arquivo()
        self.index = 0
        self.stack = list()
        self.token_list = list()

    def peek(self, pos=0):
        if (self.index + pos) <= len(self.expr) - 1:
            return self.expr[self.index + pos]
        else:
            return ""

    def advance(self):
        if (self.index + 1) <= len(self.expr) - 1:
            self.index += 1

    def analisa_a_expressao(self):
            try:
                while self.peek() != "\n":
                    token = self.peek()
                    if token == "(":
                        if self.peek(1) in termosReservados["todos_operadores"]:
                            raise Exception("Expressão invalida para este programa")
                        self.stack.append(token)
                    elif token == ')':
                        if len(self.stack) > 0:
                            self.stack.pop() 
                        else:
                            self.stack.append(token)
                    elif token in termosReservados["operadores_aritmeticos"] and self.peek(1) in termosReservados["operadores_aritmeticos"]:
                        print("Coe4")
                        raise Exception(f"Tem um operador logo em seguida do operador: {token}")
                    elif token in termosReservados["operadores_comparacao"] and self.peek(-1)in termosReservados["operadores_comparacao"]:
                        posicao_atual = self.expr.find(token)
                        self.expr = self.expr[:posicao_atual]+self.expr[self.peek(1):]
                        pass
                    elif token in termosReservados["operadores_comparacao"] and self.peek(1) in termosReservados["operadores_comparacao"]:
                        token=f"{token+self.peek(1)}"
                    elif token not in termosReservados['todos_operadores'] and not token.isalpha() and not token.isdigit():
                        print("Coe2")
                        raise Exception(f"Termo no codigo não identificado: {token}")
                    elif token in termosReservados['operadores_matematicos'] and self.peek(1) == "\n":
                        print("Coe1")
                        raise Exception("Expressão invalida para este programa")
                    self.advance()
                    print(token)
                if len(self.stack) > 0:
                    raise Exception("Expressão fora de balanço")
            except Exception as e:
                print(e)
                exit(0)

    def tokenization(self):
        self.analisa_a_expressao()
        self.index = 0
        while (peek := self.peek()) != "\n":
            if peek.isalpha():
                self.token_list.append(self.token_id())
            elif peek.isdigit():
                self.token_list.append(self.token_number())
            elif peek in termosReservados["todos_operadores"]:
                self.token_list.append(self.token())

        return self.token_list

    def token_number(self):
        token = ""
        while self.peek().isdigit():
            token += self.peek()
            self.advance()
        return Num(token)

    def token_id(self):
        token = ""
        while self.peek().isalpha():
            token += self.peek()
            self.advance()
        return Id(token)

    def token(self):
        token = ""
    
        token = self.peek()
        self.advance()
        return Token(token)
