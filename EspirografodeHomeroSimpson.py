
from math import *
import math
import pygame
import random


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()     # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución

    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        radio = 100
        for angulo in range (0,360+1,1):
            r=350
            R=170
            l=0.5
            a = math.radians(angulo)
            k = r//R
            giros = r//math.gcd(r,R)
            x = R*((1-k)*cos(a)+l*k*cos((1-k//k)*a))
            y = R*((1-k)*sin(a)-l*k*sin((1-k//k)*a))
            colorAzar = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.circle(ventana,colorAzar,(int(x+ANCHO//3), int(ALTO//2-y)),100,1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def main():
    dibujar()


main()