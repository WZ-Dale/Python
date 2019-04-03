# -*- coding: utf-8 -*-

import sys
import pygame

def check_events():
	"""响应鼠标和键盘事件"""
	for event in pygame.event.get():				#键盘和鼠标事件会触发for循环
		if event.type == pygame.QUIT:				#如果按了退出键
			sys.exit()								#退出
