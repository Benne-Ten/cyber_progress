# Jour 3 — Log parsing

## Patterns utilisés
- grep "text" = trouve les lignes avec "text"
- grep -c = compte les occurrences
- Pattern regex IP : [0-9]\+\.[0-9]\+\.[0-9]\+\.[0-9]\+
- sed -i 's/pattern/replacement/g' = remplace dans le fichier

## Cas d'usage réel
Log analysis workflow :
1. Filtrer les erreurs : grep "ERROR"
2. Rediriger dans fichier : > errors_only.log
3. Masquer données sensibles : sed -i avec regex IP
4. Compter occurrences : grep -c

## Commandes jour 3
[ajoute tes commandes qui ont marché]

grep "Failed login" /tmp/app.log | cut -d " " -f 8
	192.168.1.101
	192.168.1.102
	192.168.1.103

echo "$(grep -c "ERROR" /tmp/app.log) [ERROR]" ;  echo "$(grep -c "INFO" /tmp/app.log) [INFO]" ; echo "$(grep -c "WARNING" /tmp/app.log) [WARNING]"
	renvoie :
	4 [ERROR]
	4 [INFO]
	2 [WARNING]

grep "ERROR" /tmp/app.log | sed 's/[0-9]\+\.[0-9]\+\.[0-9]\+\.[0-9]\+/MASKED/g' > /tmp/errors_only.log
	renvoie :
	toto-user@sec-lab:/tmp$ cat error.md
	2025-01-15 10:24:12 [ERROR] Failed login attempt from MASKED
	2025-01-15 10:27:10 [ERROR] Database connection timeout
	2025-01-15 10:29:15 [ERROR] Failed login attempt from MASKED
	2025-01-15 10:32:45 [ERROR] Failed login attempt from MASKED
