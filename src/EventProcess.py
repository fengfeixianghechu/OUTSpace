import sys
import pygame
def EventProcess(even):
    for evenTmp in even:
        if evenTmp.type == pygame.QUIT:#退出界面
            sys.exit()