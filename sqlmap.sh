#!/bin/bash

# Vérifier si l'URL cible est fournie
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <TARGET_URL>"
    exit 1
fi

# URL de la cible vulnérable
TARGET = "$1"

# Exécuter SQLMAP pour détecter les bases de données vulnérable
# -u : spécifie l'URL cible
# --dbs : récupère la liste des bases de données
# --batch : exécute en mode automatique, sans demande d'interaction
# --risk=3 : augmente le niveau de risque pour des tests plus complets (ajuster selon les besoins)
# --level=5 : augmente le niveau de test pour une couverture plus large

sqlmap -u "TARGET" --dbs --batch --risk=3 --level=5