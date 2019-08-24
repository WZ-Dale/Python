import sys
import pygame

def check_events(ship):
	"""响应鼠标和键盘事件"""
	for event in pygame.event.get():				#键盘和鼠标事件会触发for循环
		if event.type == pygame.QUIT:				#如果按了退出键
			sys.exit()								#退出

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:			#按下右键
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:			#松开右键
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False

def update_screen(ai_settings, screen, ship):
	"""更新屏幕上的图像, 并切换到新屏幕"""
	screen.fill(ai_settings.bg_color)				#使用颜色填充屏幕
	ship.blitme()									#绘制飞船,确保飞船在背景前
	pygame.display.flip()							#刷新最近绘制的屏幕
