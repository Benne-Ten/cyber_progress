NAVIGATION

pwd -> donne notre position dans l'arborescence
ls -> donne les fichiers et dossiers présent dans le répertoire -la donner les perms des fichiers et dossiers
cd -> change directory change de répertoire soit cd nom soit cd .. pour revenir avant
mkdir -> créer un dossier
rmdir -> supprime un dossier


FICHIERS

touch -> créer un fichier
cat -> affiche le contenu d'un fichier texte
nano -> ouvre un fichier
cp -> copie de fichier
mv -> permet de bouger un fichier de dossier
rm -> supprime un fichier


PERMISSIONS

chmod -> permet de changer les perms d'un fichier ou dossier = répertoire chmod 777 fichier
	4 = lecture
	2 = écriture
	1 = execution
chown -> donne le propriétaire du fichier
rwx -> read write execute


RECHERCHE

find -> permet de trouver des fichiers/dossiers
grep -> permet de trouver du contenu dans des fichiers


PROCESSUS

ps aux -> affiche les processus du système
kill -> permet de fermer ou tuer un processus sigterm sigkill


PIPES ET REDIRECTIONS

| -> fonction imbriqués int(input())
> -> vide le fichier et écrit dessus
>> -> ajoute du contenu a un fichier (ne le vide pas)
2>/dev/null -> envoie les erreus a la poubelle de linux


ERREURS
bien faire gaffe au chemin relatif vs absolu
