import csv
from pathlib import Path

PATH_FILE_CSV = Path(__file__).parent / 'csv_file.csv'

list_customers = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

# ESCREVENDO A PARTIR DE UM DICIONÁRIO
with open(PATH_FILE_CSV, 'w') as file_csv:
    
    head_file = list_customers[0].keys()
    writer = csv.DictWriter(
        file_csv,
        fieldnames= head_file
    )

    # Escrevendo o cabeçalho (definindo as colunas) do arquivo.
    writer.writeheader()

    # Escrevendo no arquivo.
    for line in list_customers:
        writer.writerow(line)



list_customers = [
    ['Luiz Otávio', 'Av 1, 22'],
    ['João Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
]


# ESCREVENDO A PARTIR DE UMA LISTA
with open(PATH_FILE_CSV, 'w') as file_csv:
    columns_names = ['Nome', 'Endereço']
    writer = csv.writer(file_csv)

    # Escrevendo os nomes das colunas.
    writer.writerow(columns_names)

    # Escrevendo no arquivo.
    for customer in list_customers:
        writer.writerow(customer)
    
    

