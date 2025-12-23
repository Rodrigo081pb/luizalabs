import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Criar diretório exemplo
(Path('exemplo')).mkdir(exist_ok=True)

# Criar arquivo
with open('exemplo/arquivo.txt', 'w', encoding='utf-8') as f:
    f.write('Conteúdo de exemplo')

# Renomear arquivo
os.replace(
    'exemplo/arquivo.txt',
    'exemplo/arquivo_renomeado.txt'
)

# Remover arquivo
os.remove('exemplo/arquivo_renomeado.txt')

##########################

# Criar novo arquivo
novo = ROOT_PATH / 'novo.txt'
novo.write_text('Arquivo novo', encoding='utf-8')

# Renomear sobrescrevendo se existir
renomeado = ROOT_PATH / 'renomeado.txt'
os.replace(novo, renomeado)

# Criar diretório destino
dest_dir = ROOT_PATH / 'teste_novo_diretório_dir'
dest_dir.mkdir(exist_ok=True)

# Mover arquivo
shutil.move(renomeado, dest_dir / 'renomeado.txt')
