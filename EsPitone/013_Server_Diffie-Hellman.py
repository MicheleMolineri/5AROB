import socket,random

def calc_B(g,b,N):
    return g**b % N

def calc_Ks(A,b,N):
    return A**b % N

def main():
    sServer , b = socket.socket(socket.AF_INET, socket.SOCK_DGRAM),None
    sServer.bind(("0.0.0.0", 5000))

    b = input("Insert your private key (b) : ")   
    msg,addr = sServer.recvfrom(4096) 
    msg = msg.decode().split(',')

    A,N,g = int(msg[0]),int(msg[1]),int(msg[2])
    #print(f"Recieved :\nA  : {A} ,g : {g}, N : {N} \n")

    B = calc_B(g,int(b),N)
    print(f"Ks : {calc_Ks(A,int(b),N)}")
    sServer.sendto(str(B).encode(),addr)
        
if __name__ == "__main__":
    main()