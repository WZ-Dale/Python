# -*- coding:GBK -*-

import sys
import pygame
from settings import Settings							#����Settings��
from ship import Ship

def run_game():
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()										#��ʼ����Ϸ
	ai_settings = Settings()							#����һ��Settingsʵ��,���洢������ai_settings��
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))		#����һ�����ڶ���
	pygame.display.set_caption("Alien Invasion")		#��������
	#����һ�ҷɴ�
	ship = Ship(screen)
	
	#��ʼ��Ϸ����ѭ��
	while True:
		
		#���Ӽ��̺�����¼�
		for event in pygame.event.get():				#���̺�����¼��ᴥ��forѭ��
			if event.type == pygame.QUIT:				#��������˳���
				sys.exit()								#�˳�
				
		#��������Ƶ���Ļ�ɼ�
		screen.fill(ai_settings.bg_color)				#ʹ����ɫ�����Ļ
		ship.blitme()									#���Ʒɴ�,ȷ���ɴ��ڱ���ǰ
		pygame.display.flip()							#ˢ��������Ƶ���Ļ
		
		
run_game()
