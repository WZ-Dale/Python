# -*- coding:GBK -*-

import pygame

class Ship():
	def __init__(self, screen):
		"""��ʼ���ɴ����������ʼλ��"""
		self.screen = screen
		
		#���طɴ�ͼ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('images/ship.bmp')	#���ز��洢�ɴ�
		self.rect = self.image.get_rect()					#��ȡsurface����rect(�ɴ�����)
		self.screen_rect = screen.get_rect()				#��ȡ��Ļ����
		
		#��ÿ�ҷɴ�������Ļ�ײ�����
		self.rect.centerx = self.screen_rect.centerx		#��Ļ����xֵ�����ɴ�����x
		self.rect.bottom = self.screen_rect.bottom			#��Ļ�ײ�yֵ�����ɴ��ײ�y
		
	def blitme(self):
		"""��ָ��λ�û��Ʒɴ�"""
		self.screen.blit(self.image, self.rect)				#����self.rectָ��λ�ý��ɴ���������Ļ��
