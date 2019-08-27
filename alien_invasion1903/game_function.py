import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:					#按下右键
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
		if len(bullets) < ai_settings.bullets_allowed:			#如果还没有到达限制，就发射一颗子弹
			new_bullet = Bullet(ai_settings, screen, ship)		#创建一颗子弹，并将其加入到编组bullets中
			bullets.add(new_bullet)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:					#松开右键
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""响应鼠标和键盘事件"""
	for event in pygame.event.get():				#键盘和鼠标事件会触发for循环
		if event.type == pygame.QUIT:				#如果按了退出键
			sys.exit()								#退出
		elif event.type == pygame.KEYDOWN:			#按键按下
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:			#按键松开
			check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
	"""更新屏幕上的图像, 并切换到新屏幕"""
	screen.fill(ai_settings.bg_color)				#使用颜色填充屏幕
	for bullet in bullets.sprites():				#在飞船和外星人后面重绘所有子弹
		bullet.draw_bullet()
	ship.blitme()									#绘制飞船,确保飞船在背景前
	pygame.display.flip()							#刷新最近绘制的屏幕

def update_bullets(bullets):
	"""更新子弹的位置，并删除已消失的子弹"""
	bullets.update()								#更新子弹的位置
	for bullet in bullets.copy():					#删除已消失的子弹
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))
