import socket

HOST = ''  # Adresse IP du serveur
PORT = 5000  # Port d'écoute du serveur

# Création d'un objet socket pour le serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur_socket:
    # Liaison de l'adresse IP et du port d'écoute à l'objet socket
    serveur_socket.bind((HOST, PORT))

    # Nombre maximum de connexions en attente
    serveur_socket.listen(1)
    print('Serveur en attente de connexion...')

    # Connexion d'un client
    connexion, adresse_client = serveur_socket.accept()
    print(f'Connexion établie avec {adresse_client}')

    while True:
        # Réception du message du client
        message = connexion.recv(1024).decode()
        print(f'Message reçu : {message}')

        # Traitement du message et envoi de la réponse
        if message.lower() == 'ping':
            reponse = 'pong'
        elif message.lower() == 'pong':
            reponse = 'ping'
        else:
            reponse = 'Message non valide'

        # Envoi de la réponse au client
        connexion.sendall(reponse.encode())
