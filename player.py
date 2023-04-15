# import pygame
# from pygame.locals import *

class player():
	def __init__(self,image_left,image_right,screen):
		#self.state='stand'
		self.walk_speed=3
		self.walking=False
		player.dir=-1
		#图片与动画
		self.screen=screen
		self.image_left=image_left
		self.image_right=image_right
		self.image=self.image_left
		self.timer=0
		self.player_anime=''
		self.N=0
		self.stateN=0
		self.frameMap = [6,4] #
		self.frameRect = self.image.get_rect()
		self.frameRect.width //= self.frameMap[0]
		self.frameRect.height //= self.frameMap[1]
		self.frameRect.y=self.frameRect.height*self.stateN
		
		#玩家位置
		self.x = 0;self.y = 125
		self.pos=(self.x,self.y)
	def play_anime(self,stateN,play_speed,fps):
		if stateN==self.stateN:
			if self.N<self.frameMap[0]:
				self.timer+=play_speed
				print((len(str(self.frameRect))+1)*'*'+'|当前帧数'+'|Timer')
				print(self.frameRect,'|',self.N,'     |',self.timer)
				self.screen.blit(self.image,self.pos,self.frameRect)
				if self.timer%fps==0:
					self.N+=1
					self.frameRect.x=self.frameRect.width * self.N
					self.frameRect.y=self.frameRect.height*self.stateN
		if self.N>=self.frameMap[0]:
			self.player_anime=''
			self.N=0
			self.timer=0
			self.frameRect = self.image.get_rect()
			self.frameRect.width //= self.frameMap[0]
			self.frameRect.height //= self.frameMap[1]
			self.frameRect.y=self.frameRect.height*self.stateN


	def main(self):
		self.pos=(self.x,self.y)
		if self.walking==True and self.dir==0:
			self.x-=self.walk_speed
			self.image=self.image_right
		if self.walking==True and self.dir==1:
			self.x+=self.walk_speed
			self.image=self.image_left
		if self.stateN==0:
			self.play_anime(self.stateN,3,60)
		if self.stateN==1:
			self.play_anime(self.stateN,3,60)
		#self.screen.blit(self.image,self.pos,self.frameRect)
		print('玩家状态:',self.stateN)
		
