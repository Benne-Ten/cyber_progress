# Semaine 2 — Résumé technique

## Ce que j'ai appris (concepts clés)

### Bash avancé
- find : chercher fichiers selon critères (-name, -type, -mtime, -size, -perm, -user)
- xargs : prendre liste en entrée, passer en arguments (-I {} pour substitution)
- sed : éditer texte en ligne (s/ancien/nouveau/g, -i pour modifier en place)
- awk : traiter fichier ligne par ligne, extraire colonnes, calculer

### Pratique
- Pipes : chaîner commandes (output d'une = input de l'autre)
- Redirects : > (écrire), >> (ajouter), 2>/dev/null (erreurs)
- Permissions : SUID (4000), world-writable (2), octal [owner][group][others]
- Combinaisons : find + exec, awk avec variables/END, xargs avec bash -c

## Ce que je sens solide (niveau 4-5/5)
- 
- 
- 

## Ce que je sens fragile (niveau 1-3/5)
- xargs (1-2/5) : comprends le concept mais syntaxe bash -c relou
- awk (2/5) : calculs simples OK, mais pas d'arrays/groupby
- 
- 

## Prochaines priorités
- Revoir xargs + bash -c (trop de guillemets)
- Awk plus avancé (arrays, groupby)
- Scripts bash réalistes (pas juste one-liners)

## Mini-projets réussis
- File Inventory (bash find + Python CSV/JSON)
- Log parsing (grep + sed + regex)
- Employee sales analysis (awk groupby, xargs fichiers)

## Ce qu'il faut reprendre en semaine 3
- [À compléter selon ressenti]
