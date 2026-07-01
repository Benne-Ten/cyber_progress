import subprocess
import argparse
import os

def recent_file(chemin : str):
	path = os.path.expanduser(chemin)
	result = subprocess.run(["find", path,  "-mtime", "-1"], capture_output=True, text=True)
	result = result.stdout
	lst_result = result.split("\n")
	nb_result = 0
	taille_result = 0
	for item in lst_result:
		nb_result += 1
		print(os.path.join(path, item))
		#ls -lh $fichier
		#result_ls =  subprocess.run(["ls", "-lh", item], capture_output=True, text=True)
		#result_ls = result_ls.stdout
		#result_ls_lst = result_ls.split()
		#print(result_ls_lst)
		#taille_result += int(result_ls_lst[6])
		taille_result += os.path.getsize(os.path.join(path, item))
	return(nb_result, taille_result)


chemin = argparse.ArgumentParser()
chemin.add_argument("--directory")
arg = chemin.parse_args()
print(recent_file(arg.directory))
