import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务器端地址
addr = ('127.0.0.1', 10021)

while True:
    # 获得数据
    data = input('请输入要处理的数据:')
    if not data or data == 'quit':
        break

    # 发送到服务端
    s.sendto(data.encode(), addr)
    recvdata, addr = s.recvfrom(1024)  # 接收服务器端发来的数据
    print(recvdata.decode('utf-8'))  # 解码打印

s.close()  # 关闭socket