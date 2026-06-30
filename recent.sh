#!/bin/bash
i=0
total_size=0
for fichier in $(find ~/dossier_entrainement/ -mtime -1)
do
  # faire quelque chose avec $fichier
  ls -lh $fichier
  i=$((i+1))
  taille=$(stat -c %s $fichier)
  total_size=$((total_size+$taille))
done
echo "Total de fichiers trouvés : $i"
echo "Taille totale des fichiers trouvé : $total_size"
