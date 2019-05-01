#bu dosya tcpsw-client kombinasyonunu test için yaratılmıştır.

import socket
import threading
import time

HOST = "192.168.1.23"
PORT = 5001

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((HOST,PORT))
serverSocket.listen(50)
print("Sunucu dinlemeye hazır")

while 1:
    connectionSocket,addr = serverSocket.accept()
    msg = connectionSocket.recv(1024).decode()
    print(msg)
    connectionSocket.close()

## client


