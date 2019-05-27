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
def thread_function():
    while True and firstime == False:
        message, address = sock.recvfrom(255)
        values = pickle.loads(message)
        if(values[0] == "puntajes"):
            listbox.insert(END, values[1])
        elif values[0] != nam:
            print(values)
def destruirMenu():
    Menu.destroy()
    canvaElegirJ()
def destruirElegirJ():
    ElegirJ.destroy()
    canvaMenu()
def IrAlJuego():
    add()
    nombre=entrada.get()
    ElegirJ.destroy()
    Main.iconify()
    Juego(nombre)
def add():
    values=[entrada.get(), btnSiguiente.cget('text')] 
    data=pickle.dumps(values)
    sock.sendto(data, (multicast_addr, port))    

def canvaElegirJ():
    global ElegirJ
    global entrada
    global btnSiguiente
    ElegirJ=tk.Canvas(Main, height = 700, width = 600,bg="DarkGoldenrod2")
    ElegirJ.pack(fill=tk.BOTH, expand=True)    
    lblNuevoJugador=tk.Label(ElegirJ,text="Si eres un nuevo Jugador, ingresa tu nombre aquí",bg="DarkGoldenrod2",fg="white",bd=0,font=("Times", 18))
    lblNuevoJugador.pack(side=tk.TOP)
    entrada=tk.Entry(ElegirJ)
    entrada.pack(side=tk.TOP)
    lblCargarJugador=tk.Label(ElegirJ,text="Si ya habias jugado antes, busca tu nombre aquí",bg="DarkGoldenrod2",fg="white",bd=0,font=("Times", 18))
    lblCargarJugador.pack(side=tk.TOP)
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
def Juego(nombre):
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
    velocidad=10
    choca=False
    chocaPiedra=False
    perder=0
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
    punt=0
    #Variable que se mantiene True hasta que se termine el programa y ocasiona que se termine el while
    run=True  
    #Loop que hace que se mantenga actualizandose la pantalla
    while run:        
        puntuacion=letra.render(str(nombre)+":"+str(punt), 0,(0,0,0))
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

            
        if Jugador.colliderect(Obstaculo1)and choca==False:
            punt-=200
            choca=True
            Choque.play()
        elif(choca==True and Jugador.colliderect(Obstaculo1)!= True):
            choca=False
            perder+=1

            
        if Jugador.colliderect(Obstaculo2)and chocaPiedra==False:
            punt-=200
            chocaPiedra=True
            Choque.play()
        elif(chocaPiedra==True and Jugador.colliderect(Obstaculo2)!= True):
            chocaPiedra=False
            perder+=1
            
        if(perder==5):
            run=False
        punt+=5
        win.fill(colorFondo)
        win.blit(Piedra,Obstaculo2)
        win.blit(Cactus1,Obstaculo1)
        win.blit(puntuacion,(0,0))
        win.blit(Carro1,Jugador)
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
multicast_addr = '224.0.0.3'
bind_addr = '0.0.0.0'          
port = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)
Main.mainloop()
