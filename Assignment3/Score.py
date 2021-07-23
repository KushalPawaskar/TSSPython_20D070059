import pygame

class Score():

	def __init__(self,a):
		self.a=a

	def show(self,pos,color,font,size,screen):
	    b=pygame.font.SysFont(font,size).render('Score : '+str(self.a),True,color)
	    b_rect=b.get_rect()
	    b_rect.centerx=pos[0]
	    b_rect.centery=pos[1]
	    screen.blit(b,b_rect)