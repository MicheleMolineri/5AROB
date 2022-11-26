import socket
from threading import Thread
from time import time
import sqlite3

class Threads(Thread):
    def __init__(self, connection,values,nt):
        Thread.__init__(self)
        self.running = True
        self.values = values
        self.connection = connection
        self.id_thread = nt
    
    def run(self):
        msg=""
        
        for value in self.values:
            if value[1]==self.id_thread:
                msg += str(value[2]+",")
            elif value[1]<self.id_thread:
                msg = "error"
        msg+="exit" # automatically ensds 
        self.connection.sendall(msg.encode())
    
    def stop(self):
        self.running = False


def readDB(fileName):
    connection = sqlite3.connect("operations.db")
    cursor = connection.cursor()

    values = cursor.execute(f'SELECT * FROM operations').fetchall()

    connection.close()

    return values



def main():

    # creating the TCP socket
    s , threads = socket.socket(socket.AF_INET,socket.SOCK_STREAM) , []
    s.bind(("0.0.0.0",6000))
    s.listen() 

    # reading the DB
    values = readDB("operations.db")
    
    # creating the threads
    n_threads = 0 
    while True:
        connection ,addr = s.accept()
        n_threads += 1
        c = Threads(connection,values,n_threads)
        c.start()
        threads.append(c)
        
        recieved =connection.recv(4096).decode()

        print (f" Client {n_threads} sent : {recieved} from {addr}") 

        

if __name__ == "__main__":
    main()