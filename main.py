import pygame as pg

#inicializar todos los modulos de pygame
#pantallas,sonidos,teclados,etc..

from figura_class import Rectangulo, Bolillas

pg.init()

#creamos una pantalla o sourface
pantalla_principal = pg.display.set_mode( (800,600) )#ventana y tamaño de ventana
pg.display.set_caption("Bolillas Rebotando")#titulo de la ventana

rect1 = Rectangulo(450,350)
rect2 = Rectangulo(350,250,color=(192, 57, 43))
bolilla1=Bolillas(400,300)
bolilla2 = Bolillas(300,200,color=(192, 57, 43))


#Variable para parar el bucle
game_over = False
while not game_over:
    

    for eventos in pg.event.get():#captura todos los eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (52, 152, 219) )#asignar color a la pantalla


    rect1.mover(800,600)
    rect2.mover(800,600)
    bolilla1.mover(800,600)
    bolilla2.mover(800,600)

    #la sourface o pantalla #color en rgb #posicion(posicionA,posicionL, tamañodel rect L,tamaño rect A)
    
    pg.draw.rect(pantalla_principal,rect1.color,(rect1.pos_x,rect1.pos_y,rect1.w,rect1.h))#metodo para dibujar un rectangulo
    pg.draw.rect(pantalla_principal,rect2.color,(rect2.pos_x,rect2.pos_y,rect2.w,rect2.h))#metodo para dibujar un rectangulo

    pg.draw.circle(pantalla_principal,bolilla1.color,(bolilla1.pos_x,bolilla1.pos_y),bolilla1.radio)
    pg.draw.circle(pantalla_principal,bolilla2.color,(bolilla2.pos_x,bolilla2.pos_y),bolilla2.radio)

    bolilla1.dibujar(pantalla_principal)
    bolilla2.dibujar(pantalla_principal)
    rect1.dibujar(pantalla_principal)
    rect2.dibujar(pantalla_principal)

    pg.display.flip()

pg.quit()