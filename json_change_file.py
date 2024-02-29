import os
import json
from pprint import pprint

# os.system('cls')
FILE_NAME = 'lesson_290.json'
ABOSLUTE_PATH_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)

json_information = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

convert_json_information = json.loads(json_information)

with open(ABOSLUTE_PATH_FILE, 'w' ) as file:
    json.dump(convert_json_information, file, indent = 2)


with open(ABOSLUTE_PATH_FILE, 'r') as file:
    read_json_file = json.load(file)
    pprint(read_json_file)