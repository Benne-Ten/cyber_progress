#!/bin/bash

echo "hello world !"

REPO=${1:-.}

result=$(ls -la "$REPO" | tail -n +2)

echo "$result" > ~/dossier_entrainement/temp.csv

awk '{print $9 "," $5 "," $6 " " $7 " " $8}' ~/dossier_entrainement/temp.csv > ~/dossier_entrainement/inventory.csv
