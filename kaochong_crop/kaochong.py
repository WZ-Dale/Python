import cv2
import os 

# """先保存文件名到test.txt，再按行读取读取文件名，并进行操作"""
# f = open("test.txt",'w')
# for root,dirs,files in os.walk("kaochong", True):      # 遍历检索根、目录、文件
# 	for file in files:                                # 文件遍历
# 		f.writelines("kaochong\\" + file)            # 按行写入文件名
# 		f.write('\n')                                # 后面给个\n

# f = open("test.txt",'r')
# for i in range(1,107):                                 # 106个文件
#      line = f.readline()                               # 读一行
#      line = line.strip('\n')                           # 去掉\n
#      #print(line)
#      image = cv2.imread(line)                          # 读取文件名对应的图片
#      # cropImg = image[0:1080:2, 240:1680:2]           # 先y范围，后x范围，每个的第三个为采样步长
#      cropImg = image[0:1080, 240:1680]                 # 裁剪
#      cv2.imwrite("kaochong1\\" + line[20:39] + ".png", cropImg)       # 保存
# f.close()

"""简化版，读到文件名之后不保存，立即进行操作"""
for root,dirs,files in os.walk("kaochong", True):           # 遍历检索根、目录、文件
	for file in files:                                     # 文件遍历
          line = "kaochong\\" + file
          #print(line)
          image = cv2.imread(line)           # 读取文件名对应的图片
          # cropImg = image[0:1080:2, 240:1680:2]           # 先y范围，后x范围，每个的第三个为采样步长
          cropImg = image[0:1080, 240:1680]                 # 裁剪
          cv2.imwrite("kaochong1\\" + line[20:39] + ".png", cropImg)       # 保存

# print(image.shape)
# cv2.imshow("image", image)
# print(cropImg.shape)
# cv2.imshow("cropImg", cropImg)
# cv2.waitKey(0)
