import string
from pathlib import Path
from datetime import datetime
import locale

local = locale.setlocale(locale.LC_ALL, "")

FILE_PATH = Path(__file__).parent / 'string_Tamplate.txt'
FILE_PATH.touch()

date_birth = datetime(1994, 1, 6)

def wage(number: float) -> str:
    br1 = locale.currency(number, symbol= True, grouping= True)
    return br1



datas = dict(
    name = 'Daniela Martins',
    date_birth = date_birth.strftime('%d/%m/%Y'),
    city = 'Ubajara - Ceará',
    work = 'nurse',
    wage = wage(1_500.25),
    age = '29')
    

text = '''
O nome dela é ${name}, ela tem ${age} anos e nasceu em ${date_birth} e vive 
atualmente em ${city}. Ela trabalha como ${work} e recebe de salário ${wage}.
'''

with open(FILE_PATH, 'w') as file:
    file.write(text)

with open(FILE_PATH, 'r') as file:
    text = file.read()
    tamplet = string.Template(text)
    print(tamplet.substitute(datas))
    