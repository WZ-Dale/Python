# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2020/11/23 20:59

import cv2
import imutils
from imutils import perspective, contours
from scipy.spatial import distance as dist
import numpy as np
from threading import Thread

path = ""
image = path + "3.jpg"
zuidashang = path + "zuidashang.jpg"
pixelsPerMetric = 4
min = 300
t = 500
T = 1000

class Crack:
    def __init__(self, image, zuidashang):
        self.image = image
        self.zuidashang = zuidashang

    # 计算中点
    def midpoint(self, ptA, ptB):
        return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

    def task(self):
        def run():
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
                    cv2.imshow("Image", orig)
                    cv2.waitKey(t)
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
                cv2.imshow("Image", orig)
                cv2.waitKey(t)
                cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
                cv2.imshow("Image", orig)
                cv2.waitKey(t)
                cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
                cv2.imshow("Image", orig)
                cv2.waitKey(t)
                cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
                cv2.imshow("Image", orig)
                cv2.waitKey(t)
                # 在中点之间画线
                cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
                cv2.imshow("Image", orig)
                cv2.waitKey(t)
                cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)
                cv2.imshow("Image", orig)
                cv2.waitKey(t)
                # 计算中点之间的欧氏距离
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                # 计算对象的大小
                dimA = dA / pixelsPerMetric
                dimB = dB / pixelsPerMetric
                # 在图像上绘制对象大小（标记尺寸）
                cv2.putText(orig, "{:.1f}mm".format(dimA), (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)  # 0.65
                cv2.imshow("Image", orig)
                cv2.waitKey(t)
                cv2.putText(orig, "{:.1f}mm".format(dimB), (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                cv2.imshow("Image", orig)
                cv2.waitKey(t)
            cv2.waitKey(3000)
        thread = Thread(target = run)
        thread.start()

if __name__ == '__main__':
    crack = Crack(image, zuidashang)
    crack.task()
