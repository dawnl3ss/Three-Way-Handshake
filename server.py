import socket
import random
import os

os.system("clear")
print("//~~ Server Side ~~//")

host, port = ("127.0.0.1", 1337)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

(client, (host, port)) = sock.accept()

# Reception de la requete SYN :
syn = client.recv(1024).decode()
print(syn)

# Envoie de la requete SYN-ACK :
m = syn.split("seq=")[1] # Recuperation de l'id SYN (qui deviendra l'id ACK)
m = str(int(m) + 1) # Ajout de 1 à l'id SYN
n = str(random.randint(1000, 2000)) # Definition de l'id SYN
client.sendall(b"[2] SYN/seq=" + n.encode() + b" ACK/seq=" + m.encode())

# Reception de la requete ACK :
ack = client.recv(1024).decode()
print(ack)