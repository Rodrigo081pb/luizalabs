import os
import shutil
from pathlib import Path

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

######################

### pegando o caminho absoluto do diretório atual
ROOT_PATH = Path(__file__).parent

# criando um novo diretório usando o Pathlib
# os.mkdir(ROOT_PATH / 'teste_novo_diretório_dir')

arquivo_path = open(ROOT_PATH / "novo.txt", "w")
arquivo_path.close()

os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / 'renomeado.txt')
