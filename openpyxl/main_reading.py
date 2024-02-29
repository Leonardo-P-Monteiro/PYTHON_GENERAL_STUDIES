from pathlib import Path
from  openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOTFOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOTFOLDER / 'workbook.xlsx'

# CARREGANDO UM ARQUIVO DO EXCEL.
workbook = load_workbook(WORKBOOK_PATH)
# worksheet: Worksheet = workbook.active #type:ignore

# NOME DA PLANILHA
sheet_name = 'My_sheet'

# SELECIONANDO A PLANILHA.
worksheet: Worksheet = workbook[sheet_name] 

# LENDO A PLANILHA.

for row in worksheet.iter_rows():
    for cell in row:
        print(cell.internal_value, end= '\t')
        if cell.value == 'Maria':
            worksheet['b3'] = '100'
    print()

# ALTERANDO DADOS DA PLANILHA.

# worksheet['b3'] = '1'


#SALVANDO OS DADOS
workbook.save(WORKBOOK_PATH)

