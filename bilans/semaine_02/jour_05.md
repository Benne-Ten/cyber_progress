# Jour 5 — Linux CLI révision (angle sécurité)

## Concepts clés
- SUID : permission 4000 (fichier s'exécute avec permissions du propriétaire)
- World-writable : permission 2 (n'importe qui peut écrire)
- `-perm -X` : "au minimum la permission X"
- `-user $USER` : fichiers appartenant à l'utilisateur courant
- `-mmin` : minutes (au lieu de jours avec -mtime)
- Conditions multiples = AND automatique

## Commandes clés

| Commande 
| But 
|
|---
|---
|
| find /usr/bin -perm -4000 -type f | trouver fichiers SUID 
|
| find /etc -perm -2 -type f | trouver fichiers world-writable 
|
| find ~ -user $USER -mmin -120 -ctime -3 -type f | trouver fichiers récents de l'user 
|
| find ... -exec ls -la {} \; | afficher avec permissions et date 
|

## Pièges
- `-perm -2` = "au minimum write pour others", pas juste write exact
- `-perm -6` = "read ET write", plus restrictif que -2
- "and" pas explicite en find : plusieurs critères = AND
- `-mmin` pour minutes, `-mtime` pour jours
- Permissions octal : [owner][group][others]

## Exos réalisés
- Exo 1 : fichiers SUID dans /usr/bin
find ~ -user $USER -mmin -120 -ctime -3 -type f -exec ls -la {} \;

- Exo 2 : fichiers world-writable dans /etc
toto-user@sec-lab:/usr/bin$ find /etc -perm -2 -type f -exec ls -la {} \;

- Exo 3 : fichiers récents de l'user courant
find /usr/bin -perm -4000 -type f -exec ls -la {} \;

