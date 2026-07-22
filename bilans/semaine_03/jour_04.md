JOUR 4 - DESIGN OSINT + PLANNING
Objectif: Planifier le projet OSINT. Architecture, scope, donnees sources.

================================================================================

CONCEPTS OSINT

OSINT = Open Source Intelligence
Collect publically available info sur une cible (personne, orga, domaine) via:
- APIs publiques
- Bases de donnees accessibles
- Web scraping
- Moteurs de recherche
- Reseaux sociaux, GitHub, etc.

================================================================================

DESIGN DU PROJET SEMAINE 3

Scope:
Input: Un mot cle (pseudo, email, nom)
Output: Rapport consolide en JSON avec resultats de 3 sources

Architecture:

osint_tool.py
├─ argparse
│   ├─ --keyword (obligatoire)
│   └─ --output (optionnel)
├─ Fonction search_csv()
│   └─ Cherche dans base de donnees locale
├─ Fonction search_api()
│   └─ Cherche sur API (JSONPlaceholder)
├─ Fonction search_web()
│   └─ Scrape une page HTML (BeautifulSoup)
├─ Fonction main()
│   └─ Combine tout + exporte JSON
└─ if __name__ == '__main__'
    └─ Lance main()

================================================================================

SOURCES DE DATA

Source 1: CSV Local
- Fichier: osint_database.csv
- Contient: pseudo, email, nom, pays, metier
- Recherche: keyword dans n'importe quel champ

Source 2: API JSONPlaceholder
- Endpoint: https://jsonplaceholder.typicode.com/users
- Contient: user info (name, email, username)
- Recherche: keyword dans name/username/email

Source 3: Web Scraping
- Site: https://example.com
- Parse: headings (<h1>, <h2>, <h3>), paragraphes (<p>), liens (<a>)
- Recherche: keyword dans le contenu

================================================================================

STRUCTURE JSON OUTPUT (OPTION A)

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
      "total": 1,
      "results": [
        {
          "tag": "h1",
          "content": "Example Domain",
          "url": "https://example.com"
        }
      ]
    }
  }
}

================================================================================

ARCHITECTURE DETAILLEE

main():
1. Parse argparse
2. Cree le dict vide avec structure Option A
3. Appelle search_csv(keyword, response_dict)
4. Appelle search_api(keyword, response_dict)
5. Appelle search_web(keyword, response_dict)
6. Export JSON

search_csv(keyword, response_dict):
- Ouvre le CSV
- Boucle sur chaque row
- Si keyword match, cree un dict avec les infos
- Append a response_dict['sources']['csv']['results']
- Increment response_dict['sources']['csv']['total']

search_api(keyword, response_dict):
- Fetch https://jsonplaceholder.typicode.com/users
- Pour chaque user, verifie si keyword est dans name/username/email
- Si match, ajoute a response_dict['sources']['api']['results']
- Increment total

search_web(keyword, response_dict):
- Fetch https://example.com
- Parse avec BeautifulSoup
- Cherche keyword dans h1/h2/h3/p
- Pour chaque match, ajoute dict avec tag/content/url
- Increment total

================================================================================

PATTERNS CLES

Modifier un Dict Depuis une Fonction:

def update_dict(keyword, response_dict):
    response_dict['sources']['csv']['results'].append({...})
    response_dict['sources']['csv']['total'] += 1

response_dict = {"sources": {"csv": {"total": 0, "results": []}}}
update_dict("alice", response_dict)
# response_dict est modifie en place (pas besoin de retourner)

Combiner Plusieurs Sources:

# Chaque fonction ajoute ses resultats au meme dict
search_csv(keyword, response_dict)
search_api(keyword, response_dict)
search_web(keyword, response_dict)
# response_dict contient maintenant les 3 sources

================================================================================

NOTES IMPORTANTES

Pourquoi 3 Sources?
- CSV: Maitrise totale des donnees, pas de rate limit
- API: Donnees externes (JSONPlaceholder comme exemple)
- Web: Pratique du scraping realiste

Rate Limits a Gerer:
- GitHub API: 60 req/h sans auth
- JSONPlaceholder: pas de limite (fake API)
- HTML scraping: depend du site (example.com pas de limit)

Extensibilite:
Pour ajouter une 4e source (ex: Twitter, HaveIBeenPwned):
1. Creer fonction search_twitter(keyword, response_dict)
2. Ajouter "twitter" a la structure dict
3. Appeler dans main()

================================================================================

CHECKPOINT AVANT JOUR 5

Comprends la structure Option A - OUI
Sais comment les 3 fonctions modifient le dict - OUI
Peux dessiner l'architecture sur papier - OUI
Sais quoi fetch de chaque source - OUI
