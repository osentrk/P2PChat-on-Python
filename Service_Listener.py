import socket
import json


soket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

ip = socket.gethostbyname(socket.gethostname()).split(".")
ip = "{}.{}.{}.255".format(ip[0],ip[1],ip[2])

HOST = ip
PORT = 5000
soket.bind((HOST,PORT))

i = 1
isNew = False

print ("Service is listening on {}:{}".format(HOST,PORT))

clients = {}

while 1:
    msg, clientAddress = soket.recvfrom(1024)
    msg = msg.decode()
    recJson = json.loads(msg) #burada patladı
    recJson["ip_address"] = clientAddress[0]
    if i == 1:
        clients[i] = {"username": recJson["username"], "ip_address": recJson["ip_address"]}
        i = i + 1
    else:
        for x in range(1,i,1):
            if(recJson["username"] == clients[x]["username"]):
                isNew = False
                break;
            else:
                isNew = True
        if(isNew == True):
            clients[i] = {"username":recJson["username"],"ip_address":recJson["ip_address"]}
            i = i + 1
            isNew = False

    print("{} ({}) is online".format(recJson["username"],recJson["ip_address"]))
    print("ONLINE LIST : {}".format(clients))
    with open('onlineList.json', 'w') as json_file:
        json_file.write(json.dumps(clients))
    print("---------------------------------------------------------------------")
