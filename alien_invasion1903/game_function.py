# -*- coding: utf-8 -*-

import sys
import pygame

def check_events():
	"""响应鼠标和键盘事件"""
	for event in pygame.event.get():				#键盘和鼠标事件会触发for循环
		if event.type == pygame.QUIT:				#如果按了退出键
			sys.exit()								#退出

def update_screen(ai_settings, screen, ship):
	"""更新屏幕上的图像, 并切换到新屏幕"""
	screen.fill(ai_settings.bg_color)				#使用颜色填充屏幕
	ship.blitme()									#绘制飞船,确保飞船在背景前
	pygame.display.flip()							#刷新最近绘制的屏幕
