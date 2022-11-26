import socket
from threading import Thread
import time

          
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("0.0.0.0",6000))
    done = False

    while not done:
        msg , calc = s.recv(4096), ""
        operations = msg.decode().split(",")

        for operation in operations:
            if operation == "exit":
                done = True
                break
            try : calc += str(eval(operation))+" , "
            except : calc += "error"
            print(calc)

        s.sendall(calc.encode())
        done = True
    
    s.close()

if __name__ == "__main__":
    main()