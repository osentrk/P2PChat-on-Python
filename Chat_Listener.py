import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5001
serverSocket.bind(("192.168.1.14",PORT))
serverSocket.listen(1)

while 1:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    print(message.decode())
    connectionSocket.close()