# დავალება 1.

# სოკეტების გამოყენებით დაწერეთ კლიენტისა და სერვერის მხარე, სოკეტები უნდა მოქმედებდეს TCP პროტოკოლის გამოყენებით. სერვერის სოკეტს უნდა შეეძლოს რექვესტების მიღება ნებისმიერი ჰოსტიდან. მაგალითისათვის კი სერვერის კავშირის შექმნის დროს დაბეჭდეთ დაკავშირებული ჰოსტის მისამართი და კლიენტის მხარეს გამოაგზავნეთ შეტყობინება რომ კავშირი შედგა წარმატებით, დაბეჭდეთ კლიენტის მხარეს.

import socket

host = '192.168.5.4'
port = 44444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print("Server is listening")


while True:
    conn, addr = server.accept()
    print(f"Connceted by: {addr}")
    message = "Server -> Hello"
    conn.sendall(message.encode())
    conn.close()