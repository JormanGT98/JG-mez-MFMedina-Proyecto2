import tkinter as tk
import pygame
import random
import socket
import struct
import pickle
import logging
import threading
import time
from os import path
from random import randint
#def thread_function():
 #   while True and firstime == False:
  #      message, address = sock.recvfrom(255)
   #     values = pickle.loads(message)
    #    if(values[0] == "puntajes"):
     #       listbox.insert(END, values[1])
      #  elif values[0] != nam:
       #     print(values)
def destruirMenu():
    Menu.destroy()
    canvaElegirJ()
def destruirElegirJ():
    ElegirJ.destroy()
    canvaMenu()
def IrAlJuego():
    #add()
    nombre1=entrada1.get()
    nombre2=entrada2.get()
    ElegirJ.destroy()
    Main.iconify()
    Juego(nombre1,nombre2)
#def add():
    #values=[entrada.get(), btnSiguiente.cget('text')] 
    #data=pickle.dumps(values)
    #sock.sendto(data, (multicast_addr, port))    

def canvaElegirJ():
    global ElegirJ
    global entrada1
    global entrada2
    global btnSiguiente
    ElegirJ=tk.Canvas(Main, height = 700, width = 600,bg="DarkGoldenrod2")
    ElegirJ.pack(fill=tk.BOTH, expand=True)    
    lblJugador1=tk.Label(ElegirJ,text="Ingresa el nombre del Jugador1",bg="DarkGoldenrod2",fg="white",bd=0,font=("Times", 18))
    lblJugador1.pack(side=tk.TOP)
    entrada1=tk.Entry(ElegirJ)
    entrada1.pack(side=tk.TOP)
    lblJugador2=tk.Label(ElegirJ,text="Ingresa el nombre del Jugador2",bg="DarkGoldenrod2",fg="white",bd=0,font=("Times", 18))
    lblJugador2.pack(side=tk.TOP)
    entrada2=tk.Entry(ElegirJ)
    entrada2.pack(side=tk.TOP)
    btnSiguiente=tk.Button(ElegirJ,text="Siguiente",bg="DarkGoldenrod2",fg="white",bd=0,command=IrAlJuego,font=("Times", 18))
    btnSiguiente.pack(side=tk.TOP)
    btnVolver=tk.Button(ElegirJ,text="Volver al Menu Principal",bg="DarkGoldenrod2",fg="white",bd=0,command=destruirElegirJ,font=("Times", 18))
    btnVolver.pack(side=tk.TOP)
        
def canvaMenu():
    global Menu
    Menu=tk.Canvas(Main,height=700,width=600,bg="DarkGoldenrod2")
    Menu.pack(fill=tk.BOTH, expand=True)
    LblTitulo=tk.Label(Menu,text="pyDakarDeath",bg="DarkGoldenrod2",fg="White",bd=0,font=("Arial", 40))
    LblTitulo.pack(side=tk.TOP)
    NuevoJuegoBtn=tk.Button(Menu,text="Nueva Partida",bg="DarkGoldenrod2",fg="White",bd=0,font=("Times", 24),command=destruirMenu)
    NuevoJuegoBtn.pack(side=tk.TOP)
    PuntajeBtn=tk.Button(Menu,text="Mejores Puntuaciones",bg="DarkGoldenrod2",fg="White",font=("Times", 24),bd=0)
    PuntajeBtn.pack(side=tk.TOP)
    SalirBtn=tk.Button(Menu,text="Salir",bg="DarkGoldenrod2",fg="White",font=("Times", 24),command=Main.destroy,bd=0)
    SalirBtn.pack(side=tk.TOP)
    Main.mainloop()
def Juego(nombre1,nombre2):
    pygame.init()
    #Constantes de el color de fondo y el tipo de letra que se va a usar
    letra=pygame.font.Font(None,20)
    colorFondo=(255,180,40)
    #Constantes del tamaño de la pantalla y el titulo
    win= pygame.display.set_mode((500,500))
    pygame.display.set_caption("pyDakarDeath")
    #Constantes y Variables del vehiculo1 y Jugador1
    Carro1=pygame.image.load("car1.png") 
    Jugador1=Carro1.get_rect()
    Jugador1.centerx=200
    Jugador1.centery=450
    velocidad=10
    chocaJugador1=False
    chocaPiedraJugador1=False
    perderJugador1=0
    #Constantes y variables del vehiculo2 y jugador2
    Carro2=pygame.image.load("car2.png")
    Jugador2=Carro2.get_rect()
    Jugador2.centerx=400
    Jugador2.centery=450
    chocaJugador2=False
    chocaPiedraJugador2=False
    perderJugador2=0
    #Constantes y variables de el obstaculo del cactus
    Cactus1=pygame.image.load("Cactus1.png")
    Obstaculo1=Cactus1.get_rect()
    velocidadObst=20
    aparece=False
    #Constantes y variables de el obstaculo piedra
    Piedra=pygame.image.load("rock2.png")
    Obstaculo2=Piedra.get_rect()
    aparecePiedra=False    
    #Constantes de los sonidos que se van a reproducir
    pygame.mixer.music.load("SonidoFondo.mp3")
    pygame.mixer.music.play(4)
    Choque=pygame.mixer.Sound("Choque.wav")
    #Variable que va a mostrar la puntuacion de la pantalla, se modifica dentro del while
    puntJugador1=0
    puntJugador2=0
    #Variable que se mantiene True hasta que se termine el programa y ocasiona que se termine el while
    run=True  
    #Loop que hace que se mantenga actualizandose la pantalla
    while run:        
        puntuacionJugador1=letra.render(str(nombre1)+":"+str(puntJugador1), 0,(0,0,0))
        puntuacionJugador2=letra.render(str(nombre2)+":"+str(puntJugador2), 0,(0,0,0))
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        keys= pygame.key.get_pressed()    
        if keys[pygame.K_LEFT]and Jugador1.left>0+velocidad:
            Jugador1.centerx-=velocidad
        if keys[pygame.K_RIGHT]and Jugador1.right<500-velocidad:
            Jugador1.centerx+=velocidad
        if keys[pygame.K_UP]and Jugador1.top>0+velocidad:
            Jugador1.centery-=velocidad
        if keys[pygame.K_DOWN]and Jugador1.bottom<500-velocidad:
            Jugador1.centery+=velocidad
        if keys[pygame.K_a]and Jugador2.left>0+velocidad:
            Jugador2.centerx-=velocidad
        if keys[pygame.K_d]and Jugador2.right<500-velocidad:
            Jugador2.centerx+=velocidad
        if keys[pygame.K_w]and Jugador2.top>0+velocidad:
            Jugador2.centery-=velocidad
        if keys[pygame.K_s]and Jugador2.bottom<500-velocidad:
            Jugador2.centery+=velocidad
            
        if(Obstaculo1.centery>=550):
            aparece=False
        if(aparece==False):
            Obstaculo1.centery=-10
            Obstaculo1.centerx=randint(10,450)
            aparece=True
        else:
            Obstaculo1.centery+=velocidadObst

        
        if(Obstaculo2.centery>=550):
            aparecePiedra=False
        if(aparecePiedra==False):
            Obstaculo2.centery=-300
            Obstaculo2.centerx=randint(10,450)
            aparecePiedra=True
        else:
            Obstaculo2.centery+=velocidadObst

            
        if Jugador1.colliderect(Obstaculo1)and chocaJugador1==False:
            puntJugador1-=200
            chocaJugador1=True
            Choque.play()
        elif(chocaJugador1==True and Jugador1.colliderect(Obstaculo1)!= True):
            choca=False
            perderJugador1+=1

        if Jugador2.colliderect(Obstaculo1)and chocaJugador2==False:
            puntJugador2-=200
            chocaJugador2=True
            Choque.play()
        elif(chocaJugador2==True and Jugador.colliderect(Obstaculo1)!= True):
            chocaJugador2=False
            perderJugador2+=1

            
        if Jugador1.colliderect(Obstaculo2)and chocaPiedraJugador1==False:
            puntJugador1-=200
            chocaPiedraJugador1=True
            Choque.play()
        elif(chocaPiedraJugador1==True and Jugador1.colliderect(Obstaculo2)!= True):
            chocaPiedraJugador1=False
            perderJugador1+=1

            
        if Jugador2.colliderect(Obstaculo2)and chocaPiedraJugador2==False:
            puntJugador2-=200
            chocaPiedraJugador2=True
            Choque.play()
        elif(chocaPiedraJugador2==True and Jugador2.colliderect(Obstaculo2)!= True):
            chocaPiedraJugador2=False
            perderJugador2+=1    
        if(perderJugador1==5):
            run=False
        if( perderJugador2==5):
            run=False
        puntJugador1+=5
        puntJugador2+=5
        win.fill(colorFondo)
        win.blit(Piedra,Obstaculo2)
        win.blit(Cactus1,Obstaculo1)
        win.blit(puntuacionJugador1,(0,0))
        win.blit(puntuacionJugador2,(0,20))
        win.blit(Carro1,Jugador1)
        win.blit(Carro2,Jugador2)
        pygame.display.flip()
    pygame.quit()
    Main.deiconify()
    canvaMenu()

Main=tk.Tk()
Main.title("pyDakarDeath")
Main.config(bg="black")
Main.geometry("600x700+0+0")
Menu=tk.Canvas(Main,height=700,width=600,bg="DarkGoldenrod2")
Menu.pack(fill=tk.BOTH, expand=True)
LblTitulo=tk.Label(Menu,text="pyDakarDeath",bg="DarkGoldenrod2",fg="White",bd=0,font=("Arial", 40))
LblTitulo.pack(side=tk.TOP)
NuevoJuegoBtn=tk.Button(Menu,text="Nueva Partida",bg="DarkGoldenrod2",fg="White",bd=0,font=("Times", 24),command=destruirMenu)
NuevoJuegoBtn.pack(side=tk.TOP)
PuntajeBtn=tk.Button(Menu,text="Mejores Puntuaciones",bg="DarkGoldenrod2",fg="White",font=("Times", 24),bd=0)
PuntajeBtn.pack(side=tk.TOP)
SalirBtn=tk.Button(Menu,text="Salir",bg="DarkGoldenrod2",fg="White",font=("Times", 24),command=Main.destroy,bd=0)
SalirBtn.pack(side=tk.TOP)
#Se maneja el servidor
#multicast_addr = '224.0.0.3'
#bind_addr = '0.0.0.0'          
#port = 3000
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)
Main.mainloop()
