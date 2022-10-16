import socket,time
import alphabot

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",8000))
s.listen()
bot = alphabot.AlphaBot()
bot.stop()

comandi  = {"":None,"right":bot.right,"stop": bot.stop,"left":bot.left,"forward":bot.forward,"backward":bot.backward}
conn,address = s.accept()
conn.sendall("Connessione Avvenuta".encode())


while True : 
    eseguito=True
    data = conn.recv(4096)
    azione = data.decode()
    
    if azione in comandi and eseguito:
        comandi[azione]()
        time.sleep(1)
        bot.stop()

    else : break

s.close()   

