import sys
import pygame
from pygame.sprite import Group
from settings import Settings							#导入Settings类
from ship import Ship
import game_function as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()										#初始化游戏
	ai_settings = Settings()							#创建一个Settings实例,并存储到变量ai_settings中
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))		#创建一个窗口对象
	pygame.display.set_caption("Alien Invasion")		#窗口命名
	#创建一艘飞船
	ship = Ship(ai_settings, screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	
	#开始游戏的主循环
	while True:	
		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, ship, bullets)
		#根据按键更新飞船位置
		ship.update()
		#更新子弹位置
		gf.update_bullets(bullets)
		#让最近绘制的屏幕可见
		gf.update_screen(ai_settings, screen, ship, bullets)
		
		
run_game()
