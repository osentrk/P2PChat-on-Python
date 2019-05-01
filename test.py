# import socketserver
#
# class MyUDPHandler(socketserver.BaseRequestHandler):
#     """
#     This class works similar to the TCP handler class, except that
#     self.request consists of a pair of data and client socket, and since
#     there is no connection the client address must be given explicitly
#     when sending data back via sendto().
#     """
#
#     def handle(self):
#         data = self.request[0].strip()
#         print("oynat bakalım : {}".format(self.request))
#         print("DATACIK {}".format(data))
#         socket = self.request[1]
#         print("data {} soket {}".format(data,socket))
#         print(self.client_address[0])
#         print("{} wrote:".format(self.client_address[0]))
#         socket.sendto(data.upper(), self.client_address)
#
# if __name__ == "__main__":
#     HOST, PORT = "localhost", 5000
#     server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
#     server.serve_forever()

import socket
import threading
import socketserver

# class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
#
#     def handle(self):
#         data = str(self.request.recv(1024), 'ascii')
#         cur_thread = threading.current_thread()
#         response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
#         self.request.sendall(response)
#
# class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     pass
#
# def client(ip, port, message):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((ip, port))
#         sock.sendall(bytes(message, 'ascii'))
#         response = str(sock.recv(1024), 'ascii')
#         print("Received: {}".format(response))
#
# if __name__ == "__main__":
#     # Port 0 means to select an arbitrary unused port
#     HOST, PORT = "localhost", 5000
#
#     server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
#     with server:
#         ip, port = server.server_address
#         print(ip,port)
#         # Start a thread with the server -- that thread will then start one
#         # more thread for each request
#         server_thread = threading.Thread(target=server.serve_forever)
#         # Exit the server thread when the main thread terminates
#         server_thread.daemon = True
#         server_thread.start()
#         print("Server loop running in thread:", server_thread.name)
#
#         client(ip, port, "Hello World 1")
#         client(ip, port, "Hello World 2")
#         client(ip, port, "Hello World 3")
#
#         server.shutdown()

import socket
import threading
import time

HOST = "192.168.1.23"
PORT = 5001

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    clientSocket.connect((HOST, PORT))
except:
    print("Sunucuya bağlanamadık")
else:
    print("Sunucuya bağlandık")


message = input("Mesaj: ")
clientSocket.send(message.encode())
gelenMesaj = clientSocket.recv(1024)
print(gelenMesaj.decode())
clientSocket.close()