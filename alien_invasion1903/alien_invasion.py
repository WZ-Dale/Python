# -*- coding:utf-8 -*-

import sys
import pygame

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()										#初始化游戏
	screen = pygame.display.set_mode((1200, 800))		#创建一个窗口对象
	pygame.display.set_caption("Alien Invasion")		#窗口命名
	bg_color = (230, 230, 230)							#存储颜色
	
	#开始游戏的主循环
	while True:
		
		#监视键盘和鼠标事件
		for event in pygame.event.get():				#键盘和鼠标事件会触发for循环
			if event.type == pygame.QUIT:				#如果按了退出键
				sys.exit()								#退出
				
		#让最近绘制的屏幕可见
		screen.fill(bg_color)							#使用颜色填充屏幕
		pygame.display.flip()							#刷新最近绘制的屏幕
		
		
run_game()
