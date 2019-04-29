import socket
import json


soket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
HOST = "192.168.1.255"
PORT = 5000
soket.bind((HOST,PORT))

i = 1
isNew = False

print ("Server is running on",PORT)

clients = {}

while 1:
    msg, clientAddress = soket.recvfrom(1024)
    msg = msg.decode()
    recJson = json.loads(msg)
    recJson["ip_address"] = clientAddress[0]
    if i == 1:
        clients[i] = {"username": recJson["username"], "ip_address": recJson["ip_address"]}
        i = i + 1
    else:
        for x in range(1,i,1):
            if(recJson["username"] == clients[x]["username"]):
                isNew = False
            elif(x==i-1):
                isNew = True
        if(isNew):
            clients[i] = {"username":recJson["username"],"ip_address":recJson["ip_address"]}
            i = i + 1
            isNew = False

    print("{} ({}) is online".format(recJson["username"],recJson["ip_address"]))
    print("ONLINE LIST : {}".format(clients))
    with open('onlineList.json', 'w') as json_file:
        json_file.write(json.dumps(clients))
    print("---------------------------------------------------------------------")
