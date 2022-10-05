import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", 5000))

    f = open("file.csv", "r")
    righe = f.readlines()
    f.close()
    contatti = {}

    for riga in righe:
        persona = riga.split(",")
        nome = str(persona[0])
        indirizzo = str(persona[1][:-1])
        contatti[nome] = indirizzo
    print(contatti)

    while True:
        msg, ind_client = s.recvfrom(4096)
        msgDiviso = msg.decode().split("|")
        print(f"{msg.decode()} inviato da {msgDiviso[1]}") 

        msgFinale = msgDiviso[0]
        ip = contatti[msgDiviso[1]]
        
        s.sendto(msgFinale.encode(), (ip, 5000))

if __name__ == "__main__":
    main()