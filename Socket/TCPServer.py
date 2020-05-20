""" 简单的TCP服务端 """
from socket import *

serverPort = 12000      # 服务端口

serverSocket = socket(AF_INET, SOCK_STREAM) # 创建TCP套接字
serverSocket.bind(('', serverPort))         # 套接字绑定服务端口
serverSocket.listen(1)  # 开始监听

print("The server is ready to receive!")    # 打印提示
while True:
    connectionSocket, clientAddress = serverSocket.accept() # 新建套接字为客户端专用，并保存客户端地址
    message = connectionSocket.recv(2048)   # 接收请求报文
    modifiedMessage = message.upper()       # 处理报文
    connectionSocket.send(modifiedMessage)  # 发送响应报文到客户端
    connectionSocket.close()                # 关闭套接字

serverSocket.close()    # 关闭套接字
