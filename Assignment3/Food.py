import pygame,random

class Food():

    def __init__(self,screen,stgs):
        self.screen=screen
        self.pos=[random.randrange(0,(stgs.screen_width//10))*10,random.randrange(2,(stgs.screen_height//10))*10]
        self.spawn=True
        self.stgs=stgs

    def update(self):
        if not self.spawn:
            self.pos=[random.randrange(0,(self.stgs.screen_width//10))*10,random.randrange(2,(self.stgs.screen_height//10))*10]
            self.spawn=True