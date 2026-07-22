JOUR 5 - GITHUB API + OSINT SOURCE 1
Objectif: Chercher des infos sur un pseudo via GitHub API.

================================================================================

GITHUB API BASICS

Endpoints Cles:
https://api.github.com/users/{username}
Retourne: name, bio, followers, repos_url, avatar_url, etc.

https://api.github.com/users/{username}/repos
Retourne: liste des repos (name, description, stargazers_count, language, html_url)

https://api.github.com/search/repositories?q=python&sort=stars
Retourne: repos matching la search

Response Structure:
{
  "login": "octocat",
  "id": 583231,
  "name": "The Octocat",
  "bio": "Nullam semper...",
  "public_repos": 8,
  "followers": 23342,
  "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4",
  "repos_url": "https://api.github.com/users/octocat/repos",
  ...
}

Rate Limiting:
Sans auth: 60 req/heure
Avec auth: 5000 req/heure
Error: 403 Forbidden si depassé

User-Agent Requirement:
GitHub refuse les requests sans User-Agent.
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

================================================================================

EXERCICES JOUR 5

Exo 1 - Fetch User Info:
Resultat: Affiche name, bio, followers, public_repos, avatar_url
import requests

url = f'https://api.github.com/users/octocat'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
data = response.json()

print(f"Name: {data['name']}")
print(f"Bio: {data['bio']}")
print(f"Followers: {data['followers']}")
print(f"Public Repos: {data['public_repos']}")
print(f"Avatar: {data['avatar_url']}")

Exo 2 - Fetch & Parse Repos:
Resultat: Pour chaque repo: name, description, stars, language, url
repos_url = data['repos_url']
repos_response = requests.get(repos_url, headers=headers)
repos_list = repos_response.json()

for repo in repos_list:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Language: {repo['language']}")
    print(f"URL: {repo['html_url']}\n")

Exo 3 - Combine User + Repos:
Resultat: JSON structure avec user info + repos list

Exo 4 - Error Handling:
Resultat: Gere 404 (user not found) et autres errors
try:
    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code == 404:
        print("User not found")
    elif response.status_code == 403:
        print("Rate limit exceeded")
    else:
        data = response.json()
        # Process...
except requests.exceptions.Timeout:
    print("Timeout")
except Exception as e:
    print(f"Error: {e}")

================================================================================

PIEGES RENCONTRES JOUR 5

Piege 1: 403 Forbidden (Rate Limit)
Cause: Trop de requetes. Dependant de l'adresse IP
Solution tentee: User-Agent header
Resultat: Parfois aide, parfois pas. Peut demander une pause.

Piege 2: Boucler sur URL au lieu de Liste
MAUVAIS:
for repo in data['repos_url']:  # string
    # ...

CORRECT:
repos_response = requests.get(data['repos_url'])
repos_list = repos_response.json()
for repo in repos_list:
    # ...

Piege 3: Accessing Non-Existent Keys
data['starred_url']  # OK
data['stars']        # KeyError - c'est 'stargazers_count'

Piege 4: Typos dans les Keys
data['langage']      # WRONG - c'est 'language'
data['userId']       # WRONG - c'est 'userId' dans JSONPlaceholder

================================================================================

POINTS CLES

Request Flow:
1. Fetch user endpoint
2. Check status (200 = ok, 404 = not found, 403 = rate limit)
3. Parse JSON
4. Acceder aux keys (voir la structure)
5. Fetch repos via repos_url
6. Boucle sur repos_list

Argparse Integration:
parser = argparse.ArgumentParser()
parser.add_argument('--keyword')
parser.add_argument('--output', default='github_result.json')
args = parser.parse_args()

url = f'https://api.github.com/users/{args.keyword}'
# ...
with open(args.output, 'w') as f:
    json.dump(result_dict, f)

Export JSON:
result = {
    "user": {...},
    "repos": [...],
    "total": 5
}
with open('output.json', 'w') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

================================================================================

CHECKPOINT AVANT JOUR 6

Peux fetch user GitHub et afficher infos - OUI
Peux fetch repos et les parser - OUI
Geres les erreurs (404, 403, timeout) - OUI
Exports en JSON structure - OUI
Comprends le rate limit (meme si frustrant) - OUI
