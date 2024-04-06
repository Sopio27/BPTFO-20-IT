# დავალება 2.

# სოკეტების გამოყენებით დაწერეთ ჩატი, სოკეტები უნდა მოქმედებდეს TCP პროტოკოლით, სერვერის სოკეტს უნდა შეეძლოს რექვესტების მიღება მხოლოდ ლოკალური ჰოსტიდან, მიმოწერა შეინახეთ ტექსტურ ფაილში.

import socket
import threading

host = '192.168.5.4'
port = 44444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle (client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat.'.encode('ascii'))
            nickname.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('Nickname'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}.')
        broadcast(f'{nickname} joined the chat.'.encode('ascii'))
        client.send('Connected to the server.'.encode('ascii'))

        thread = threading.Thread(targer=handle, args=(client,))
        thread.start()

print('Server is listening')
receive()