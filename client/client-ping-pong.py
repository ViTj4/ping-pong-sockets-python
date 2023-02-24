import socket

HOST = 'localhost'  # Adresse IP du serveur
PORT = 5000  # Port d'écoute du serveur

# Création d'un objet socket pour le client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connexion au serveur
    client_socket.connect((HOST, PORT))

    while True:
        # Saisie du message à envoyer
        message = input('Message : ')

        # Envoi du message au serveur
        client_socket.sendall(message.encode())

        # Réception de la réponse du serveur
        reponse = client_socket.recv(1024).decode()
        print(f'Reponse : {reponse}')
