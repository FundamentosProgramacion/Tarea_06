# Autor: Carlos Martínez
# El siguiente programa es un espirográfo para dibujar figuras con círculos en pygame

# Librerías que se ocupan en el programa
import pygame, math, random
from math import sin, cos, radians


def espirografo(ventana, w, h, r, R, l):

    # Paleta de colores
    naranja = (250, 152, 58)
    rojo = (235, 47, 6)
    azul = (30, 55, 153)

    # Constante k de la función
    # R = radio externo
    # r = radio interno
    k = r / R

    # El número de vueltas para completar un perdiodo interno
    giros = (r // math.gcd(r, R))

    for angulo in range(0, (giros * 360) + 1, 1):
        # Selección de color
        if (angulo % 3 == 0):
            color = naranja
        elif (angulo % 4 == 0):
            color = rojo
        else:
            color = azul

        a = radians(angulo)  # Convierte a radianes
        x = int(R * ((1 - k) * cos(a) + l * k * (cos(((1 - k) / k) * a))))
        y = int(R * ((1 - k) * sin(a) - l * k * (sin(((1 - k) / k) * a))))
        pygame.draw.circle(ventana, color, (x + w // 2, h // 2 - y), 1)

def dibujar(r, R, l):
    ANCHO = 800
    ALTO = 800

    BLANCO = (255, 255, 255)

    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        # Utilizamos la función para dibujar la figura
        espirografo(ventana, ANCHO, ALTO, r, R, l)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def main():
    dibujar(255, 150, .6)

main()
