""" 简单的TCP客户端 """
from socket import *

serverName = '192.168.137.99'       # 服务端地址
serverPort = 12000                  # 服务端端口

clientSocket = socket(AF_INET, SOCK_STREAM)     # 创建TCP套接字
clientSocket.connect((serverName, serverPort))  # 在客户端和服务端建立一个TCP连接

message = input("Input lowercase sentence: ")   # 打印提示
message = message.encode()          # 将str转为字节流
clientSocket.send(message)          # 发送报文到服务端

modifiedMessage = clientSocket.recv(2048)       # 接收来自服务器的数据
print(modifiedMessage.decode())     # 打印响应报文

clientSocket.close()                # 关闭套接字
