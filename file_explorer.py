import os
path = os.path.expanduser("~/dossier_entrainement/")
items = os.listdir(path)
lst_dossier = []
for item in items:
	if os.path.isfile(item):
		lst_dossier.append(item) #.append(os.path.join(path, item)) car permet de lancer le fichier de
#n'importe sinon si on lance ca autre par ca va juste crash
print(lst_dossier)
