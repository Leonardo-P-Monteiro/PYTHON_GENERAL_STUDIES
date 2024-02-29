import csv
from pathlib import Path


PATH_FILE_CSV = Path(__file__).parent / 'csv_file.csv'

# Lendo em formato de lista.
with open(PATH_FILE_CSV, 'r') as file_csv:
    
    read_csv = csv.reader(file_csv)
    
    for line in read_csv:
        print(line)

print('-/'*32)

# Lendo em formato de dicionário.
with open(PATH_FILE_CSV, 'r') as file_csv:
    
    read_csv = csv.DictReader(file_csv)
    
    for dict_ in read_csv:
        print(dict_)