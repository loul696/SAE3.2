import socket
import os
import sys
import platform
import psutil

print("Le serveur est On")
#Initialisation de la connexion entre le client et le serveur

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 4000))
server_socket.listen(1)
#Connexion du client au serveur
while True :
    conn, address = server_socket.accept()
    msg = ""
    data = ""

# Intepretation des commandes "Disconnect" & "Kill"
    while msg != "Kill" and msg != "Disconnect" and data != "Disconnect" and data != "Kill":
        data = conn.recv(1024).decode()
        print(data)
        if msg == 'Kill' or data == 'Kill':
            print("Arrêt du serveur")
            server_socket.close()
        elif msg == 'Disconnect' or data == 'Disconnect':
            print("Déconnection du client")
            conn.close()
#Commande OS qui permet l'affichage du systeme d'exploitation
        elif data == 'os':
            message = f"Votre système est {platform.system()}, et votre version de windows est : {platform.release()}"
            conn.send(message.encode())
#Commande Ram qui affiche la ram, utilisée, libres, totale et les %
        elif data == 'ram':
            message = f"RAM memory : {psutil.virtual_memory()}"
            conn.send(message.encode())
#Affiche le cpu du pc
        elif data == 'cpu':
            message = f"Le CPU est {platform.processor()}"
            conn.send(message.encode())
#Affiche l'ip du poste
        elif data == 'ip':
            message = f"L'adresse ip est {socket.gethostbyname(socket.gethostname())}"
            conn.send(message.encode())
#Commande qui ne fait asbolument rien
        elif data == 'none':
            message = f'La commande ne fait rien'
            conn.send(message.encode())
#Affiche la version de python
        elif data == 'Python --version':
            message = f'Voici la version actuelle de python {sys.version}'
            conn.send(message.encode())
#Affiche les repertoires du disque C
        elif data == 'dir':
            path = "C://"
            dir_list = os.listdir(path)
            message = f'voici le répertoire {dir_list}'
            conn.send(message.encode())
#Renvoie la mauvaise interprétation du commande non renseignée dans le code
        else:
            msg = 'Votre commande existe pas'
            conn.send(msg.encode())
        msg = ""
#Ferme la connexion
    conn.close()

