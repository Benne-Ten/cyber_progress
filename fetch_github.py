import argparse
import subprocess
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('--keyword')
args = parser.parse_args()

pseudo = args.keyword


url = f'https://api.github.com/users/{pseudo}'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
print(f"Status: {response.status_code}")
if response.status_code == 404:
	print('user not found')
else:
	data = response.json()
	print(data['login'])
	print(data['bio'])
	print(data['repos_url'])
	print(data['followers_url'])
	print(data['following_url'])
	print(data['avatar_url'])

	repos_response = requests.get(data['repos_url'])
	repos_list = repos_response.json()

	response_dict = {
        "user": {}
        'name': data['login'],
        'bio': (data['bio']),
        'followers': data['followers_url'],
        'public repos': data['repos_url'],
	'repos': [],
        'avatar url': data['avatar_url'],
	'total_repos_fetched': 0
        }


	for repo in repos_list:
		repos = requests.get(repo)
		data_url = repos.json()
		print(data_url['name'])
		print(data_url['description'])
		repos_dict = {
		"name": data_url['name'],
		"description": data_url['description'],
		"stars": data_url['stargazers_count'],
		"language": data_url['language'],
		"url": repo
		}
		response_dict['repos'].append(repos_dict)
		response_dict['total_repos_fetched'] += 1


	with open("/home/toto-user/dossier_entrainement/export_github.json", "w", encoding="utf-8") as fichier:
        # indent=4 pour l'indentation, ensure_ascii=False pour les caractères spéciaux
                json.dump(response_dict, fichier, indent=4, ensure_ascii=False, sort_keys=True)
