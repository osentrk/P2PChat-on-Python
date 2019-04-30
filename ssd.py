# import socket
# import threading
# import time
#
#
# clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# HOST = "192.168.1.23"
# PORT = 5001
# clientSocket.connect((HOST,PORT))
#
# def listenData():
#     while True:
#         data = clientSocket.recvfrom(1024)
#         print(data)
#
# def sendmessage():
#     while True:
#         msg = input("{}: ".format(username))
#         clientSocket.send(msg.encode())
#
# if __name__ == '__main__':
#
#
#     username = input("Enter username: ")
#     t = threading.Thread(target=listenData,name='thread1')
#     t2 = threading.Thread(target=sendmessage,name='thread2')
#
#     t.start()
#     t2.start()

import socket
import threading
import time


soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
HOST = "192.168.1.255"
PORT = 5000

TCPHost = ""
TCPPort = 5001
def sayhello():
    while True:
        soket.sendto(username.encode(), (HOST, PORT))
        time.sleep(10)

def sendmsg():
    while True:
        msg = input("{}: ".format(username))
        control = msg.split(" ")
        if control[0] == "connect":
            global TCPHost
            TCPHost = control[1]
            t3 = threading.Thread(target=TCPSender, name='thread3')
            t3.start()
            break;
        soket.sendto(msg.encode(),(HOST,PORT))

def TCPSender():
    tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpSocket.connect((TCPHost,TCPPort))
    print("You will chat with {}".format(TCPHost))
    while 1:
        tm = input("{}: ".format(username))
        if tm == "exit":
            sendmsg()
            break;
        tcpSocket.send(tm.encode())
    tcpSocket.close()


if __name__ == '__main__':


    username = input("Enter username: ")
    t = threading.Thread(target=sayhello,name='thread1')
    t2 = threading.Thread(target=sendmsg,name='thread2')
    t.start()
    t2.start()