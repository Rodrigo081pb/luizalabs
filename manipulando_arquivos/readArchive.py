
# Lendo arquivos de texto de Readline
with open(
    "C:/Users/r.pinheiro.braga/Desktop/luizalabs/manipulando_arquivos/src/archive.txt",
    "r",
    encoding="utf-8"
) as arquivo:
    print(arquivo.readline())

with open(
    "C:/Users/r.pinheiro.braga/Desktop/luizalabs/manipulando_arquivos/src/archive.txt",
    "r",
    encoding="utf-8"
) as arquivo:
    print(arquivo.readlines())
    
