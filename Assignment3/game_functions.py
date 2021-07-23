import pygame,sys,time,random

def check_events(s):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                s.change_to='RIGHT'
            elif event.key==pygame.K_LEFT:
                s.change_to='LEFT'
            elif event.key==pygame.K_UP:
                s.change_to='UP'
            elif event.key==pygame.K_DOWN:
                s.change_to='DOWN'

def update_screen(s,f,score,stgs,screen):
    score.show([100,10],(240,240,240),"helvetica",20,screen)
    s.update(f,score,stgs)
    f.update()
    pygame.display.flip()