import pygame,random,time,sys

class Snake():

    def __init__(self,screen):
        self.screen=screen
        self.pos=[100,50]
        self.body=[[100,50],[90,50],[80,50]]
        self.direction='RIGHT'
        self.change_to=self.direction

    def check_direction(self):
        if self.change_to=='RIGHT' and self.direction!='LEFT':
            self.direction='RIGHT'
        elif self.change_to=='LEFT' and self.direction!='RIGHT':
            self.direction='LEFT'
        elif self.change_to=='UP' and self.direction!='DOWN':
            self.direction='UP'
        elif self.change_to=='DOWN' and self.direction!='UP':
            self.direction='DOWN'

    def draw(self,f,score,stgs):
        self.body.insert(0,self.pos[:])
        if self.pos==f.pos:
            score.a+=1
            f.spawn=False
        else:
            self.body.pop()
        pygame.draw.rect(self.screen,(230,230,230),pygame.Rect(f.pos[0],f.pos[1],10,10))
        for i in self.body:
            if i==self.pos:
                pygame.draw.rect(self.screen,(230,230,0),pygame.Rect(i[0],i[1],10,10))
            else:
                pygame.draw.rect(self.screen,(0,230,0),pygame.Rect(i[0],i[1],10,10))

    def game_over(self,f,score,stgs):
        go=False
        screen_rect=self.screen.get_rect()
        for i in range(len(self.body)):
            if self.pos==self.body[i] and i!=0:
                go=True
                break
        if self.pos[0]==screen_rect.left-10 or self.pos[0]==screen_rect.right or self.pos[1]==screen_rect.top+10 or self.pos[1]==screen_rect.bottom:
            go=True
        if go:
            a=pygame.font.SysFont('helvetica',50).render('GAME OVER',True,(240,240,0))
            b=pygame.font.SysFont('helvetica',25).render('SCORE : '+str(score.a),True,(0,240,0))
            a_rect=a.get_rect()
            a_rect.centerx=stgs.screen_width//2
            a_rect.centery=stgs.screen_height//2
            b_rect=b.get_rect()
            b_rect.centerx=stgs.screen_width//2
            b_rect.centery=3*stgs.screen_height//4
            self.screen.fill(stgs.bg_color)
            self.screen.blit(a,a_rect)
            self.screen.blit(b,b_rect)
            pygame.display.flip()
            time.sleep(3)
            sys.exit()

    def update(self,f,score,stgs):
        self.check_direction()
        if self.direction=='RIGHT':
            self.pos[0]+=10
        elif self.direction=='LEFT':
            self.pos[0]-=10
        elif self.direction=='UP':
            self.pos[1]-=10
        elif self.direction=='DOWN':
            self.pos[1]+=10
        self.draw(f,score,stgs)
        self.game_over(f,score,stgs)
