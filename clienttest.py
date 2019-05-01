import socket
import threading
import time


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "192.168.1.17"
PORT = 5001
clientSocket.connect((HOST,PORT))

def listenData():
    while True:
        data = clientSocket.recvfrom(1024)
        print(data)

def sendmessage():
    while True:
        msg = input("{}: ".format(username))
        clientSocket.send(msg.encode())

if __name__ == '__main__':


    username = input("Enter username: ")
    t = threading.Thread(target=listenData,name='thread1')
    t2 = threading.Thread(target=sendmessage,name='thread2')

    t.start()
    t2.start()