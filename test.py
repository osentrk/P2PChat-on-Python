# #
# import socket

#
# if __name__ == '__main__':
#   UDP_IP = "192.168.1.255"
#   UDP_PORT = 5000
#   MESSAGE = "KEEP ALIVE".encode()
#   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#   sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#   while True:
#     sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
#     time.sleep(1)


import socket
ip = socket.gethostbyname(socket.gethostname()).split(".")
print(ip)
ip = "{}.{}.{}.255".format(ip[0],ip[1],ip[2])
print(ip)