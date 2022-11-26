import socket
from threading import Thread
from time import time
import sqlite3

s , threads = socket.socket(socket.AF_INET,socket.SOCK_STREAM) , []

class Threads(Thread):
    def __init__(self, connection,address):
        Thread.__init__(self)
        self.running = True
        self.connection = connection
    
    def run(self):
        while self.running:
            msg  = self.connection.recv(4096)
            msg = msg.decode() # function | filename | frNumber
            msg = msg.split("|")

            if msg[0] == "1":               #searchFile
                self.connection.sendall(searchFile(msg[1]).encode())
            elif msg[0] == "2":             #getFragments
                self.connection.sendall(getFragments(msg[1]).encode())
            elif msg[0] == "3":             #getHost
                self.connection.sendall(getHost(msg[1],msg[2]).encode())
            elif msg[0] == "4":             #getAllHosts
                self.connection.sendall(getAllHosts(msg[1]).encode())
            elif msg[0] == "5": 
                print("Shutting down the connession...")            #exit
                self.stop()
                self.connection.close()
            else:
                self.connection.sendall("Comando non riconosciuto".encode())
            
            
    def stop(self):
        self.running = False


def checkFile(fileName):
    connection = sqlite3.connect("000_PreparazioneVerificaFile.db")
    cursor = connection.cursor()

    res = cursor.execute(f'SELECT COUNT(*) FROM files WHERE files.nome = "{fileName}"')
    count = res.fetchall()
    connection.close()
    if count[0][0] > 0 :
        return True
    else:
        return False

#chiedere al server se un certo nome file è presente;
def searchFile(fileName):
    if checkFile(fileName): return "File found :)"
    else: return "File not found :( "

#chiedere al server il numero di frammenti di un file 
#a partire dal suo nome file;

def getFragments(fileName):

    if checkFile(fileName):
        connection = sqlite3.connect("000_PreparazioneVerificaFile.db")
        cursor = connection.cursor()

        res = cursor.execute(f'SELECT tot_frammenti FROM files WHERE files.nome = "{fileName}"')
        fragments = res.fetchall()
        connection.close()
        return "Number of fragments : "+str(fragments[0][0])
    else:return "File not found :( "

#chiedere al server l’IP dell’host che ospita un frammento 
# a partire nome file e dal numero del frammento;

def getHost(fileName,fragmentNumber):
    if fragmentNumber == "" : fragmentNumber = 1
    if checkFile(fileName):
        connection = sqlite3.connect("000_PreparazioneVerificaFile.db")
        cursor = connection.cursor()

        res = cursor.execute(f'SELECT host FROM files,frammenti WHERE files.id_file = frammenti.id_file and files.nome = "{fileName}" AND frammenti.n_frammento = {fragmentNumber}')
        host = res.fetchall()
        connection.close()
        return f"Address of fragment {fragmentNumber} : "+str(host[0][0])
    else:return "File not found :( "

#chiedere al server tutti gli IP degli host sui quali 
# sono salvati i frammenti di un file a partire dal nome file.

def getAllHosts(fileName):
    if checkFile(fileName):
        connection = sqlite3.connect("000_PreparazioneVerificaFile.db")
        cursor = connection.cursor()

        res = cursor.execute(f"SELECT distinct host FROM files,frammenti WHERE files.id_file = frammenti.id_file  and files.nome = \"{fileName}\"")
        hosts = res.fetchall()
        connection.close()
        return f"Fragments addresses of {fileName} : "+str(hosts)
    else:return "File not found :( "

def main():
    s.bind(("0.0.0.0",8000))
    s.listen() 
    #print("Waiting to connect ... ")

    while True:
        connection, address = s.accept()
        connection.sendall("Connession established 👍 ".encode())
        c = Threads(connection,address)
        c.start()
        threads.append(c)

        for thread in threads:
            if not thread.running:
                thread.join()
                threads.remove(thread)

if __name__ == "__main__":
    main()