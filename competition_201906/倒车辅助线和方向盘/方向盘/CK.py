# -*- coding: utf-8 -*-
import cv2
import threading
import time
import serial
import matplotlib.pyplot as plt

class ComThread:
    def __init__(self, Port='COM6'):
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.port = Port
        self.direction = 0
		
    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        self.l_serial.baudrate = 9600
        #self.l_serial.timeout = 1
        self.l_serial.open()
        if self.l_serial.isOpen():
            self.waitEnd = threading.Event()
            self.alive = True
            self.thread_read = None
            self.thread_read = threading.Thread(target=self.FirstReader)
            self.thread_read.setDaemon(1)
            self.thread_read.start()
            return True
        else:
            return False
	
    def FirstReader(self):
        while self.alive:
            data = ''
            data = data.encode('utf-8')

            n = self.l_serial.inWaiting()
            if n:
                 data = data + self.l_serial.read(n)

            n = self.l_serial.inWaiting()
            if len(data)>0 and n==0:
                try:
                    temp = data.decode('gb18030')
                    arr1 = temp.split('：')
                    arr2 = arr1[1].split('\r')[:1]
                    self.direction = int(arr2[0])
                    print(self.direction)
                except:
                    print("读取错误，请重试！\n")
            a = int((self.direction + 4) / 10) * 10
            img = plt.imread(repr(a) + '.bmp')
            plt.imshow(img)
            plt.ion()
            plt.pause(0.0001)

#调用串口，测试串口
def main():
	rt = ComThread()
	rt.start()
	print(rt.l_serial.name)
	rt.waiting()
    

if __name__ == '__main__':
	main()
