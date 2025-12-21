# Iteradores

# iter significa que é um iterador que consegue percorrer uma coleção de dados utilizando o método next()
# Um iterador é um objeto que permite percorrer uma coleção de dados, como listas, tuplas ou dicionários, de forma sequencial.
# Ele implementa dois métodos principais: __iter__() e __next__().

# Podemos percorrer o arquivo lista.txt utilizando um iterador: 

# criando a classe FileIterator
class FileIterator:

    # self: significa em python o objeto que está sendo criado
    # init: método construtor que inicializa o objeto
    # filename: nome do arquivo que será lido
    # open: abre o arquivo
    

    def __init__(self, filename):
        self.file = open(filename) # aqui estamos abrindo o arquivo
    
    def __iter__(self):
        return self # retorna o próprio objeto iterador
    
    def __next__(self):
        line = self.file.readline() # lê uma linha do arquivo
        if not line: # se não houver mais linhas para ler
            self.file.close() # fecha o arquivo
            raise StopIteration # sinaliza o fim da iteração
        return line.strip() # retorna a linha lida, removendo espaços em branco
    
# Usando o FileIterator para ler o arquivo lista.txt
for line in FileIterator('iteradores/lista.txt'):
    print(line)
