# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2020/11/24 10:06

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

class Test:
    def __init__(self):
        self.ui = QUiLoader().load("detection_ui1.ui")
        self.show_image()
        self.update_item(QPixmap("1.jpg"))

    def show_image(self):
        pix = QPixmap("3.jpg")
        # Image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        # pix = QPixmap.fromImage(image)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.item.setScale(0.49)
        self.scene.addItem(self.item)
        self.ui.graph.setScene(self.scene)  # 将场景添加至视图

        pix = QPixmap.fromImage("zuidashang.jpg")
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.item.setScale(0.49)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.ui.graph_2.setScene(self.scene)  # 将场景添加至视图

    def update_item(self, upimage):
        self.item = QGraphicsPixmapItem(upimage)
        self.item.setScale(0.49)
        self.scene.addItem(self.item)

if __name__ == '__main__':
    app = QApplication([])
    test = Test()
    test.ui.show()
    app.exec_()
