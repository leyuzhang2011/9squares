#导入↓
import time as ti
import pygame as pg 
import sys as s
from objects import *
#初始化↓ zhang
cube_x=50;cube_y=450
pg.init()
screen=pg.display.set_mode([650,650]);screen.fill([255,255,255])
shapes=[]
LEVEL=1
def draw():
    screen.blit(bg,[25,25])
    for shape in shapes:
        screen.blit(shape.image,shape.rect)
    pg.display.flip()
def collision():
    for shape in shapes:
        if not shape==cube:
            if shape.rect==cube.rect:
                return True
    return False

#导入，绘制角色↓
bg = pg.image.load("background.png")
screen.blit(bg,[25,25])
cube=Shape("cube.png",[cube_x,cube_y])
shapes.append(cube)
my_ball=Shape("ball.png",[450,50])
shapes.append(my_ball)
#screen.blit(my_ball.image,[450,50])
screen.blit(cube.image,cube.rect)
pg.display.flip()
#感应（按下关闭）↓
running=True
k=0
while running:
    draw()
    if LEVEL==2:
        k+=1
        if k%40==0:
            positions=[[250,450],[250,250],[250,50],[250,250]]
            blue.place(positions)

    if (collision())and(LEVEL==1):
        LEVEL=2
        win=pg.image.load('WIN.png')
        screen.blit(win,[75,250])
        pg.display.flip()
        ti.sleep(0.3)
        cube_x=50;cube_y=450
        cube.move(cube_x,cube_y)
        my_ball.move(450,50)
        blue=Blue("blue cube.png",[250,250])
        shapes.append(blue)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        elif event.type==pg.KEYDOWN:
            if (event.key==pg.K_UP)and(cube_y>=250):
                cube_y-=200
                cube.move(cube_x,cube_y)
            elif (event.key==pg.K_DOWN)and(250>=cube_y):
                cube_y+=200
                cube.move(cube_x,cube_y)
            elif (event.key==pg.K_RIGHT)and(250>=cube_x):
                cube_x+=200
                cube.move(cube_x,cube_y)
            elif (event.key==pg.K_LEFT)and(cube_x>=250):
                cube_x-=200
                cube.move(cube_x,cube_y)
pg.quit()