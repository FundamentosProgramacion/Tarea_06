# encoding: UTF-8
# Sebastian Morales Martin
# Tarea_06: mandalas


import pygame
from math import *
from random import randint as ran
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
NARANJA = (255, 131, 0)
def drawRose(ventana, m, k):
    contador = 1
    contador2 = 0
    for alfa in range(0, 360, 1):
        contador -= 3
        alfaRad = radians(alfa)
        r = m* cos(k*alfaRad)
        x = (int(r*cos(alfaRad)) + ANCHO//2)
        y = ALTO//2 - int(r*sin(alfaRad))
        x2 = (int(r*cos(sin(alfaRad)))+ANCHO//2)
        y2 = ALTO//2 - int(r*sin(cos(alfaRad)))
        randomColor = (ran(0, 255), ran(0, 255), ran(0, 255))
        pygame.draw.circle(ventana, randomColor, (x, y), 10, 2)
        contador += 5
        contador2 += 1
        pygame.draw.circle(ventana, ROJO, (x+ contador*2, y - contador*3), 25)
        pygame.draw.circle(ventana, ROJO, (x - contador * 3, y + contador * 2), 25)
        pygame.draw.circle(ventana, BLANCO, (x+contador, y + contador), 20, 0)
        pygame.draw.circle(ventana, BLANCO, (x - contador, y - contador), 20, 0)
        pygame.draw.circle(ventana, VERDE_BANDERA, (x, y//3), 20, 0)
        pygame.draw.circle(ventana, VERDE_BANDERA, (x//3, y), 20, 0)
        pygame.draw.circle(ventana, VERDE_BANDERA, (x//3, y *3), 20, 0)
        pygame.draw.circle(ventana, VERDE_BANDERA, (x*3, y//3), 20, 0)
        pygame.draw.circle(ventana, NARANJA, (x2, y2), 20, 1)
        pygame.draw.circle(ventana, NARANJA, (x2, y2),20, 1)

# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Dimensiones de la pantalla

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
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        drawRose(ventana, 50,10)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def main():
    dibujar()

main()



