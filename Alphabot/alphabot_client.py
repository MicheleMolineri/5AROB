import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_alphabot = ("192.168.0.122",8000)
s.connect(ip_alphabot)

data = s.recv(4096)
print(data.decode())

while True :
    comando = input("Inserisci il comando : ")
    s.sendall(comando.encode())
    if comando == "exit":
        break
    
s.close()
