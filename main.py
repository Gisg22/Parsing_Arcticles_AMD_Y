import requests
import lxml
import json
from bs4 import BeautifulSoup

headers ={
'Accept': '*/*',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

with open('index.html', encoding='utf-8') as file:
    scr = file.read()

soup = BeautifulSoup(scr, 'lxml')
name_and_href_articles = {}
a_href = []
name_and_text_pages = {}

for item in soup.find_all('h2', class_='entry-title'):
    name_and_href_articles[item.text] = item.find_next('a')['href']

with open('name_and_href_articles.json', encoding='utf-8') as file:
    all_page_articles = json.load(file)

for name, href in all_page_articles.items():
    with open(f"data/{name}.html", encoding='utf-8') as file:
        scr = file.read()
    soup = BeautifulSoup(scr, 'lxml')
    text_pages = soup.find_all('div', class_='entry-content')
    for item in text_pages:
        name_and_href_articles[name] = item.text

with open(f"text_data/texts_articles.json", 'w', encoding='utf-8') as file:
    json.dump(name_and_href_articles, file, indent=70,
              ensure_ascii=False)

