import socket


def main():
    '''用套接字上传图片 服务端'''
    # 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip和port
    server_addr = ('192.168.1.4', 7890)
    tcp_socket.bind(server_addr)

    # 改为被动连接
    tcp_socket.listen(128)

    # 等待客户端连接
    client_socket, _ = tcp_socket.accept()

    # 接收客户端发来的文件名
    recv_data = client_socket.recv(1024).decode("utf-8")

    # 找到该文件，发给客户端
    content = None
    with open("database.png", 'rb') as f:
        content = f.read()
    
    if content:
        client_socket.send(content)

    # 关闭套接字
    client_socket.close()
    tcp_socket.close()

if __name__ == "__main__":
    main()