import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5001
serverSocket.bind(('',PORT))
serverSocket.listen(1)

while 1:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    connectionSocket.close()