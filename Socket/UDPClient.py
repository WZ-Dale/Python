""" 简单的UDP客户端 """
from socket import *

serverName = '192.168.137.99'       # 服务端地址
serverPort = 12000                  # 服务端端口

clientSocket = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字

message = input("Input lowercase sentence: ")                   # 打印提示
message = message.encode()          # 将str转为字节流
clientSocket.sendto(message, (serverName, serverPort))          # 发送报文到服务端地址的服务端端口

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)    # 接收来自服务器的数据
print(modifiedMessage.decode())     # 打印响应报文

clientSocket.close()                # 关闭套接字
