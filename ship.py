import pygame
class ship():  
    def __init__(self, screen, shipIMGPath): """初始化飞船并设置其初始位置"""
        self.screen = screen  #pygame的屏幕
        self.shipIMGPath = shipIMGPath #图片路径
        self.speed = 3 #默认三个像素移动
        self.image #用于存储飞机图片
        self.rect #存储飞船的范围
        self.screen_centerx = self.screen.centerx#屏幕的行向中心点
        self.screen_bottom = self.screen.bottom #游戏屏幕的底部
    def load_ship():#加载图片
        self.image = pygame.image.load(self.shipIMGPath) #加载飞船图片
    def getRect():#获取图片的大小;
        self.rect = self.image.rect() #获取图片的大小
    def init_ship():
        self.rect.centerx = self.screen_centerx #将飞船的设置到屏幕的中间
        self.rect.bottom  = self.screen_centerx
        
