# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2020/11/21 17:28

from PySide2.QtWidgets import QApplication, QTextBrowser, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Signal, QObject
import time
import prettytable as pt
from threading import Thread
from PySide2.QtGui import QPixmap, QImage

import cv2
import imutils
from imutils import perspective, contours
from scipy.spatial import distance as dist
import numpy as np

path = ""
image = path + "3.jpg"
zuidashang = path + "zuidashang.jpg"
upimage = "1.jpg"
pixelsPerMetric = 4
min = 300


# 自定义信号源对象类型，一定要继承自 QObject
class MySignals(QObject):
    text_print = Signal(str)
    show_update = Signal(np.ndarray)

class Detection:
    def __init__(self, image, zuidashang):
        self.image = image
        self.zuidashang = zuidashang

        self.ui = QUiLoader().load("detection_ui.ui")
        self.ui.label_6.setText("检测日期：" + str(time.strftime("%Y-%m-%d", time.localtime(time.time()))))
        self.ui.pushButton.clicked.connect(self.show_ticket)
        self.ui.pushButton.clicked.connect(self.task)
        self.ui.pushButton_2.clicked.connect(self.save_mysql)

        self.ms = MySignals()                          # 实例化自定义信号源
        self.ms.text_print.connect(self.printToGui)    # 绑定自定义信号的处理函数
        self.ms.show_update.connect(self.update_graph2)

        self.scene = QGraphicsScene()  # 创建场景
        self.scene2 = QGraphicsScene()  # 创建场景

        self.show_graph()

    def printToGui(self, text):
        self.ui.textBrowser.append(text)
        self.ui.textBrowser.ensureCursorVisible()

    def show_ticket(self):
        """使用漂亮表格输出检测结果"""
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
            result += "检测日期：" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))) + "\n"

            tb = pt.PrettyTable()
            tb.field_names = [rc, col1, col2]
            lst = [row1, "轻度磨损", "定期检查"]
            tb.add_row(lst)
            lst = [row2, "无缺块", "定期检查"]
            tb.add_row(lst)
            lst = [row3, "1条(4.8mm)", "立即修补"]
            tb.add_row(lst)

            self.ms.text_print.emit(result + str(tb))
            print(result + str(tb))

        thread = Thread(target=run)
        thread.start()

    def save_mysql(self):
        """保存到数据库"""
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

    def show_graph(self):
        pix = QPixmap(self.image)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.item.setScale(0.49)
        self.scene.addItem(self.item)
        self.ui.graph.setScene(self.scene)  # 将场景添加至视图
    def show_graph2(self):
        pix = QPixmap(self.zuidashang)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.item.setScale(0.49)
        self.scene2.addItem(self.item)
        self.ui.graph_2.setScene(self.scene2)  # 将场景添加至视图
    def update_graph2(self, upimage):
        Image = QImage(upimage.data, upimage.shape[1], upimage.shape[0], QImage.Format_RGB888)
        Image = QPixmap(Image)
        self.item = QGraphicsPixmapItem(Image)
        self.item.setScale(0.49)
        self.scene2.addItem(self.item)

    # 计算中点
    def midpoint(self, ptA, ptB):
        return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
    # 裂纹检测
    def task(self):
        def run():
            # 在graph_2中显示
            self.show_graph2()
            # 读取图像数据
            img = cv2.imread(self.image)
            zds = cv2.imread(self.zuidashang)
            # 执行边缘检测，然后执行膨胀+侵蚀
            edged = cv2.Canny(zds, 50, 100)
            edged = cv2.dilate(edged, None, iterations=1)
            edged = cv2.erode(edged, None, iterations=1)
            # 在边缘图中找到轮廓
            cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            # 对轮廓从左到右排序，并初始化
            (cnts, _) = contours.sort_contours(cnts)
            # 拷贝一下，用于处理
            orig = img.copy()
            for c in cnts:
                # 如果轮廓不够大，忽略它
                if cv2.contourArea(c) < min:
                    continue
                # 计算轮廓的旋转包围盒
                box = cv2.minAreaRect(c)    # 求出在上述点集下的最小面积矩形
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)    # 画最小外接矩形
                box = np.array(box, dtype="int")
                # 对轮廓中的点进行排序，使它们按左上、右上、右下和左下的顺序出现，然后绘制旋转后的包围框的轮廓
                box = perspective.order_points(box)
                cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)   # 矩形框选
                # 在原来的点上循环并画出它们（循环画出四个点）
                for (x, y) in box:
                    cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
                self.ms.show_update.emit(orig)
                time.sleep(1)
                # 解压缩有序边界框
                (tl, tr, br, bl) = box
                # 计算左上角和右上角坐标之间的中点，以及左下角和右下角坐标之间的中点
                (tltrX, tltrY) = self.midpoint(tl, tr)
                (blbrX, blbrY) = self.midpoint(bl, br)
                # 计算左上点和左下点之间的中点，以及右上点和右下点之间的中点
                (tlblX, tlblY) = self.midpoint(tl, bl)
                (trbrX, trbrY) = self.midpoint(tr, br)
                # 在图像上画中点
                cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
                cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
                cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
                cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
                self.ms.show_update.emit(orig)
                time.sleep(1)
                # 在中点之间画线
                cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
                cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)
                self.ms.show_update.emit(orig)
                time.sleep(1)
                # 计算中点之间的欧氏距离
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                # 计算对象的大小
                dimA = dA / pixelsPerMetric
                dimB = dB / pixelsPerMetric
                # 在图像上绘制对象大小（标记尺寸）
                cv2.putText(orig, "{:.1f}mm".format(dimA), (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)  # 0.65
                cv2.putText(orig, "{:.1f}mm".format(dimB), (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                self.ms.show_update.emit(orig)
                time.sleep(1)
            time.sleep(2)
        thread = Thread(target = run)
        thread.start()

if __name__ == '__main__':
    app = QApplication([])
    dete = Detection(image, zuidashang)
    dete.ui.show()
    app.exec_()
