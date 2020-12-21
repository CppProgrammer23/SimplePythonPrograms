import socket
import threading

#constant values

SERVER=socket.gethostbyname(socket.gethostname())
PORT=5050
ADDR=(SERVER, PORT)
DIS_MSG = 'Disconnect'

#
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def clientHandle(con,addr):
    print(f'[NEW CONNECTION]: {addr} connected.')
    c=True
    while c:
        mLength=con.recv(64).decode('utf-8')
        if mLength:
            mLength=int(mLength)
            m=con.recv(mLength).decode('utf-8')
            if m==DIS_MSG:
                c=False
            print(f'[{addr}] {m}')
    con.close()
def start():
    server.listen()
    while True:
        con,addr=server.accept()
        fun=threading.Thread(target=clientHandle,args=(con,addr))
        fun.start()
start()