import pygame
from random import randint
pygame.init()
#Constantes de el color de fondo y el tipo de letra que se va a usar
letra=pygame.font.Font(None,20)
colorFondo=(255,180,40)
#Constantes del tamaño de la pantalla y el titulo
win= pygame.display.set_mode((500,500))
pygame.display.set_caption("pyDakarDeath")
#Constantes y Variables del vehiculo y Jugador
Carro1=pygame.image.load("car1.png") 
Jugador=Carro1.get_rect()
Jugador.centerx=500/2
Jugador.centery=450
velocidad=5
#Constantes y variables de el obstaculo del cactus
Cactus1=pygame.image.load("Cactus1.png")
Obstaculo1=Cactus1.get_rect()
Obstaculo1.centerx=randint(10,450)
Obstaculo1.centery=-10
velocidadObst=10
aparece=False
#Variable que va a mostrar la puntuacion de la pantalla, se modifica dentro del while
punt=0        
#Variable que se mantiene True hasta que se termine el programa y ocasiona que se termine el while
run=True
#Variable que multiplica el tiempo en el cual los obstaculos van a salir en la parte superior de la pantalla
tick=1
#Loop que hace que se mantenga actualizandose la pantalla
while run:
    Tiempo=pygame.time.get_ticks()/1000
    if(Tiempo==tick*3):
        dibujar=True
        tick+=1
    else:
        dibujar=False
    puntuacion=letra.render("Jugador1:"+str(punt), 0,(0,0,0))
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys= pygame.key.get_pressed()    
    if keys[pygame.K_LEFT]and Jugador.left>0+velocidad:
        Jugador.centerx-=velocidad   
    if keys[pygame.K_RIGHT]and Jugador.right<500-velocidad:
        Jugador.centerx+=velocidad     
    if keys[pygame.K_UP]and Jugador.top>0+velocidad:
        Jugador.centery-=velocidad
    if keys[pygame.K_DOWN]and Jugador.bottom<500-velocidad:
        Jugador.centery+=velocidad
    if(dibujar==True):
        aparece=True
    if(aparece==True):
        Obstaculo1.centery+=velocidadObst
    if(Obstaculo1.top>=500):
        aparece=False
    punt+=1
    win.fill(colorFondo)
    if(aparece==True):
        win.blit(Cactus1,Obstaculo1)
    win.blit(puntuacion,(0,0))
    win.blit(Carro1,Jugador)
    pygame.display.flip()
pygame.quit()        
