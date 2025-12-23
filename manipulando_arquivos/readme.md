Objetivo:

Aprender como manipular, ler e reescrever arquivos utilizando python

![alt text](image.png)

# Porque precisamso manipular arquivos: 

Os arquivos são essenciais para qualquer tipo de programação pois fornecem um meio de armazenar e recuperar dados através da manipulação de arquivos, podemos persistir os dados além da vida útil de um programa.

Programas persistentes é aqueles programas que persistem os dados mesmos quando os programas estão fechados ou a máquina desligado

# Conceito de arquivo em informática.

Um arquivo é um container no computador onde as informações armazenadas em formato digital

## Existem dois tipos de arquivos que podemos manipular em python:

Arquivos de texto e arquivos binários

----

Por que precisamos manipular arquivos ?

Para manipular arquivos em Python, primeiro precisamos abri-los. Usamos a função 'open()' para isso.

Quando terminamos de trabalhar com o arquivo, utilizamos a função 'close()' para liberar recursos.

### Modos de abertura de arquivo

Existem diferentes modos para abrir um arquivo, como somente leitura ('r'), gravação ('w') e anexar ('a'). O modo de abertura deve ser escolhido de acordo com a operação que iremos realizar.

---

# Introdução a leitura de arquivos

Python fornece várias maneiras de ler um arquivo. Podemos usar 'read()', 'readline()', ou 'readlines()' dependendo de nossas necessidades.

# Métodos readline e readlines

O método 'readline()' lê uma linha por vez, enquanto 'readlines()' retorna uma lista onde cada elemento é uma linha do arquivo.

---

##  Introdução a escrita em códigos:

Podemos usar 'write()' ou 'writelines()' para escrever em um arquivo. Lembre-se, no entanto, de abrir o arquivo no modo correto

