import socket
import pickle #to send objects

SERVER=socket.gethostbyname(socket.gethostname())
PORT=5050
ADDR=(SERVER, PORT)
DIS_MSG = 'Disconnect'

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(m):
    msg=m.encode('utf-8')
    mLength=len(msg)
    sLength=str(mLength).encode('utf-8')
    sLength+=b' '*(64-len(sLength))
    client.send(sLength)
    client.send(msg)
send('Hello there!')
s=input('[Enter your message]:')
send(s)
s=input('[Enter your message]:')
send(s)
send(DIS_MSG)