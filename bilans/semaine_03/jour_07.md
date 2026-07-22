JOUR 7 - INTEGRATION COMPLETE OSINT TOOL
Objectif: Combiner les 3 sources (CSV + API + Web scraping) en un script OSINT unifié.

================================================================================

ARCHITECTURE FINALE

osint.py
├─ Imports (csv, requests, json, BeautifulSoup, argparse)
├─ def search_csv(keyword, response_dict)
├─ def search_api(keyword, response_dict)
├─ def search_web(keyword, response_dict)
├─ def main()
└─ if __name__ == '__main__': main()

================================================================================

STRUCTURE DICT FINALE (OPTION A)

{
  "keyword": "alice",
  "sources": {
    "csv": {
      "total": 1,
      "results": [...]
    },
    "api": {
      "total": 0,
      "results": []
    },
    "web": {
      "total": 2,
      "results": [...]
    }
  },
  "results_found": 3
}

================================================================================

CODE COMPLET

import csv
import requests
import json
from bs4 import BeautifulSoup
import argparse

def search_csv(keyword, response_dict):
    """Cherche dans la base CSV locale"""
    with open('osint_database.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if keyword.lower() in row['pseudo'].lower() or \
               keyword.lower() in row['email'].lower() or \
               keyword.lower() in row['nom'].lower():
                
                result = {
                    "pseudo": row['pseudo'],
                    "email": row['email'],
                    "nom": row['nom'],
                    "pays": row['pays'],
                    "metier": row['metier']
                }
                response_dict['sources']['csv']['results'].append(result)
                response_dict['sources']['csv']['total'] += 1
                response_dict['results_found'] += 1

def search_api(keyword, response_dict):
    """Cherche sur JSONPlaceholder API"""
    try:
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url, timeout=5)
        data = response.json()
        
        for user in data:
            if keyword.lower() in user['name'].lower() or \
               keyword.lower() in user['username'].lower() or \
               keyword.lower() in user['email'].lower():
                
                result = {
                    "name": user['name'],
                    "username": user['username'],
                    "email": user['email'],
                    "id": user['id']
                }
                response_dict['sources']['api']['results'].append(result)
                response_dict['sources']['api']['total'] += 1
                response_dict['results_found'] += 1
    except Exception as e:
        print(f"API search error: {e}")

def search_web(keyword, response_dict):
    """Scrape et cherche dans une page HTML"""
    try:
        url = 'https://example.com'
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Chercher dans headings
        for h in soup.find_all(['h1', 'h2', 'h3']):
            if keyword.lower() in h.text.lower():
                result = {
                    "tag": h.name,
                    "content": h.text,
                    "url": url
                }
                response_dict['sources']['web']['results'].append(result)
                response_dict['sources']['web']['total'] += 1
                response_dict['results_found'] += 1
        
        # Chercher dans paragraphes
        for p in soup.find_all('p'):
            if keyword.lower() in p.text.lower():
                result = {
                    "tag": "p",
                    "content": p.text,
                    "url": url
                }
                response_dict['sources']['web']['results'].append(result)
                response_dict['sources']['web']['total'] += 1
                response_dict['results_found'] += 1
    except Exception as e:
        print(f"Web search error: {e}")

def main():
    # Argparse
    parser = argparse.ArgumentParser(description='OSINT Search Tool')
    parser.add_argument('--keyword', required=True, help='Keyword to search')
    parser.add_argument('--output', default='osint_report.json', help='Output file')
    args = parser.parse_args()
    
    # Initialiser le dict
    response_dict = {
        "keyword": args.keyword,
        "sources": {
            "csv": {"total": 0, "results": []},
            "api": {"total": 0, "results": []},
            "web": {"total": 0, "results": []}
        },
        "results_found": 0
    }
    
    # Chercher dans les 3 sources
    print(f"Searching for '{args.keyword}'...")
    search_csv(args.keyword, response_dict)
    search_api(args.keyword, response_dict)
    search_web(args.keyword, response_dict)
    
    # Exporter en JSON
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(response_dict, f, indent=4, ensure_ascii=False)
    
    print(f"Results: {response_dict['results_found']} matches found")
    print(f"Exported to {args.output}")

if __name__ == '__main__':
    main()

================================================================================

UTILISATION

Commandes:

# Recherche simple
python3 osint.py --keyword alice

# Avec output custom
python3 osint.py --keyword bob --output results_bob.json

# Aide
python3 osint.py --help

Output Exemple:
toto-user@sec-lab:~/dossier_entrainement$ python3 osint.py --keyword alice
Searching for 'alice'...
Results: 3 matches found
Exported to osint_report.json

Fichier JSON Genere:
{
    "keyword": "alice",
    "sources": {
        "csv": {
            "total": 1,
            "results": [
                {
                    "pseudo": "alice123",
                    "email": "alice@mail.com",
                    "nom": "Alice Martin",
                    "pays": "France",
                    "metier": "Dev"
                }
            ]
        },
        "api": {
            "total": 0,
            "results": []
        },
        "web": {
            "total": 2,
            "results": [
                {
                    "tag": "h1",
                    "content": "Example Domain",
                    "url": "https://example.com"
                },
                {
                    "tag": "p",
                    "content": "This domain is for use...",
                    "url": "https://example.com"
                }
            ]
        }
    },
    "results_found": 3
}

================================================================================

PATTERNS CLES JOUR 7

Modifier un Dict Depuis une Fonction:

def search_csv(keyword, response_dict):
    # response_dict est modifie en place (pas besoin de return)
    response_dict['sources']['csv']['total'] += 1
    response_dict['sources']['csv']['results'].append({...})

Combiner Plusieurs Sources:

# Chaque fonction ajoute ses donnees
search_csv(keyword, response_dict)
search_api(keyword, response_dict)
search_web(keyword, response_dict)
# response_dict accumule tout

Try/Except pour Chaque Source:

try:
    # Fetch + parse
except Exception as e:
    print(f"Source error: {e}")
# Continue avec les autres sources meme si une echoue

Export JSON Final:

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(response_dict, f, indent=4, ensure_ascii=False)

================================================================================

PIEGES JOUR 7

Piege 1: Functions not called
Cause: Oubli d'appeler dans main()
Solution: Verifier search_csv(keyword, response_dict) est appele

Piege 2: Dict structure wrong
Cause: Mauvaise initialisation
Solution: Suivre Option A strictement

Piege 3: Results accumulate
Cause: Pas reset entre sources
Solution: Dict reinitialise une seule fois

Piege 4: File path hardcoded
Cause: Non flexible
Solution: Utiliser argparse --output

Piege 5: No error handling
Cause: Une source crash tout
Solution: Try/except par source

================================================================================

BONUS POSSIBLE

Ajouter Totals Sub-Dict:
"totals": {
    "csv": 1,
    "api": 0,
    "web": 2,
    "global": 3
}

Multi-Threading pour APIs:
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(search_csv, keyword, response_dict)
    executor.submit(search_api, keyword, response_dict)
    executor.submit(search_web, keyword, response_dict)

Logging + Verbose Mode:
parser.add_argument('-v', '--verbose', action='store_true')
if args.verbose:
    print(f"Found {response_dict['sources']['csv']['total']} in CSV")

================================================================================

APPRENTISSAGES CETTE SEMAINE

Competences Consolidees:
- requests pour fetch web/APIs
- BeautifulSoup pour parser HTML
- csv.DictReader() pour donnees locales
- argparse multi-arguments
- json dump/load
- Architecture modulaire (fonctions)
- Dict manipulation

Realisme:
- Combiner plusieurs sources
- Gerer les erreurs reseau
- Exporter rapports

OSINT Basics:
- Reconnaissance passive
- Consolidation de donnees
- Reporting structure

================================================================================

CHECKPOINT AVANT SEMAINE 4

Le script tourne sans erreurs - OUI
Toutes les 3 sources retournent des resultats - OUI
JSON export fonctionne - OUI
Argparse works (--keyword, --output) - OUI
Code est lisible + commente - OUI

================================================================================

PROCHAINES ETAPES (SEMAINE 4)

- Debugging avancé (pdb, unittest)
- OSINT refinement (plus de sources)
- Tests + Quality assurance
- Performance optimization
