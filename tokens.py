
class Token:
    def __init__(self, tag):
        self.tag = tag


class Num(Token):
    def __init__(self, value):
        super().__init__("Numero")
        self.value = value


class Id(Token):
    def __init__(self, value):
        super().__init__("id")
        self.value = value