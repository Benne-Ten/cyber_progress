import os
import csv


path = os.path.expanduser("~/dossier_entrainement/")

with open(os.path.join(path, 'inventory.csv'), 'r', encoding='utf-8') as f:
	reader = csv.reader(f)

	nb_lignes = 0
	nb_large_files = 0
	list_files = []

	for ligne in reader:
		nb_lignes += 1

		if int(ligne[1]) >= 1000:
			nb_large_files += 1
		file = {"path": os.path.join(path, ligne[0]), "size": ligne[1], "date": ligne[2]}
		list_files.append(file)


	report = {"total_files": nb_lignes, "large_files": nb_large_files, "files": list_files}
print(report)
