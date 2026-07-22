SEMAINE 3 - WEB SCRAPING + OSINT BASICS
Dates: 21 juillet 2026
Objectif: Maitriser requests, BeautifulSoup, integration avec argparse/json pour OSINT

================================================================================

STRUCTURE DE LA SEMAINE

Jour 1: requests - Fetch pages/APIs, gestion erreurs - VALIDÉ
Jour 2: BeautifulSoup - Parser HTML, extraire donnees - VALIDÉ
Jour 3: Révision + Integration - Projet mini scraper posts - VALIDÉ
Jour 4: Design OSINT - Architecture + planning - VALIDÉ
Jour 5: GitHub API - Fetch user/repos data - PARTIELLEMENT (403 limit)
Jour 6: CSV + recherche - DictReader, export JSON - VALIDÉ
Jour 7: Integration complete - Combine 3 sources en 1 script - VALIDÉ

================================================================================

COMPETENCES ACQUISES

Web Scraping:
- Fetch avec requests (GET, status codes, timeout)
- Parse HTML avec BeautifulSoup (find, find_all, CSS selectors)
- Extraire attributs, texte, liens

Data Processing:
- Lire CSV avec csv.DictReader()
- Parser JSON avec response.json()
- Exporter en JSON avec json.dump()

Architecture:
- Argparse multi-arguments (obligatoires + optionnels)
- Combiner plusieurs sources de data
- Structurer outputs complexes

Pieges + Solutions:
- GitHub API 403 (rate limit) - User-Agent header aide pas toujours
- Acces string vs liste dans BeautifulSoup - bien verifier .text vs iteration
- Dict recrees dans boucle - creer dehors, append dedans
- Argparse avec tirets (--user-id) vs code (user_id) - underscore en Python

================================================================================

TOTAL SEMAINE 3

~15 fichiers Python ecrits
APIs testees: GitHub, JSONPlaceholder, HTML scraping
Concepts consolides: requests, BeautifulSoup, argparse, json, csv

================================================================================

PROCHAINE ETAPE: Semaine 4 - Debugging avance + tests + OSINT refinement
