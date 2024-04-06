import socket

host = '192.168.5.4'
port = 44444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client is active")

server.connect((host, port))

received_message = server.recv(1024).decode()
print(received_message)
server.close()