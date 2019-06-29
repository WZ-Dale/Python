# -*- coding: utf-8 -*-

import threading
import time
import serial
import line1

class ComThread:
    def __init__(self, Port='COM6'):
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.port = Port
        self.ID = None
        self.data = None
        self.direction = 0
		
    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def SetStopEvent(self):
        if not self.waitEnd is None:
            self.waitEnd.set()
        self.alive = False
        self.stop()

    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        self.l_serial.baudrate = 9600
        self.l_serial.timeout = 2
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
                    #print(type(temp))
                    ###print(temp,end=' ')

                    arr1 = temp.split('：')
                    arr2 = arr1[1].split('\r')[:1]
                    self.direction = int(arr2[0])
                    print(self.direction)
                    
                except:
                    print("读取错误，请重试！\n")

            line1.image(self.direction)
        self.ID = direction
        self.data = direction
        self.waitEnd.set()
        self.alive = False
        

    def stop(self):
        self.alive = False
        self.thread_read.join()
        if self.l_serial.isOpen():
            self.l_serial.close()

#调用串口，测试串口
def main():
    rt = ComThread()
    #rt.sendport = '**1*80*'
    try:
        if  rt.start():
            print(rt.l_serial.name)
            rt.waiting()
            print("The data is:%s,The Id is:%s"%(rt.data,rt.ID))
            rt.stop()
        else:
            pass
    except Exception as se:
        print(str(se))

    if rt.alive:
        rt.stop()

    print('')
    print ('End OK .')
    temp_ID=rt.ID
    temp_data=rt.data
    del rt
    return temp_ID,temp_data


if __name__ == '__main__':

    #设置一个主函数，用来运行窗口，便于若其他地方下需要调用串口时可以直接调用main函数
    ID,data = main()

    print("******")
    print(ID,data)
