import socket
import random
import os

os.system("clear")
print("//~~ Client Side ~~//")

host, port = ("127.0.0.1", 1337)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# Envoie de la requete SYN :
m = str(random.randint(1000, 2000)) # Definition de l'id SYN
sock.sendall(b"[1] SYN/seq=" + m.encode())

# Reception de la requete SYN-ACK :
synack = sock.recv(1024).decode()
print(synack)

# Envoie de la requete ACK :
n = synack.split("seq=")[1].split(" ")[0] # Recuperation de l'id SYN (qui deviendra l'id ACK)
n = str(int(n) + 1) # Ajout de 1 à l'id SYN
sock.sendall(b"[3] ACK/seq=" + n.encode())