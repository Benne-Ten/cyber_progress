JOUR 6 - CSV LOCAL SEARCH + OSINT SOURCE 2
Objectif: Creer une base de donnees CSV, la chercher, exporter les resultats en JSON.

================================================================================

FORMAT CSV

pseudo,email,nom,pays,metier
alice123,alice@mail.com,Alice Martin,France,Dev
bob_dev,bob@work.com,Bob Johnson,USA,Admin
charlie77,charlie.b@mail.com,Charles Brown,UK,Pentester
diana_sec,diana@company.com,Diana Prince,Canada,Security
echo_pro,echo@pro.dev,Echo Smith,Germany,Hacker

csv.DictReader():

import csv

with open('osint_database.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['pseudo'])  # row est un dict avec headers comme keys
        print(row['email'])

Boucler + Condition:

for row in reader:
    if 'keyword' in row['pseudo'].lower() or \
       'keyword' in row['email'].lower() or \
       'keyword' in row['nom'].lower():
        print(f"Match: {row['pseudo']}")

================================================================================

EXERCICES JOUR 6

Exo 1 - Lire CSV Basique:
Resultat: Affiche chaque ligne formatee
import csv

with open('osint_database.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Pseudo: {row['pseudo']} | Email: {row['email']} | Nom: {row['nom']}")

Exo 2 - Chercher par Mot Cle:
Resultat: Argparse pour keyword, affiche les matches
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--keyword')
args = parser.parse_args()
keyword = args.keyword

with open('osint_database.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if keyword.lower() in row['pseudo'].lower() or \
           keyword.lower() in row['email'].lower() or \
           keyword.lower() in row['nom'].lower():
            print(f"Pseudo: {row['pseudo']} | Email: {row['email']} | Nom: {row['nom']}")

Exo 3 - Export en JSON:
Resultat: Cherche + exporte en JSON structure
import csv
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--keyword')
parser.add_argument('--output', default='osint_csv_result.json')
args = parser.parse_args()

response_dict = {
    "keyword": args.keyword,
    "results_found": 0,
    "results": []
}

with open('osint_database.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if args.keyword.lower() in row['pseudo'].lower() or \
           args.keyword.lower() in row['email'].lower() or \
           args.keyword.lower() in row['nom'].lower():
            result_dict = {
                "pseudo": row['pseudo'],
                "email": row['email'],
                "nom": row['nom'],
                "pays": row['pays'],
                "metier": row['metier']
            }
            response_dict["results"].append(result_dict)
            response_dict["results_found"] += 1

with open(args.output, 'w', encoding='utf-8') as f:
    json.dump(response_dict, f, indent=4, ensure_ascii=False)

print(f"Found {response_dict['results_found']} results in CSV")

OUTPUT JSON:

{
    "keyword": "alice",
    "results_found": 1,
    "results": [
        {
            "pseudo": "alice123",
            "email": "alice@mail.com",
            "nom": "Alice Martin",
            "pays": "France",
            "metier": "Dev"
        }
    ]
}

================================================================================

POINTS CLES

Dict Cree Dehors de la Boucle:

WRONG:
for row in reader:
    response_dict = {"results": []}  # Recreated every iteration
    # ...
    response_dict["results"].append(...)

CORRECT:
response_dict = {"results": []}  # Created once
for row in reader:
    if match:
        response_dict["results"].append(...)

Case-Insensitive Search:

if keyword.lower() in row['pseudo'].lower():
    # Matching "Alice" avec "ALICE" ou "alice"

Initialiser le CSV:

import csv

data = [
    ['pseudo', 'email', 'nom', 'pays', 'metier'],
    ['alice123', 'alice@mail.com', 'Alice Martin', 'France', 'Dev'],
    ['bob_dev', 'bob@work.com', 'Bob Johnson', 'USA', 'Admin'],
]

with open('osint_database.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

================================================================================

PIEGES JOUR 6

Piege 1: Dict recreated in loop
Cause: Oubli de creer dehors
Solution: Initialiser avant la boucle

Piege 2: .lower() sur None
Cause: Certains champs peuvent etre vides
Solution: Ajouter check if row['field']:

Piege 3: KeyError sur une cle
Cause: Typo dans le nom de colonne
Solution: Verifier les headers CSV

Piege 4: File path hardcoded
Cause: Pas flexible
Solution: Utiliser argparse --output

================================================================================

NOTA BENE

Avantages CSV vs API:
- Pas de rate limit
- Controle total sur les donnees
- Rapide a tester

Limitations:
- Donnees limitees a ce qu'on a cree

Pour OSINT Reel:
On pourrait avoir CSVs de:
- Breached databases (HaveIBeenPwned dumps)
- Leaked credentials
- Company employees listes
- Social media profiles

================================================================================

CHECKPOINT AVANT JOUR 7

Peux lire un CSV et boucler dessus - OUI
Sais faire une recherche case-insensitive - OUI
Exportes les resultats en JSON - OUI
Utilises argparse pour keyword + output - OUI
