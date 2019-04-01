# -*- coding:GBK -*-

import sys
import pygame
from settings import Settings							#导入Settings类
from ship import Ship

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()										#初始化游戏
	ai_settings = Settings()							#创建一个Settings实例,并存储到变量ai_settings中
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))		#创建一个窗口对象
	pygame.display.set_caption("Alien Invasion")		#窗口命名
	#创建一艘飞船
	ship = Ship(screen)
	
	#开始游戏的主循环
	while True:
		
		#监视键盘和鼠标事件
		for event in pygame.event.get():				#键盘和鼠标事件会触发for循环
			if event.type == pygame.QUIT:				#如果按了退出键
				sys.exit()								#退出
				
		#让最近绘制的屏幕可见
		screen.fill(ai_settings.bg_color)				#使用颜色填充屏幕
		ship.blitme()									#绘制飞船,确保飞船在背景前
		pygame.display.flip()							#刷新最近绘制的屏幕
		
		
run_game()
