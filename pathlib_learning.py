import pprint
from pathlib import Path
import shutil

# CRIANDO OS CAMINHOS ABSOLUTOS.
PATH_PROJECT = Path()
PATH_PROJECT_ABSOLUTE = PATH_PROJECT.absolute()

# CRIANDO A PASTA.
folder_example_practice = PATH_PROJECT_ABSOLUTE / 'folder_example'
folder_example_practice.mkdir(exist_ok=True) 

# CRIANDO UMA PASTA DENTRO DE OUTRA PASTA JÁ CRIADA.
folder_example_practice_into = folder_example_practice / 'new folder'
folder_example_practice_into.mkdir(exist_ok=True)

# CRIANDO ARQUIVO DENTRO DA PASTA ANTERIORMENTE CRIADA
path_file_exemple = Path(__file__).parent / 'folder_example' / \
'file_exemple.txt'
path_file_exemple.touch()

# CRIANDO ARQUIVO DENTRO DE SUBPASTA.
file_sub_folder = folder_example_practice_into / 'file_sub_folder.txt'
file_sub_folder.touch()


# ESCREVENDO DENTRO DO ARQUIVO.
path_file_exemple.write_text(
"""
Hello, World!
I'm study about the pathlib and your uses.
"""
)

content_file = path_file_exemple.read_text()

# EXCLUINDO ARQUIVO DA SUB PASTA. 
file_sub_folder.unlink()

# ESCREVENDO EM ARQUIVOS USANDO CONTEXTMANEGER. ESSE ARQUIVO É O DA SUBPASTA.
with open(file_sub_folder, 'a+') as file:
    file.write('My name is Leonardo \n')
    file.write('Flamengo is the better soccer team on \
the world! \n')

# AVALIANDO O CONTEÚDO DE UMA PASTA.

# Posso fazer isso usando laço for, mas aqui estarei limitado a apenas um nível
# de diretório.
# for i in folder_example_practice.glob('*'):
#     if i.is_dir():
#         print(f'Directory Name: {i.name}')
#     elif i.is_file():
#         print(f'File Name: {i.name}')

# Para acessar mais níveis de pastas internas usaremos uma função recursiva.
def rmtree(path_folder: Path, remove_folder = True):
    for file in path_folder.glob('*'):
        if file.is_dir():
            print(f'Directory: {file.name}')
            rmtree(file)
            
        
        if file.is_file():
            print(f'File: {file.name}')
            file.unlink()
    if remove_folder:
        path_folder.rmdir()

    
rmtree(folder_example_practice) #chamada da função.


# print(file_sub_folder.read_text())

# APAGANDO DIRETORIOS E ARQUIVOS DE UMA VEZ SÓ
# shutil.rmtree(folder_example_practice)


