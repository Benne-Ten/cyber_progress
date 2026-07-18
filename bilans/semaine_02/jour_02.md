# Jour 2 — xargs et sed

## Ce que j'ai appris
- xargs : prend une liste (pipe) et la passe en arguments
- xargs -I {} : remplace {} par chaque ligne
- sed : remplace du texte
- sed 's/ancien/nouveau/g' : syntaxe substitution (g = global)
- sed -i : modifie le fichier en place

## Commandes clés
| Commande 
| But 
| Exemple 
|
|---
|---
|---
|
| xargs mkdir -p 
| créer dossiers à partir liste 
| cat list.txt \| xargs mkdir -p 
|
| xargs -I {} | remplacer {} par chaque ligne | xargs -I {} echo {} 
|
| sed 's/X/Y/g' | remplacer X par Y (affiche) | sed 's/localhost/127.0.0.1/g' 
|
| sed -i 's/X/Y/g' | remplacer X par Y (modifie) | sed -i 's/Backup/archive/g' *.txt 
|
| sed sur * | modifier tous fichiers | sed -i 's/X/Y/g' /path/* 
|

## Pièges
- sed sans -i affiche juste le résultat, ne modifie pas
- xargs sans -I {} passe juste les mots en arguments (bon pour mkdir, touch)
- xargs -I {} nécessite bash -c si tu dois faire du multi-commande
