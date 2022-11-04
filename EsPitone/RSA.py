def MCD(num_1,num_2):
    if num_1 < num_2 :
        num_1,num_2 = num_2,num_1

    while(num_1 % num_2 != 0): 
        num_2,num_1  = num_1 % num_2,num_2

    return num_2

def mcm(num_1,num_2):
    return (num_1*num_2)/MCD(num_1,num_2)

def trovaInteroC(m):
    c = 2

    while( MCD(c,m)!=1 and c < m ):
        c+=1

    return c

def trovaInteroD(m,c):
    d = 0

    while( c*d%m!=1 and d < m ):
        d+=1

    return d

def cifraMessaggio(msg,n,c):
    caratteriASCII , cifrato = (ord(i) for i in msg),[]

    for a in  caratteriASCII:
        cifrato.append(chr(a**c % n))

    return ''.join(cifrato)

def decifraMessaggio(msg,n,d):
    decifrato = []
    for car in msg:
        b = ord(car)
        decifrato.append(chr(b**d % n))
    
    return(''.join(decifrato))


def main():
    # Scegli p tra 2, 3, 5 e q tra: 7, 11, 13
    p , q = 349,181 #int(input("Inserisci un numero Primo : ")),int(input("Inserisci un numero Primo : "))

    n = p * q
    m = int(mcm(p-1,q-1))
    c = trovaInteroC(m)
    d = trovaInteroD(m,c)

    print(f"\nCHIAVI PUBBLICHE n : {d} c : {c}\n") #divulga n e c
    print(f"CHIAVE PRIVATA d : {d}\n") #divulga n e c

    print(decifraMessaggio(cifraMessaggio("ciao",n,c),n,d))

if __name__ == "__main__":
    main()
