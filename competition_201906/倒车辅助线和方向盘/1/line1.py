# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

def image(direction):
	#读取图片
	img = cv2.imread('BG.bmp')
	image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	###print(img.shape)
	M = np.float32([[1, 0, 0], [0, 1, 0]])
	c = image[0:10, 0:640]
	a = cv2.warpAffine(c, M, (c.shape[1], c.shape[0]))
	for i in range(360):
		b = image[i:i+1, 0:640]
		#direction = 0
		p = (-1000 + (i*2777.8)**0.5)
		if direction == 0:
			x = p
		elif direction <= 50:
			x = p*((50-direction)/50)
		else:
			x = (-p)*((direction-50)/50)
		#print(x)
		M = np.float32([[1, 0, x], [0, 1, 0]])
		d = cv2.warpAffine(b, M, (b.shape[1], b.shape[0]))
		a = np.vstack((a,d))
	plt.imshow(a, 'gray')
	plt.title('Back-up Auxiliary Line')  
	plt.xticks([]),plt.yticks([])
	plt.ion()
	plt.pause(0.00001)

