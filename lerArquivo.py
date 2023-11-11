import sys
import re


class LerArquivo:
    def verifica_args(self):
        try:
            if len(sys.argv) > 1:
                arquivo = sys.argv[1]
                return arquivo
            else:
                raise Exception("No file")
        except Exception as e:
            print(e)

    def verificar_nome_args(self):
        regular = r'^[a-zA-Z0-9]+\.bombom$'

        try:
            nome_arq = self.verifica_args()
            verifica_final = re.search(regular, nome_arq)
            if verifica_final:
                return nome_arq
            else:
                raise Exception("Extensão inválida!! Tente com a extensão .bombom")
        except Exception as e:
            print(e)

    def ler_arquivo(self):
        try:
            if open(self.verificar_nome_args()):
                texto = open(self.verificar_nome_args())
                conteudo = texto.read()
                conteudo = conteudo.replace("\n", "")
                conteudo = conteudo.replace(" ", "")
                texto.close()

                codigo = ""
                for line in conteudo:
                    codigo += line

                codigo += "\n"

                return codigo
            else:
                raise Exception("Não abri o arquivo")
        except Exception as e:
            print(e)
