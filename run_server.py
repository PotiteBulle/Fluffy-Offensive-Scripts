#!/usr/bin/python3

# Importation du module serveur 'http.server' et du module de connexion réseau 'socketserver'
import http.server
import socketserver

# Définir le port sur lequel le serveur écoutera 
PORT = 8080 #CHANGE THIS

# Créer un gestionnaire de requêtes HTTP simple
Handler = http.server.SimpleHTTPRequestHandler

def run_server(port):
    """Démarre le serveur HTTP sur le port spécifié."""
    # Utilisation d'un gestionnaire de contexte pour s'assurer que le serveur se ferme correctement
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serveur en cours d'exécution sur le port {port}...")
        try:
            # Maintenir le serveur en cours d'exécution indéfiniment ou jusqu'à ce que vous mettiez fin à la session.
            httpd.serve_forever()
        except KeyboardInterrupt:
            # Gestion d'une interruption clavier pour arrêter le serveur proprement
            print("\nArrêt du serveur.")
            httpd.server_close() # Fermer le server lorsqu'il est arrêté

if __main__ == "__main__":
    # Appeler la fonction pour démarrer le serveur HTTP
    run_server(PORT)
