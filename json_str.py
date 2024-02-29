import os
from pprint import pprint
os.system('cls')
import json
from typing import TypedDict


class Person(TypedDict):
    Name: str
    Age: int
    BornDate: list[int]
    Married: bool | None


leonardo_docstring = '''
{
    "Name": "Leonardo",
    "Age": "27",
    "BornDate": ["27", "11", "1995"],
    "Married": "False"
}
'''
leonardo_convert_json: Person = json.loads(leonardo_docstring)


leonardo_back_json = json.dumps(leonardo_convert_json)



print(leonardo_convert_json['BornDate'])
print(leonardo_back_json)