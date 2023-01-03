import socket

print("Le client est connecté")

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("localhost", 4000))
#Etablie la connexion entre le serveur et le client

msg = ""

data = ""

while msg.lower() != "Kill" and msg != "Disconnect" and data != "Disconnect" and data != "Kill":
    msg = input("--> ")
    if msg == "Disconnect" or data == 'Disconnect':
        print("Vous allez être déconnecté")
        rep = input("continuer (y/n)")
        if rep == "y":
            print("Déconnection")
            client_socket.send(msg.encode())
            exit()
#Interprétation des commandes "Disconnect" & "Kill"
    elif msg == 'Kill' or data == 'Kill':
        print("Arrêt du serveur")
        client_socket.send(msg.encode())
    elif msg == 'Reset' or data == 'Reset':
        print("Les systèmes vont redemarrer")
        client_socket.send(msg.encode())
    else:
        client_socket.send(msg.encode())
    data = client_socket.recv(1024).decode()
    print(data)
#Coupe la connexion entre le client et le seuveur
client_socket.close()
