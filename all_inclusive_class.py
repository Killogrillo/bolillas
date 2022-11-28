import pygame as pg

class Figura:
    def __init__(self,pos_x,pos_y,w=20,h=20,color=(255,255,255),vx=1,vy=1,radio=20):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx=vx
        self.vy=vy
        self.radio = radio

    def moverRectangulo(self,xmax,ymax):
        self.pos_x += self.vx
        self.pos_y += self.vy        
        
        if  self.pos_x <= 0 or self.pos_x >= (xmax-self.w):
            self.vx *= -1

        if self.pos_y <= 0 or self.pos_y >= (ymax-self.h):
            self.vy *=-1

    def moverCirculo(self,xmax,ymax):
        self.pos_x += self.vx
        self.pos_y += self.vy        
        
        if  self.pos_x <= 0 or self.pos_x >= (xmax-self.radio):
            self.vx *= -1

        if self.pos_y <= 0 or self.pos_y >= (ymax-self.radio):
            self.vy *= -1        

    def dibujarRectangulo(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x,self.pos_y,self.w,self.h)) 

    def dibujarCirculo(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)           