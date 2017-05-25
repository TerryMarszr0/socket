import socket
import time
# import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket

s.bind(('127.0.0.1', 4999))  # 绑定本机IP和任意端口

s.listen(1)  # 监听，等待连接的最大数目为1

print('Server is running...')


def TCP(sock, addr):  # TCP服务器端处理逻辑

    print('Accept new connection from %s:%s.' % addr)  # 接受新的连接请求

    while True:
        rec_data = sock.recv(1024)  # 接受其数据
        time.sleep(1)  # 延迟
        if not rec_data or rec_data.decode() == 'quit':  # 如果数据为空或者'quit'，则退出
            break
        print(rec_data.decode('utf-8'))

        exp_data = input("请输入需要发送的数据：")

        sock.send(exp_data.encode())  # 将需要发送的数据编码后，发送

    sock.close()  # 关闭连接
    print('Connection from %s:%s closed.' % addr)


while True:
    sock, addr = s.accept()  # 接收一个新连接
    TCP(sock, addr)  # 处理连接