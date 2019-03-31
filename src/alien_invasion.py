import sys
import pygame
from Ship  import Ship as outShip
from EventProcess import EventProcess
from updateScreen import update_screen
def run_game():
    pygame.init() #初始化游戏界面
    bg_color = (230,230,230) #设置背景色
    screen =pygame.display.set_mode((1000,500))  #初始化界面的大小
    pygame.display.set_caption("宇宙大战")
    ship =  outShip(screen,".\\image\\ship.bmp")   #初始化宇宙飞船

    ship.load_shipIMG() #加载宇宙飞船
    ship.getRect()
   
    ship.init_ship()#初始化飞船的位置 
    while True:
        #event = pygame.event.get()
       # update_screen(screen,ship)
       # EventProcess(event)
        ship.blitme()

run_game()