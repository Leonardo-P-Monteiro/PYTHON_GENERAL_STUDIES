from bs4 import BeautifulSoup
import requests

url = 'http://localhost:8000/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
path_exemple = parsed_html.select_one('#intro > div > div > article > h2')

if path_exemple is not None:
    for p in path_exemple.parent.select('p'):
        print(p.text, end='\n')

# print(path_exemple.select('p'))
