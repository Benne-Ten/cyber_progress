import requests
import json
import argparse

def fetch_json(url : str, user_id, limit):
	response = requests.get(url)
	data = response.json()
	data_dict = {'posts' : []}

	if user_id == None:

		print(response.status_code)

		for i in range(0, limit):
			print(data[i])
			data_dict['posts'].append(data[i])

	else :
		key = 0
		i = 0
		while key != limit and i < len(data):
			if data[i]['userId'] == user_id:
				key += 1
				print(data[i])
				data_dict['posts'].append(data[i])
			i += 1


	with open("/home/toto-user/dossier_entrainement/export.json", "w", encoding="utf-8") as fichier:
	# indent=4 pour l'indentation, ensure_ascii=False pour les caractères spéciaux
		json.dump(data_dict, fichier, indent=4, ensure_ascii=False, sort_keys=True)


parser = argparse.ArgumentParser()

parser.add_argument('url')
parser.add_argument('--user-id', type=int, default=None)
parser.add_argument('--limit', type=int, default=10)
parser.add_argument('--output', type=str, default='posts.json')

args = parser.parse_args()

# Utilisation
print(args.url)        # Obligatoire, tu l'as toujours
url = args.url
print(args.user_id)    # None si pas fourni, sinon la valeur
user_id = args.user_id
print(args.limit)      # 10 par défaut, ou la valeur passée
limit = args.limit
print(args.output)     # 'posts.json' par défaut

fetch_json(url, user_id, limit)
