import socket
from threading import Thread
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("0.0.0.0",8000))

class receive(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
    
    def run(self):
        while self.running:
            print()
            time.sleep(1)
            msg = input("\nMenu\n"+
            "1|filename -> Search File\n"+
            "2|filename -> Get Fragments\n"+
            "3|filename|nFragment -> Get Host\n"+
            "4|filename -> Get All Hosts\n"+
            "5 -> Exit\n"+"\n\nInsert your choice: ")
            
            if msg == 5 :
                self.stop()
                s.close()
            else:
                s.sendall(msg.encode())

    def stop(self):
        self.running = False
            
def main():
    r = receive()
    r.start()

    while r.running:
        msg = s.recv(4096)
        msg = msg.decode()
        print(msg)

if __name__ == "__main__":
    main()