import socket
import json
from pathlib import Path

soket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

ip = socket.gethostbyname(socket.gethostname()).split(".")
ip = "{}.{}.{}.255".format(ip[0],ip[1],ip[2])


HOST = ''
PORT = 5000
soket.bind((HOST,PORT))

i = 1
isNew = False

print ("Service Listener is working on {}:{}".format(ip,PORT))
print("Online list will be available on this location \033[91m"+str(Path.home())+"/\033[m after receive a connection.")
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
                break;
            else:
                isNew = True
        if(isNew == True):
            clients[i] = {"username":recJson["username"],"ip_address":recJson["ip_address"]}
            i = i + 1
            isNew = False

    print("\033[92m{}\033[m ({}) is online".format(recJson["username"],recJson["ip_address"]))
    print("--------------------------\033[92m[ONLINE LIST]\033[m------------------------------")
    for x in clients:
        print("{}-) {}".format(x,clients[x]["username"]))
    try:
        home = str(Path.home())
        with open(home + '/onlineList.json', 'w') as json_file:
            json_file.write(json.dumps(clients))
    except:
        print("\033[91mOnline list cannot write to file.\033[m")
    print("---------------------------------------------------------------------\r\n")
