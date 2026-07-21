import csv
import argparse
import json
from bs4 import BeautifulSoup
import requests


def main():
	# argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--keyword')
	parser.add_argument('--output', default='osint_report.json')
	args = parser.parse_args()
	keyword = args.keyword
	export_fichier = args.output


	# dict final
	response_dict = {
	"keyword": keyword,
	"sources": {
	"csv": [],
	"api" : [],
	},
	"results_found": 0,
	}

	osint_csv(keyword, response_dict)
	osint_html(keyword, response_dict)
	osint_json('https://jsonplaceholder.typicode.com/posts', keyword, 50, response_dict)

	# conversion du dict final en json

	with open(("/home/toto-user/dossier_entrainement/" + export_fichier), "w", encoding="utf-8") as fichier:
	# indent=4 pour l'indentation, ensure_ascii=False pour les caractères spéciaux
        	json.dump(response_dict, fichier, indent=4, ensure_ascii=False, sort_keys=True)

# osint à partir de csv

def osint_csv(keyword, response_dict):
	response_csv = {"results_found": 0}

	with open('/home/toto-user/dossier_entrainement/osint_database.csv', 'r', encoding='utf-8') as f:
		reader = csv.DictReader(f)  # Parse avec les headers comme keys


		for row in reader:

			if keyword.lower() in row['pseudo'] or keyword.lower() in row['email'] or keyword.lower() in row['nom']:
                        	#print(f'Pseudo : {row['pseudo']} | Email : {row['email']} | Nom : {row[ 'nom']}')
				response_csv["pseudo"] =  row['pseudo']
				response_csv["email"] = row['email']
				response_csv["nom"] = row['nom']
				response_csv["pays"] =  row['pays']
				response_csv["metier"] = row['metier']
				response_csv["results_found"] +=1
				response_dict["results_found"] +=1
				response_dict["sources"]['csv'].append(response_csv)


def osint_html(keyword, response_dict):
	response_html ={
	"results_found": 0,
	"results": [],
	}
	url = 'https://example.com'
	response = requests.get(url)

	soup = BeautifulSoup(response.text, 'html.parser')


	h_result = soup.find_all(['h1', 'h2', 'h3'])
	for element in h_result:
		response_html["results"].append(element.text)
		response_html["results_found"] += 1
	p_result = soup.find_all('p')
	for element in p_result:
		response_html["results"].append(element.text)
		response_html["results_found"] += 1
	link_result = soup.find_all('a')
	for element in link_result:
		response_html["results"].append(element.get('href'))
		response_html["results_found"] += 1

	response_dict["html"] = response_html
	response_dict["results_found"] += response_html["results_found"]


def osint_json(url : str, user_id, limit, response_dict):
	response = requests.get(url)
	data = response.json()
	data_dict = {'posts' : []}

	if user_id == None:
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
		data_dict["results_found"] = key
		response_dict["json"] = data_dict
		response_dict["results_found"] += key


if __name__ == '__main__':
	main()


"""
il faut faire une boucle principale qui demande la partie argparse a chaques fois mais pas le plus utile
il faut encore faire la partie api json place holder pour l'instant lien fixe mais pour plus tard lien qui change
il faut faire la partie html beautifulsoup toujours lien fixe mais qui changera plus tard
regarder dans les anciens fichier json place holder et beautiful soup deja surement fait
regrouper tous les réasultat des méthode dans le meme dict qui sera converti en json ensuite
"""
