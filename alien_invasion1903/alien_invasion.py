import sys
import pygame
from pygame.sprite import Group
from settings import Settings							#导入Settings类
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_function as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()										#初始化游戏
	ai_settings = Settings()							#创建一个Settings实例,并存储到变量ai_settings中
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))		#创建一个窗口对象
	pygame.display.set_caption("Alien Invasion")		#窗口命名
	#创建Play按钮
	play_button = Button(ai_settings, screen, "Play")
	#创建一个用于存储游戏统计信息的实例，并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	#创建一艘飞船
	ship = Ship(ai_settings, screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个用于存储外星人的编组
	aliens = Group()
	#创建一个外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#开始游戏的主循环
	while True:	
		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		if stats.game_active:
			#根据按键更新飞船位置
			ship.update()
			#更新子弹位置
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			#更新外星人位置
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		#让最近绘制的屏幕可见
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
			
run_game()
