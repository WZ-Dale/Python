# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2020/11/21 17:28

from PySide2.QtWidgets import QApplication, QTextBrowser, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Signal, QObject
import time
import prettytable as pt
from threading import Thread
import cv2
from PySide2.QtGui import QPixmap, QImage

# 自定义信号源对象类型，一定要继承自 QObject
class MySignals(QObject):
    text_print = Signal(str)

class Detection:
    def __init__(self):
        self.ui = QUiLoader().load("detection_ui.ui")
        self.ui.label_6.setText("检测日期：" + str(time.strftime("%Y-%m-%d", time.localtime(time.time()))))
        self.ui.pushButton.clicked.connect(self.detect)
        self.ui.pushButton_2.clicked.connect(self.show_ticket)
        self.ms = MySignals()                          # 实例化自定义信号源
        self.ms.text_print.connect(self.printToGui)    # 绑定自定义信号的处理函数
        self.show_image()

    def printToGui(self, text):
        self.ui.textBrowser.append(text)
        self.ui.textBrowser.ensureCursorVisible()

    def detect(self):
        """开始检测，普通输出"""
        def run():
            rc = "缺陷类型"
            row1 = "磨损"
            row2 = "缺块"
            row3 = "裂纹"
            col1 = "检测结果"
            col2 = "应采取措施"
            owner = self.ui.owner.text()
            oper = self.ui.oper.text()

            result = "车主姓名：" + owner + "\t" + "操作员姓名:" + oper + "\n"
            result += "检测日期：" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))) + "\n"
            result += "=========================================" + "\n"
            result += rc + "\t" + col1 + "\t\t" + col2 + "\n"
            result += row1 + "\t" + "轻度磨损\t\t" + "定期检查" + "\n"
            result += row2 + "\t" + "无缺块\t\t" + "定期检查" + "\n"
            result += row3 + "\t" + "1条(4.8mm)\t" + "立即修补" + "\n"

            self.ms.text_print.emit(result)
            print(result)

        thread = Thread(target = run)
        thread.start()

    def show_ticket(self):
        """使用漂亮表格输出"""
        def run():
            rc = "缺陷类型"
            row1 = "磨损"
            row2 = "缺块"
            row3 = "裂纹"
            col1 = "检测结果"
            col2 = "应采取措施"
            owner = self.ui.owner.text()
            oper = self.ui.oper.text()

            result = "=========================================" + "\n"
            result += "车主姓名：" + owner + "\t" + "操作员姓名:" + oper + "\n"
            result += "检测日期：" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

            self.ms.text_print.emit(result)
            print(result)

            tb = pt.PrettyTable()
            tb.field_names = [rc, col1, col2]
            lst = [row1, "轻度磨损", "定期检查"]
            tb.add_row(lst)
            lst = [row2, "无缺块", "定期检查"]
            tb.add_row(lst)
            lst = [row3, "1条(4.8mm)", "立即修补"]
            tb.add_row(lst)

            self.ms.text_print.emit(str(tb))
            print(tb)

        thread = Thread(target=run)
        thread.start()

    def show_image(self):
        # image = cv2.imread("3.jpg")
        # Image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage("3.jpg")
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.item.setScale(0.49)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.ui.graph.setScene(self.scene)  # 将场景添加至视图

        pix = QPixmap.fromImage("zuidashang.jpg")
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.item.setScale(0.49)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.ui.graph_2.setScene(self.scene)  # 将场景添加至视图

if __name__ == '__main__':
    app = QApplication([])
    dete = Detection()
    dete.ui.show()
    app.exec_()
