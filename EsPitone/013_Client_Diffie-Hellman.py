import socket,random

def readPrimes():
    f=open("./nPrimi.csv","r")
    testo = f.readlines()
    primes  = [int(n) for n in testo]
    f.close()
    return primes

def randomPrimo():
    primes = readPrimes()
    return primes[random.randint(2,len(primes))]

def random_g(N):
    return random.randint(2,N)

def calc_A(g,a,N):
    return g**a % N

def calc_Ks(B,a,N):
    return B**a % N

def main():
    sClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    a,N = None,randomPrimo()
    g = random_g(N)

    a = input("Insert your private key  (a) : ")
    s = (f"{calc_A(g,int(a),N)},{N},{g}")
    #print(f"a : {a} ,g : {g}, N : {N} ")

    sClient.sendto(s.encode(), ("0.0.0.0", 5000))
    msg,addr = sClient.recvfrom(4086)
    #print(msg)
    B = int(msg.decode())
    print("Ks : ",calc_Ks(B,int(a),N))

if __name__ == "__main__":
    main()