# -*- coding:utf-8 -*-

import sys
import pygame

def run_game():
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()										#��ʼ����Ϸ
	screen = pygame.display.set_mode((1200, 800))		#����һ�����ڶ���
	pygame.display.set_caption("Alien Invasion")		#��������
	bg_color = (230, 230, 230)							#�洢��ɫ
	
	#��ʼ��Ϸ����ѭ��
	while True:
		
		#���Ӽ��̺�����¼�
		for event in pygame.event.get():				#���̺�����¼��ᴥ��forѭ��
			if event.type == pygame.QUIT:				#��������˳���
				sys.exit()								#�˳�
				
		#��������Ƶ���Ļ�ɼ�
		screen.fill(bg_color)							#ʹ����ɫ�����Ļ
		pygame.display.flip()							#ˢ��������Ƶ���Ļ
		
		
run_game()
