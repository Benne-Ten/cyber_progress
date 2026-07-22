JOUR 3 - REVISION + MINI-PROJET INTEGRATION
Objectif: Consolider requests + json, faire un mini-projet complet (fetch + parse + export)

================================================================================

DE MEMOIRE (REVISION)

L'exo 1 demandait de refaire sans regarder les anciens fichiers:
- Argparse pour prendre URL
- Fetch avec requests
- Parse JSON
- Afficher infos structurees

Piege: Oublier d'appeler response.json() au lieu de juste afficher le dict brut

================================================================================

MINI-PROJET: SCRAPER POSTS

Specs:
- Fetch l'API: https://jsonplaceholder.typicode.com/posts
- Pour chaque post: garder id, title, body, userId
- Exporter en JSON
- Argparse:
  --user-id (optionnel): filtrer par user
  --limit (optionnel, defaut 10): nombre de posts
  --output (optionnel, defaut posts.json): nom fichier

CODE COMPLET:

import requests
import json
import argparse

def fetch_json(url: str, user_id, limit, output_file):
    response = requests.get(url)
    data = response.json()
    data_dict = {'posts': []}
    
    if user_id is None:
        # Tous les posts, limites par limit
        print(f"Status: {response.status_code}")
        for i in range(0, limit):
            if i < len(data):
                data_dict['posts'].append(data[i])
    else:
        # Filtrer par userId
        key = 0
        i = 0
        while key != limit and i < len(data):
            if data[i]['userId'] == user_id:
                key += 1
                data_dict['posts'].append(data[i])
            i += 1
    
    # Ajouter le compte total
    data_dict['total_posts'] = len(data_dict['posts'])
    
    # Exporter en JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)
    
    print(f"Exported {data_dict['total_posts']} posts to {output_file}")

# Argparse
parser = argparse.ArgumentParser()
parser.add_argument('url')
parser.add_argument('--user-id', type=int, default=None)
parser.add_argument('--limit', type=int, default=10)
parser.add_argument('--output', type=str, default='posts.json')
args = parser.parse_args()

# Execution
fetch_json(args.url, args.user_id, args.limit, args.output)

USAGES:

# Tous les posts (10 par defaut)
python3 script.py https://jsonplaceholder.typicode.com/posts

# Posts de l'user 2, limite a 5
python3 script.py https://jsonplaceholder.typicode.com/posts --user-id 2 --limit 5

# Custom output
python3 script.py https://jsonplaceholder.typicode.com/posts --output result.json

OUTPUT JSON:

{
    "posts": [
        {
            "id": 1,
            "title": "sunt aut facere...",
            "body": "quia et suscipit...",
            "userId": 1
        },
        {
            "id": 2,
            "title": "qui est esse",
            "body": "est rerum tempore...",
            "userId": 1
        }
    ],
    "total_posts": 10
}

================================================================================

POINTS CLES DE CE JOUR

Argparse Recap:
# Obligatoire (pas de tirets)
parser.add_argument('url')

# Optionnel (avec tirets)
parser.add_argument('--user-id', type=int, default=None)
parser.add_argument('--limit', type=int, default=10)

Response -> Dict:
response = requests.get('...')
data = response.json()  # Automatic conversion

Filtrer Une Liste:
# Condition dans boucle
for item in data:
    if item['userId'] == user_id:
        # Garder cet item

Export JSON:
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, indent=4, ensure_ascii=False)

================================================================================

PIEGES CE JOUR

Piege 1: Dict cree dans la boucle
Cause: Reinit a chaque iteration
Solution: Creer dehors, append dedans

Piege 2: response_dict['results'] n'existe pas
Cause: Pas initialise au depart
Solution: Initialiser la structure complete

Piege 3: .lower() sur None
Cause: Texte peut etre None
Solution: Ajouter if text: avant .lower()

Piege 4: File path hardcode
Cause: Pas flexible
Solution: Utiliser argparse pour output

================================================================================

CHECKPOINT AVANT JOUR 4

Comprends argparse multi-arguments - OUI
Peux filtrer une liste JSON avec condition - OUI
Exportes en JSON avec bonne structure - OUI
Peux ecrire le mini-projet from scratch - OUI
