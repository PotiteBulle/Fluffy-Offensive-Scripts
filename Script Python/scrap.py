# Importation du module 'requests' et du module 'BeautifulSoup'
import requests                 
from bs4 import BeautifulSoup    

def scrape_website(url):
    """Récupère le contenu d'une page web et l'affiche sous forme formatée."""
    try:
        response = requests.get(url)  # Envoi de la requête GET à l'URL fournie
        response.raise_for_status()    # Vérifie si la requête a réussi (status 200)
        
        # Analyse du contenu HTML de la réponse
        soup = BeautifulSoup(response.text, 'html.parser')
        # Affiche le HTML formaté
        print(soup.prettify())
        
    except requests.exceptions.HTTPError as http_err:
        # Affiche l'erreur HTTP si la requête échoue
        print(f"Erreur HTTP : {http_err}")
    except requests.exceptions.RequestException as err:
        # Affiche toute autre erreur liée à la requête
        print(f"Erreur lors de la requête : {err}")

if __name__ == "__main__":
    # Demande à l'utilisateurices d'entrer l'URL à scraper
    url = input("Entrez l'URL à scraper : ") 
    scrape_website(url)  # Appelle la fonction de scraping avec l'URL fournie