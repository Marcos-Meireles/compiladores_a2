from analisadorLexico import Lexico
from tokens import Token, Id, Num

dummy = Lexico()

listinha = dummy.tokenization()

for elementinho in listinha:
    if hasattr(elementinho, 'value'):
        print(f'<{elementinho.tag},{elementinho.value}>', end=" ")
    else:
        print(f'<{elementinho.tag}>', end=" ")
