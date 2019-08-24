import pygame

class Ship():
	def __init__(self, screen):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		
		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')	#加载并存储飞船
		self.rect = self.image.get_rect()					#获取surface属性rect(飞船矩形)
		self.screen_rect = screen.get_rect()				#获取屏幕矩形
		
		#将每艘飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx		#屏幕中央x值赋给飞船中央x
		self.rect.bottom = self.screen_rect.bottom			#屏幕底部y值赋给飞船底部y
		
		#移动标志
		self.moving_right = False
		self.moving_left = False


	def update(self):
		"""根据移动标志调整飞船位置"""
		if self.moving_right:								#若移动标志moving_right为True
			self.rect.centerx += 1							#则使飞船持续右移
		if self.moving_left:
			self.rect.centerx -= 1

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)				#根据self.rect指定位置将飞船绘制在屏幕上
