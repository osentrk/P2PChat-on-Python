#CLASS LIST
import socket
import json

clients = {}

with open('onlineList.json') as json_file:
    clients = json.load(json_file)


class colors: # You may need to change color settings in iPython
    RED = '\033[91m'
    ENDC = '\033[m'
    GREEN = '\033[32m'

def onlineList():
    print("ONLINE LIST")
    for i in clients:
        print("{} {}".format(clients[str(i)]["username"],clients[str(i)]["ip_address"]))
    print("----------------------------------")

chatUser = ""
chatIP = ""
def getInfo(ip):
    for x in clients:
        if(clients[str(x)]["ip_address"] == ip):
            global chatUser,chatIP
            chatUser = clients[str(x)]["username"]
            chatIP = clients[str(x)]["ip_address"]

def control(u):
    isOnline = False
    for x in clients:
        if(clients[str(x)]["username"] == u):
            connect(clients[str(x)]["ip_address"])
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
            tm = input("You -> {}: ".format(ip))
            if (tm == "exit"):
                break;
            tcpSocket.send(tm.encode())
            tcpSocket.close()
    except socket.error:
        print(colors.RED + " {"+ip+"} is not online right now." + colors.ENDC)

if __name__ == '__main__':
    while True:
        onlineList()
        getUsername = input("Connect to: ")
        control(getUsername)