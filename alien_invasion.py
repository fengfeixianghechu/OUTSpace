import sys
import pygame

def run_game():
    pygame.init() #初始化游戏界面
    bg_color = (230,230,230) #设置背景色
    screen =pygame.display.set_mode((1200,800))  #初始化界面的大小
    pygame.display.set_caption("宇宙大战")
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
            screen.fill(bg_color)   
        pygame.display.flip()#让最近绘制的颜色屏幕可见
    
run_game()