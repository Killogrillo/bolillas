import pygame as pg

class Rectangulo:
    def __init__(self,pos_x,pos_y,w=20,h=20,color=(255,255,255),vx=1,vy=1):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color

        self.vx = 0
        self.vy = 0

    def mover(self,xmax,ymax):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.pos_x <= 0 or self.pos_x >= (xmax-self.w):
            self.vx *= -1

        if self.pos_y <= 0 or self.pos_y >= (ymax-self.h):
            self.vy *=-1

    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x,self.pos_y,self.w,self.h))

    



class Bolillas:
    def __init__(self,pos_x,pos_y,color=(255,255,255),radio=20,vx=1,vy=1):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color 
        self.vx = vx
        self.vy = vy

    def mover(self,xmax,ymax):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.pos_x <= 0 or self.pos_x >= (xmax-self.radio):
            self.vx *= -1

        if self.pos_y <= 0 or self.pos_y >= (ymax-self.radio):
            self.vy *=-1

    
    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)