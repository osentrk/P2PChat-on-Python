import socket
import json

clients = {}

with open('onlineList.json') as json_file:
    clients = json.load(json_file)


class colors: # You may need to change color settings in iPython
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'

def onlineList():
    print("ONLINE LIST")
    for i in clients:
        print(i)
        print("{} {}".format(clients[str(i)]["username"],clients[str(i)]["ip_address"]))
    print("----------------------------------")

def control(u):
    isOnline = False
    for x in clients:
        if(clients[str(x)]["username"] == u):
            connect(clients[str(x)]["ip_address"])
            #return clients[str(x)]["ip_address"]
            isOnline = True
    if(isOnline == False):
        print("{} is not online.".format(u))
#l
def connect(ip):
    try:
        TCPHost = ip
        TCPPort = 5001
        print("Connecting..")
        while 1:
            tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSocket.settimeout(5.0)
            tcpSocket.connect((TCPHost, TCPPort))
            tm = input("You -> {} ".format(ip))
            if (tm == "exit"):
                break;
            tcpSocket.send(tm.encode())
            tcpSocket.close()
    except socket.error:
        print("{} is not online right now.".format(ip))
        print(colors.RED + "is not online" + colors.ENDC)

if __name__ == '__main__':
    while True:
        onlineList()
        getUsername = input("Connect to: ")
        control(getUsername)










# import socket
#
# s = socket.socket()
# s.settimeout(5)   # 5 seconds
# try:
#     s.connect(('123.123.123.123', 12345))         # "random" IP address and port
# except socket.error, exc:
#     print "Caught exception socket.error : %s" % exc