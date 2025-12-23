import os
import shutil

# criar um diretório
# os.mkdir('exemplo')

# criar um arquivo dentro do diretório
with open('exemplo/arquivo.txt', 'w', encoding='utf-8') as f:
    f.write('Conteúdo de exemplo')

# Renomear um diretório
# Renomear o arquivo
os.rename(
    'exemplo/arquivo.txt',
    'exemplo/arquivo_renomeado.txt'
)

# Remover arquivo
os.remove('exemplo/arquivo_renomeado.txt')

