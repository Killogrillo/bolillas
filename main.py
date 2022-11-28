import pygame as pg

#inicializar todos los modulos de pygame
#pantallas,sonidos,teclados,etc..
pg.init()

#creamos una pantalla o sourface
pantalla_principal = pg.display.set_mode( (800,600) )#ventana y tamaño de ventana
pg.display.set_caption("Bolillas Rebotando")#titulo de la ventana

#Variable para parar el bucle
game_over = False

x=400
y=300
vx=1
vy=1

x2=300
y2=200
vx2=1
vy2=1





while not game_over:
    

    for eventos in pg.event.get():#captura todos los eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (52, 152, 219) )#asignar color a la pantalla
    x += vx
    y += vy

    x2= vx2
    y2 = vy2

    if x >= 800 or x==0:#llegue a los limites
        vx*= -1
    if y >= 600 or y==0:
        vy*= -1

    if x2 >= 300 or x2==0:#llegue a los limites
        vx2*= -1
    if y2 >= 200 or y2==0:
        vy2*= -1


    '''
        x += 1
        if y != 580:
            y += 1

    if x==780:
        x-=1
        '''

                #la sourface o pantalla #color en rgb #posicion(posicionA,posicionL, tamañodel rect L,tamaño rect A)
    pg.draw.rect(pantalla_principal,(192, 57, 43),(x,y,20,20))#metodo para dibujar un rectangulo

    pg.draw.rect(pantalla_principal,(255, 255, 0),(x2,y2,20,20))


    pg.display.flip()



pg.quit()