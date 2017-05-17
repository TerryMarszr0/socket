import socket

# 创建一个socket,SOCK_DGRAM表示UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定IP地址及端口
s.bind(('127.0.0.1', 10021))

print('Bound UDP on 10021...')

# 获得数据和客户端的地址与端口,一次最大接收1024字节
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # 将数据变成大写送回客户端
    s.sendto(data.decode('utf-8').upper().encode(), addr)

# 不关闭socket
