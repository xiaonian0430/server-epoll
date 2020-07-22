# encoding: utf-8
"""
@author: XiaoNian
@contact: xiaonian030@163.com

@version: 1.0
@license: Apache Licence
@file: client.py
@time: 2020-07-22 11:15

"""
import socket

# 创建客户端socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 服务端IP地址和端口号元组
server_address = ('112.74.58.15', 8888)
# 客户端连接指定的IP地址和端口号
client_socket.connect(server_address)

while True:
    # 输入数据
    data = input('please input:').strip()
    if data == 'close':
        break
    # 客户端发送数据
    client_socket.sendall(data.encode('utf-8'))
    # 客户端接收数据
    server_data = client_socket.recv(1024)
    print('客户端收到的数据：', server_data)

# 关闭客户端socket
client_socket.close()
