import pygame,sys,time,random
from Settings import Settings
from S import Snake
from Food import Food
from Score import Score
import game_functions as gf

def run_game():
    pygame.init()
    stgs=Settings()
    screen=pygame.display.set_mode((stgs.screen_width,stgs.screen_height))
    pygame.display.set_caption('Snake Eater')
    s=Snake(screen)
    f=Food(screen,stgs)
    fps_controller=pygame.time.Clock()
    score=Score(0)

    while True:
        screen.fill(stgs.bg_color)
        pygame.draw.rect(screen,stgs.top_color,pygame.Rect(0,0,stgs.top_width,stgs.top_height))
        gf.check_events(s)
        gf.update_screen(s,f,score,stgs,screen)
        fps_controller.tick(25)

run_game()