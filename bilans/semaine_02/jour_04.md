# Jour 4 — Pipes complexes + awk

## Concepts clés
- awk : extraire colonnes ($1, $2, $NF = dernière colonne)
- Variables en awk (sum += $3)
- END block : exécuter du code à la fin
- OFS : séparateur de colonnes en output
- NR : nombre de lignes

## Commandes clés

| Commande 
| But 
|
|---
|---
|
| ls -lS | trier fichiers par taille (descending) 
|
| awk '{print $5, $NF}' | extraire colonne 5 et dernière 
|
| awk 'BEGIN{OFS=","} {print $1, $2}' | output avec virgules 
| awk {print $1 "," $2 " " $3}' | output avec virgules et espaces
|
| awk '{sum += $3} END {print sum/NR}' | calculer moyenne colonne 3 
|

## Pièges
- OFS change le séparateur mais tu peux aussi concaténer avec "" dans print
- END block s'exécute une fois à la fin (pas à chaque ligne)
- NR = nombre de lignes (utile pour moyennes)

## Exos réalisés
- Exo 1 : extraire fichiers + tailles
ls -lS /var/log/*.log | awk '{print $5, $NF}'

- Exo 2 : créer CSV avec awk
awk '{print $9 "," $5 "," $6 " " $7 " " $8}' files_info.txt > inventory.csv

- Exo 3 : calculer moyenne avec sum et NR
awk '{sum += $3} END {print "Moyenne : " sum/NR}' sales.txt
