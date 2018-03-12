##Autor: David Medina Medina A01653311
##Espirografo

import pygame
from random import *
from math import *

ancho = 800
alto = 800
blanco = (255,255,255)
cafe = (139,69,19)
b = ancho//2
c = alto//2

def dibujar(R,r,l,cafe):
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(blanco)
        Espirografo(ventana,r,R,l,cafe)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def Espirografo(v,r,R,l,q):
    g = r // gcd(r, R)
    for angulo in range(0,g*360+1,1):
        k = r/R
        a = radians(angulo)
        x = int(R*((1-k)* cos(a)+l*k*(cos(((1-k)/k)*a))))
        y = int(R*((1-k)* sin(a)-l*k*(sin(((1-k)/k)*a))))
        pygame.draw.circle(v, q, (x + b, c-y),1)

def main():
    r = int(input("Ingresar r: "))
    R = int(input("Ingresar R: "))
    l = float(input("Ingresar l: "))
    dibujar(r,R,l,cafe)
main()
