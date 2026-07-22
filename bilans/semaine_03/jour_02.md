JOUR 2 - BEAUTIFULSOUP HTML PARSING
Objectif: Parser HTML, chercher tags, extraire infos structurees

================================================================================

INSTALLATION

pip install beautifulsoup4

================================================================================

CONCEPTS CLES

Parsing HTML:
from bs4 import BeautifulSoup
html = "<html><h1>Title</h1></html>"
soup = BeautifulSoup(html, 'html.parser')

find() - Premiere occurrence:
soup.find('h1')                    # Premier <h1>
soup.find('p', class_='desc')      # Premier <p> avec class="desc"
soup.find('div', id='main')        # Premier <div> avec id="main"

find_all() - Toutes les occurrences:
soup.find_all('a')                 # Tous les <a>
soup.find_all(['h1', 'h2', 'h3']) # Tous les headings

CSS Selectors - Plus puissant:
soup.select('.description')        # Tous les elements avec class="description"
soup.select('#myid')               # Element avec id="myid"
soup.select('div > p')             # <p> enfants directs de <div>

Extraire Texte:
element = soup.find('h1')
print(element.text)  # "Title"

Extraire Attributs:
link = soup.find('a')
print(link.get('href'))     # Contenu de href=""
print(link.get('title'))    # Contenu de title="" (peut etre None)

Iterer:
for link in soup.find_all('a'):
    print(link.get('href'))
    print(link.text)

================================================================================

PATTERNS IMPORTANTS

Fetch + Parse:
import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')

Boucle + Condition:
for element in soup.find_all('p'):
    text = element.text
    if 'keyword' in text.lower():
        print(text)

Imbriques (find dans un resultat):
articles = soup.find_all('article')
for article in articles:
    title = article.find('h2')
    print(title.text)

Attributs personnalises (data-*):
# HTML: <div data-id="123">
element = soup.find('div')
print(element.get('data-id'))  # "123"

================================================================================

EXERCICES JOUR 2

Exo 1 - Parse HTML Basique:
Resultat: Affiche tous les <h2> et <p> formatés

Exo 2 - Fetch reel + Extraire Liens:
Resultat: Fetch https://jsonplaceholder.typicode.com/, affiche tous les liens (texte + URL)

Exo 3 - Tableau HTML:
Resultat: Parse un tableau, affiche chaque ligne formatee (Nom: X, Age: Y)

Exo 4 - CSS Selectors + Attributs:
Resultat: Cherche <article class="post">, affiche titre + auteur + data-id
from bs4 import BeautifulSoup

html = """
<div id="posts">
  <article class="post" data-id="1">
    <h3>Post 1</h3>
    <p class="meta">By Alice</p>
  </article>
</div>
"""

soup = BeautifulSoup(html, 'html.parser')
for article in soup.find_all('article'):
    h3 = article.find('h3')
    meta = article.find('p', class_='meta')
    data_id = article.get('data-id')
    print(f"Title: {h3.text}, Author: {meta.text}, ID: {data_id}")

Exo 5 - Scraper Un Vrai Site:
Resultat: Fetch https://example.com, affiche tous les <h1>/<h2>/<h3>, <p>, liens
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Headings
for h in soup.find_all(['h1', 'h2', 'h3']):
    print(f"{h.name}: {h.text}")

# Paragraphes
for p in soup.find_all('p'):
    print(f"P: {p.text}")

# Liens
for a in soup.find_all('a'):
    print(f"Link: {a.text} -> {a.get('href')}")

================================================================================

PIEGES RENCONTRES

Piege 1: find() retourne une list
Cause: Confusion find vs find_all
Solution: find() = 1er, find_all() = tous

Piege 2: .text None sur None object
Cause: Element n'existe pas
Solution: Ajouter try/except ou verifier avec if

Piege 3: Boucle sur string au lieu de liste
Cause: URL au lieu d'endpoint API
Solution: Verifier que c'est une liste avant boucle

Piege 4: Attribute error sur .get('href')
Cause: Element pas trouve (None)
Solution: Verifier if element: avant .get()

Piege 5: Caracteres speciaux mal affiches
Cause: Encoding HTML
Solution: Utiliser .encode('utf-8') ou ensure_ascii=False

================================================================================

CHECKPOINT AVANT JOUR 3

Peux parser du HTML string - OUI
Sais utiliser find(), find_all(), select() - OUI
Extrais texte et attributs - OUI
Combines requests + BeautifulSoup - OUI
