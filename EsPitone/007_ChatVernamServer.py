import socket,random
from threading import Thread

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

class Reciver(Thread):
    def __init__(self,chiave):
        self.Thread.__init__(self)
        self.chiave = chiave
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea il socket
        self.s.bind(('127.0.0.1', 5000)) # Associa il socket ad una porta
        self.s.listen(5) # Mette il socket in ascolto
        print("Server in ascolto sulla porta 5000")

    def run(self):
        while self.running:
            msg, addr = self.sock.recvfrom(4096)
            print(f"Messaggio Ricevuto: {decodifica(self.chiave,msg.decode())}")

    def stop(self):
        self.running = False


def main():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#tcp
    server = ("192.168.0.136", 5000)
    tutti =("192.168.0.255", 5000)
    io = ("127.0.0.1", 5000)
    

    conn, addr=s.accept() # Accetta la connessione
    print("Connessione accettata da", addr)
    chiave = input("Inserisci la chiave: ")

    t1 = Reciver(chiave)
    t1.start()
    
    while True:
        msg = input("Inserisci il messaggio: ")
        conn.send(codifica(chiave,msg).decode()) # Invia i dati


if __name__ == "__main__":
    main()

