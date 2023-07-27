''''
Ce POC utilise BeautifulSoup pour récupérer le titre d'une 
page web à partir de son URL en utilisant des techniques de web scraping.
'''

import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    print('Titre de la page :', title)
else:
    print('Erreur lors de la récupération de la page.')
