import socket
import json
from pathlib import Path

clients = {}

class colors:
    RED = '\033[91m'
    ENDC = '\033[m'
    GREEN = '\033[92m'

def onlineList():
    try:
        with open(str(Path.home()) + '/onlineList.json') as json_file:
            global clients
            clients = json.load(json_file)
    except:
        print("\033[91mOnline list cannot load from the file.\033[m")
    print(colors.GREEN + "ONLINE LIST" + colors.ENDC)
    for i in clients:
        print("{}-) {} {}".format(i,clients[str(i)]["username"],clients[str(i)]["ip_address"]))
    print("----------------------------------")

chatUser = ""
chatIP = ""

def getInfo(ip):
    for x in clients:
        if(clients[str(x)]["ip_address"] == ip):
            global chatUser,chatIP
            chatUser = clients[str(x)]["username"]
            chatIP = clients[str(x)]["ip_address"]

def getName(ip):
    for x in clients:
        if(clients[str(x)]["ip_address"] == ip):
            return clients[str(x)]["username"]

def control(u):
    isOnline = False
    for x in clients:
        if(clients[str(x)]["username"] == u):
            return clients[str(x)]["ip_address"]
            isOnline = True
    if(isOnline == False):
        print("{} is not online.".format(u))

def connect(ip):
    try:
        TCPHost = ip
        TCPPort = 5001
        print("Connecting..")
        while 1:
            tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSocket.settimeout(5.0)
            tcpSocket.connect((TCPHost, TCPPort))
            tm = input("You -> {}: ".format(getName(ip)))
            if (tm == "exit"):
                tcpSocket.send("exit".encode())
                tcpSocket.close()
                break;
            else:
                tcpSocket.send(tm.encode())
            tcpSocket.close()
    except socket.error:
        print(colors.RED + getName(ip) + " is not online right now." + colors.ENDC+"\r\n")


if __name__ == '__main__':
    print("\033[91mIn order to start conversation to any online user, type their username. Type \033[92mexit\033[m \033[91mto leave conversation.\033[m")
    print("\033[91mType \033[92mreload\033[m \033[91mto refresh online list.\033[m\r\n")
    while True:
        onlineList()
        username = input("Connect to: ")
        if(username == "reload"):
            continue;
        else:
            if(control(username)):
                connect(control(username))


