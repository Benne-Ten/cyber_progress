import csv
import argparse
import json

# Lire
with open('/home/toto-user/dossier_entrainement/osint_database.csv', 'r', encoding='utf-8') as f:
	reader = csv.DictReader(f)  # Parse avec les headers comme keys

	parser = argparse.ArgumentParser()
	parser.add_argument('--keyword')
	args = parser.parse_args()
	keyword = args.keyword

	response_dict = {
                        "keyword": keyword,
                        "results_found": 0,
                        "results": []
                        }

	for row in reader:
		#print(f'Pseudo : {row['pseudo']} | Email : {row['email']} | Nom : {row[ 'nom']}')

		if keyword.lower() in row['pseudo'] or keyword.lower() in row['email'] or keyword.lower() in row['nom']:
			print(f'Pseudo : {row['pseudo']} | Email : {row['email']} | Nom : {row[ 'nom']}')
			result_dict = {"pseudo" : row['pseudo'], "email": row['email'], "nom": row['nom'], "pays": row['pays'],"metier": row['metier']}
			response_dict["results_found"] +=1
			response_dict["results"].append(result_dict)
	print(response_dict)
	with open("/home/toto-user/dossier_entrainement/export_osint_csv.json", "w", encoding="utf-8") as fichier:
        # indent=4 pour l'indentation, ensure_ascii=False pour les caractères spéciaux
                json.dump(response_dict, fichier, indent=4, ensure_ascii=False, sort_keys=True)
