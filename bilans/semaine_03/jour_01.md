JOUR 1 - REQUESTS MODULE
Objectif: Fetch des pages web/APIs, gerer les erreurs reseau, comprendre les status codes

================================================================================

CONCEPTS CLES

Status Codes:
200 = succes
404 = page not found
403 = forbidden (rate limit, auth)
500+ = serveur error

Structure Requete de base:
import requests
response = requests.get('https://...')
response.status_code → le code (200, 404, etc.)
response.text → HTML/content brut (string)
response.json() → parse JSON auto si possible
response.headers → headers de la reponse

================================================================================

PATTERNS IMPORTANTS

Fetch Simple:
response = requests.get('https://api.github.com/users/octocat')
print(response.status_code)  # 200
print(response.json())       # dict

Avec Timeout (IMPORTANT):
response = requests.get('https://...', timeout=5)
# Sans timeout, peut bloquer indefiniment

Headers (User-Agent):
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://...', headers=headers)
# GitHub/certains sites ignorent si pas d'User-Agent

Parametres Query:
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=params)
# URL finale: https://api.github.com/search/repositories?q=python&sort=stars

Gestion Erreurs:
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Leve exception si status >= 400
    data = response.json()
except requests.exceptions.Timeout:
    print("Timeout!")
except requests.exceptions.ConnectionError:
    print("Connection error!")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"Erreur: {e}")

================================================================================

EXERCICES JOUR 1

Exo 1 - Fetch JSON Simple:
Resultat: Fetch user GitHub, affichage JSON
import requests
response = requests.get('https://jsonplaceholder.typicode.com/users/1')
print(response.json())

Exo 2 - Erreur Handling + Argparse:
Resultat: Prend URL en argument, affiche status + 5 premieres lignes si 200, gere 404/timeout
import requests
import argparse

def requete(url: str):
    try:
        response = requests.get(url, timeout=5)
        print(f"Status Code : {response.status_code}")
        if response.status_code == 200:
            lignes = response.text.splitlines()
            for ligne in lignes[:5]:
                print(ligne)
        elif response.status_code == 404:
            print("Page not found")
    except requests.exceptions.Timeout:
        print("Timeout!")
    except requests.exceptions.ConnectionError:
        print("Connection error!")
    except Exception as e:
        print(f"Error: {e}")

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()
requete(args.url)

Exo 3 - Query Parameters:
Resultat: Fetch posts d'un user specifique avec parametres query
response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=1')
posts = response.json()
for post in posts:
    print(f"Titre: {post['title']}")
    print(f"Body: {post['body']}\n")

Exo 4 - GitHub API Parsing:
Resultat: Fetch repos Python top stars, affiche name/stars/description/url
import requests

url = "https://api.github.com/search/repositories?q=python&sort=stars&per_page=5"
header = {'User-Agent': "Mozilla/5.0"}
response = requests.get(url, headers=header)
data = response.json()

for repo in data['items']:
    print(f"{repo['name']} — {repo['stargazers_count']} stars")
    print(f"{repo['description']}")
    print(f"{repo['html_url']}\n")

================================================================================

PIEGES RENCONTRES

Piege 1: AttributeError: module 'requests' has no attribute 'get'
Cause: Fichier nomme requests.py
Solution: Renommer en autre chose

Piege 2: requests.status_codes au lieu du vrai code
Cause: Confusion module vs valeur
Solution: Utiliser response.status_code

Piege 3: Timeout indefini
Cause: Pas de timeout
Solution: Ajouter timeout=5 a chaque request

Piege 4: GitHub 403
Cause: Rate limit (60 req/h sans auth)
Solution: Ajouter User-Agent header

================================================================================

CHECKPOINT AVANT JOUR 2

Comprends la structure request/response - OUI
Peux fetch une API simple - OUI
Geres les erreurs avec try/except - OUI
Sais utiliser headers + params - OUI
