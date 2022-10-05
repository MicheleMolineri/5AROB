import random, socket

dict,alfabeto = {"a": 0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25," ":26},"abcdefghijklmnopqrstuvwxyz"
dict_invertito = {v: k for k, v in dict.items()}


def generaChiave(parola):
    chiave=""

    for _ in range(len(parola)):
        chiave+=(alfabeto[random.randint(0, len(alfabeto)-1)])
    print(f"Chiave randomica : {chiave}")

    return chiave

def letteraAindice(parola):
    return [dict[i] for i in parola]

def indiceAlettera(parola):
    s=""
    for i in parola:
        s+=dict_invertito[i]
    return s

def codifica(chiave, parola):
    
    chiave = letteraAindice(chiave)
    parola = letteraAindice(parola)
    parolaCifrata  = []

    for i in range(len(parola)):
        parolaCifrata.append((parola[i] + chiave[i]) % len(dict))

    return indiceAlettera(parolaCifrata)

def decodifica(chiave, parola):
    chiave = letteraAindice(chiave)
    parola = letteraAindice(parola)
    parolaDecifrata  = []

    for i in range(len(parola)):
        parolaDecifrata.append((parola[i] - chiave[i]) % len(dict))
    
    return indiceAlettera(parolaDecifrata)

import socket
from threading import Thread

class Reciver(Thread):
    def __init__(self,chiave):
        self.chiave = chiave
        Thread.__init__(self)
        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 5000
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
        self.running = True

    def run(self):
        while self.running:
            msg, addr = self.s.recvfrom(4096)
            print(f"Messaggio Ricevuto: {decodifica(self.chiave,msg.decode())}")

    def stop(self):
        self.running = False





def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = ("192.168.0.136", 5000)
    tutti =("192.168.0.255", 5000)
    io = ("127.0.0.1", 5000)
    chiave = input("Inserisci la chiave: ")
    t1 = Reciver(chiave)
    t1.start()

        
    while True:   
        msg = input("Inserisci il messaggio: ")
        msg = codifica(chiave, msg)
        s.sendto(msg.encode(), server)

if __name__ == "__main__":
    main()