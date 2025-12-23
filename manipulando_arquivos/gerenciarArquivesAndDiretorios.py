import os
import shutil

# criar um diretório
os.mkdir('exemplo')

# Renomear um diretório
os.rename('exemplo.txt', 'exemplo_renomeado.txt')

# Remover arquivo
os.remove('exemplo_renomeado.txt')

# mover um diretório
shutil.move('diretorio_origem.txt', 'diretorio_destino.txt')
