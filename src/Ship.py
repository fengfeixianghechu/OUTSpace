import pygame


class Ship():  
    def __init__(self, screen, shipIMGPath): #"""初始化飞船并设置其初始位置"""
        self.screen = screen  #pygame的屏幕
        self.shipIMGPathLoc = shipIMGPath #图片路径
        self.speed = 3 #默认三个像素移动
        self.screen_rect = self.screen.get_rect()
        self.screen_centerx = self.screen_rect.centerx#屏幕的行向中心点
        self.screen_bottom = self.screen_rect.bottom #游戏屏幕的底部 
    def load_shipIMG(self):#加载图片
        self.image = pygame.image.load(self.shipIMGPathLoc) #加载飞船图片
    def getRect(self):#获取图片的大小;
        self.rect = self.image.get_rect() #获取图片的大小
    def init_ship(self):
        self.rect.centerx = self.screen_centerx #将飞船的设置到屏幕的中间
        self.rect.bottom  = self.screen_bottom
    def blitme(self): 
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)
