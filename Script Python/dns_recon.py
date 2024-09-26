# Importation des blibliothèque 'dns.resolver' & 'sys'
import dns.resolver
import sys

def dns_recon(domain):
    """Effectue une reconnaissance DNS pour récupérer les adresses IP associées à un domaine."""
    try:
        # Résoudre les enregistrements A pour le domaine donné
        result = dns.resolver.resolver(domain, 'A')

        # Créer une liste des adresse IP en format TXT
        ip_adresses = [ipval.to_text() for ipval in result]

        # Vérifier si des adresses IP ont été trouver et les afficher
        if ip_adresses:
            print(f'Adresses IP pour {domain}:')
            for ip in ip_adresses:
                print(f' - {ip}') # Afficher chaque adresse IP trouvé

        else:
            print(f'Aucune adresse ip trouver pour {domain}.') # Message si aucunes adresse IP n'est trouvée
    except dns.resolver.NoAnswer: 
        # Gérer le cas où aucune réponse n'est trouvée pour le domaine
        print(f'Aucune réponse trouvée pour {domaine}.')
    except dns.resolver.NXDOMAIN:
        # Gérer le cas où le domaine n'existe pas
        print(f'Le domaine {domain} n\'existe pas.')
    except Exception as e:
        # Gérer toutes les autres exception qui pourrait survenir
        print(f'Erreur: {e}')

def main():
    """Fonction principale pour récuérer le domaine à analyser à partir des arguments de ligne de commande."""
    # Vérifier que l'utilisateurice a fourni un argument de domaine
    if len(sys.argv) != 2:
        print("Usage: python dns_recon.py <DOMAIN>")
        sys.exit(1) # Quitte le programme avec un code d'erreur

    domain = sys.argv[1] # Récupère le domaine passé en argument
    dns_recon(domain) # Appeler la fonction de reconnaisance DNS avec le domaine

if __name__ = "__main__":
    # Exécuter la fonction principale si le script est exécuter directement
    main() 
