""" 简单的UDP服务端 """
from socket import *

serverPort = 12000      # 服务端口

serverSocket = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字
serverSocket.bind(('', serverPort))         # 套接字绑定服务端口

print("The server is ready to receive!")    # 打印提示
while True:
    message, clientAddress = serverSocket.recvfrom(2048)    # 接收请求报文和客户端地址
    modifiedMessage = message.upper()                       # 处理报文
    serverSocket.sendto(modifiedMessage, clientAddress)     # 发送响应报文到客户端地址

clientSocket.close()    # 关闭套接字
