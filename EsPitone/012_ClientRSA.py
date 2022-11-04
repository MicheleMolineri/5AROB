import socket
from threading import Thread
import RSA

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.0.112",5000))
data = s.recv(4096)
print(data.decode())

while True:
    s.sendall(input("inserisci un messaggio : ").encode())

