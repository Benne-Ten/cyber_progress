import requests

url = "https://api.github.com/search/repositories?q=python&sort=stars&per_page=5"
header = {'User-Agent' : "Mozilla/5.0"}


response = requests.get(url, headers=header)

data = response.json()

for repo in data['items']:
    print(f"{repo['name']} — {repo['stargazers_count']} stars")
    print(f"{repo['description']}")
    print(f"{repo['html_url']}")
    print()
