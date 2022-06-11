import pygame as pg
#动画精灵↓ 
class Shape(pg.sprite.Sprite):
    def __init__(self,image_file,location):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
    def move(self,x,y):
        #移动
        self.rect.left,self.rect.top=x,y

class Blue(Shape):
    def __init__(self,image_file,location):
        Shape.__init__(self,image_file,location)
        self.m=0
        self.positions=[]
    def place(self,positions):
        self.positions=positions
        self.move(self.positions[self.m][0],self.positions[self.m][1])
        self.m+=1
        self.m=self.m%len(self.positions)
