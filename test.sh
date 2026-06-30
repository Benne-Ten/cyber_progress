#!/bin/bash
if [ -f /etc/passwd ]
then
  echo "Le fichier existe"
else
  echo "Le fichier n'existe pas"
fi
