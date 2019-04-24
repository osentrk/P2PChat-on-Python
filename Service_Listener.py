import socket
import json
soket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
HOST = "192.168.1.255"
PORT = 5000
soket.bind((HOST,PORT))


print ("Server is running on",PORT)

clients = ()

while 1:
    msg, clientAddress = soket.recvfrom(1024)
    msg = msg.decode()
    recJson = json.loads(msg)
    recJson["ip_address"] = clientAddress
    print("{} ({}) is online".format(recJson["username"],recJson["ip_address"]))
