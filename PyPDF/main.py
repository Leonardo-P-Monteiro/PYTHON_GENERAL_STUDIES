from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader, PdfWriter, PdfFileMerger

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_FILES_FOLDER = ROOT_FOLDER / 'file_pdf'
NEW_FILES_FOLDER = ROOT_FOLDER / 'new_files'
RELATORY_BACEN = ORIGINAL_FILES_FOLDER / 'R20240112.pdf'

NEW_FILES_FOLDER.mkdir(exist_ok=True)

# LEITOR DE PDF
reader = PdfReader(RELATORY_BACEN)

# ESCRITOR DE PDF
writer = PdfWriter()

# UNINDO ARQUIVOS
merger = PdfMerger()

# TRABALHANDO COM IMAGEMS
page_0 = reader.pages[0]
picture_0 = page_0.images[0]

# with open(NEW_FILES_FOLDER / picture_0.name, 'wb') as imagem:
#     imagem.write(picture_0.data)

# MANIPULANDO ARQUIVOS
# writer.add_page(page_0)

# Copiando apenas uma página específica do arquivo.
# with open(NEW_FILES_FOLDER / 'page_0.pdf', 'wb') as part_pdf:
#     writer.write(part_pdf) #type: ignore

# Copiando todas as páginas do arquivo.
# with open(NEW_FILES_FOLDER / 'all_pages.pdf', 'wb') as all_pages:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(all_pages)
    
# Criando um pdf para cada página de uma vez só.
# for i, page in enumerate(reader.pages):
#     writer_2 = PdfWriter()
#     with open(NEW_FILES_FOLDER / f'page_{i}.pdf', 'wb') as each_page:
#         writer_2.add_page(page)
#         writer_2.write(each_page)

# Criando um arquivo unindo outros arquivos.
path_files_list = [
    NEW_FILES_FOLDER / 'page_1.pdf',
    NEW_FILES_FOLDER / 'page_0.pdf',
]

for file in path_files_list:
    merger.append(file)
with open(NEW_FILES_FOLDER / 'merged_file.pdf', 'wb') as file_merged:
    merger.write(file_merged) 

