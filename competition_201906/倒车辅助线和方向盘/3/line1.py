# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def image(direction):
	img = plt.imread('0.bmp')
	plt.imshow(img)
	plt.title('Back-up Auxiliary Line')
	plt.ion()
	plt.pause(0.00001)
