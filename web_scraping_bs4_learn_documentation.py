from turtle import title
from bs4 import BeautifulSoup
import requests

url = 'http://localhost:8000/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='UTF-8')
path_exemple = parsed_html.select_one('#intro > div > div > article')



print(parsed_html.select('div.section-content'))



# for i in title_html.stripped_strings:
#     print(i)


# print(title_html.strings)
# for i in title_html.strings:
#     print(i)


# for i in title_html.descendants:
#     print(i)



# print(parsed_html.get_text())


# print(parsed_html.find_all('a'))

# for a in parsed_html.find_all('a'):
#     print(a.get('href'), end='\n')




# paragraphs = path_exemple.parent.select('p')
# for p in paragraphs:
#     print(p.text)

# if path_exemple is not None:
#     for p in path_exemple.parent.select('p'):
#         print(p.text, end='\n')