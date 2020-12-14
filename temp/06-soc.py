import socket



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 8080))

sock.listen(5)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print(data)

    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"123123")
    conn.close()
