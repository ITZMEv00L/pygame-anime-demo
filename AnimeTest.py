#coding=utf-8
import sys,pygame,os
from pygame import *

from player import player
os.chdir(sys.path[0])
 
pygame.init() #初始化pygame类
screen = pygame.display.set_mode((840,630)) #设置窗口大小
pygame.display.set_caption('动画测试') #设置窗口标题

TICK = pygame.time.Clock()

FPS = 60 #fps
FPSClock = pygame.time.Clock()


player_resize=(144*5,256*5)
player_left_image=pygame.transform.scale(pygame.image.load('player_left.png'),player_resize)
player_right_image=pygame.transform.scale(pygame.image.load('player_right.png'),player_resize)
player=player(player_left_image,player_right_image,screen)


def control():
	#self.KeyCode=-1 
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT or event.key ==K_RIGHT:
				#player.state='walk'
				player.stateN=1
				if event.key == K_LEFT:
					player.walking=True
					player.dir=0
					
				if event.key == K_RIGHT:
					player.walking=True
					player.dir=1
			if event.key==K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type==KEYUP:
			if event.key==K_LEFT or K_RIGHT:
				player.walking=False
				player.dir=-1
				player.stateN=0
while True:
	screen.fill((46,123,5))#设置背景为绿色

	
	control()
	player.main()
	FPSClock.tick(FPS)  #设置刷新率
	pygame.display.update() #刷新窗口
	
	
	# for i in range(10):
		# i+=1
		# if i>=10:
			# print(FPSClock)
			# i=0