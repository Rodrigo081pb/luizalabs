import os
import shutil

# criar um diretório
# os.mkdir('exemplo')

# criar um arquivo dentro do diretório
with open('exemplo/exemplo.txt', 'w', encoding='utf-8') as f:
    f.write('Conteúdo de exemplo')

# Renomear um diretório
os.rename('exemplo.txt', 'exemplo_renomeado.txt')

# Remover arquivo
os.remove('exemplo/exemplo.txt')

# mover um diretório
shutil.move('diretorio_origem.txt', 'diretorio_destino.txt')
