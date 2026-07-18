# xargs — Apprentissage

## Concept clé
xargs prend une liste (pipe) et la passe en arguments à une commande
-I {} remplace {} par chaque ligne

## Commandes jour 7
| But 
| Commande 
|
|---
|---
|
| Echo chaque ligne | cat file.txt \| xargs echo 
|
| Prefix chaque ligne | cat file.txt \| xargs -I {} echo "Prefix: {}" 
|
| Créer fichiers avec contenu | cat file.txt \| xargs -I {} bash -c 'echo "content {}" > /tmp/{}.txt' 
|

## Pièges
- Quotes en bash relou, chercher la bonne combo
- bash -c nécessaire si commande complexe
- {} doit être entre apostrophes simples dans bash -c
