# awk — Apprentissage

## Concept clé
awk traite fichiers ligne par ligne, extraie colonnes ($1, $2, $NF), calcule

## Commandes jour 8
| But | Commande 
|
|---
|---
|
| Extraire colonnes 
| awk '{print $1, $3}' file 
|
| Calculer dans output | awk '{print $1, $3 * 1.1}' file 
|
| Moyenne colonne | awk '{sum+=$3; n++} END {print sum/n}' file 
|

## Pièges
- Espaces autour de $1, $2 dans print changent l'output (cosmétique mais relou)
- Boucle implicite : awk répète pour chaque ligne
- END block s'exécute une fois à la fin
- n++ équivalent de n+=1
