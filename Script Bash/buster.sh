#!/bin/bash

# Définir la cible
TARGET="http://example.com" # CHANGE THIS

# Liste des fichiers de wordlists
WORDLISTS=( # Wordlist avec DIRB. Adaptez la wordlist en fonction de vos besoins.
    "/usr/share/wordlists/dirb/common.txt"
    "/usr/share/wordlists/dirb/big.txt"
    "/usr/share/wordlists/dirb/small.txt"
    "/usr/share/wordlists/dirb/euskera.txt"
    "/usr/share/wordlists/dirb/extensions_common.txt"
    "/usr/share/wordlists/dirb/indexes.txt"
    "/usr/share/wordlists/dirb/mutations_common.txt"
    "/usr/share/wordlists/dirb/catala.txt"
)

# Boucle sur chaque wordlist
for WORDLIST in "${WORDLISTS[@]}"; do
    echo "Utilisation de la wordlist: $WORDLIST"
    gobuster dir -u $TARGET -w $WORDLIST
done