from pathlib import Path
from  openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOTFOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOTFOLDER / 'workbook.xlsx'


workbook = Workbook()
# worksheet: Worksheet = workbook.active #type:ignore
sheet_name = 'My_sheet'
workbook.create_sheet(sheet_name, 0)
worksheet: Worksheet = workbook[sheet_name] 

workbook.remove(workbook['Sheet'])

# CRIANDO CABEÇALHOS.
worksheet.cell(1, 1, 'Nome')
worksheet.cell(1, 2, 'Idade')
worksheet.cell(1, 3, 'Nota')

# DADOS A TRABALHAR.
students = [
    # nome      idade nota
    ['João',    14,   5.5],
    ['Maria',   13,   9.7],
    ['Luiz',    15,   8.8],
    ['Alberto', 16,   10],]


# PARTICULARMENTE PREFIRO ESSA LÓGICA PARA REFORÇA-LA NA MENTE. POIS PODE SER USADA EM MUITAS SITUAÇÕES.
# for line, data_row in enumerate(students, start= 2):
#     for column, data_colum in enumerate(data_row, start=1):
#         worksheet.cell(line, column, data_colum)

# ADICIONANDO DADOS NA WORKSHEET.
for student in students:
    worksheet.append(student)


#SALVANDO OS DADOS
workbook.save(WORKBOOK_PATH)

print('we')