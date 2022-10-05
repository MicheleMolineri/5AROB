import socket
from threading import Thread

sClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sServer.bind(("0.0.0.0", 5000))

class receive(Thread):
    def __init__(self):   
        Thread.__init__(self)
        self.running = True
    
    def run(self):
        while self.running:
            msg, ind_client = sServer.recvfrom(4096)
            print(msg.decode()) 

    def stop(self):
        self.running = False

def main():
    r = receive()
    r.start()

    while True:
        string = input()
        sClient.sendto(string.encode(), ("192.168.0.136", 5000))
        if string == "break":
            r.stop()
            r.join()
            break

    sClient.close()

if __name__ == "__main__":
    main()