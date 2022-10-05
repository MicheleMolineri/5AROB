import random

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

def main():
    
    parola=input("inserisci parola :")
    s=input("Voui codificare una parola o decodificarla ? c/d : ")
    if s == "c":
        scelta=input("Genera chiave randomica? y/n : ")
        if scelta=="y" or scelta=="Y":
            chiave=generaChiave(parola)
        else:
            chiave=input("inserisci chiave : ")
        parolaCifrata = codifica(chiave, parola)
        parolaDecifrata = decodifica(chiave, parolaCifrata)
        print(f"Parola cifrata : {parolaCifrata}\nParola decifrata : {parolaDecifrata}")
    elif s=="d":
        parolaCifrata=input("inserisci parola cifrata :")
        chiave=input("inserisci chiave : ")
        parolaDecifrata = decodifica(chiave, parolaCifrata)
        print(f"Parola decifrata : {parolaDecifrata}")



if __name__ == "__main__":
    main()