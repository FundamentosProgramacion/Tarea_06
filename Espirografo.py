#Autor Karla Fabiola Ramirez Martines
#Descripcion Espirografo <3

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
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras

        for angulo in range(0, 360 + 1,1):

            x=ANCHO//2
            y=ALTO//2
            k = r / R
            C = R - r
            P = (l * r) / C
            vueltas = r // math.gcd(r,R)
            v1=0
            while v1<vueltas:
                a = math.radians(angulo)
                v1+=1
                x1= int(R * ((l - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a)))
                y2 = int(R * ((l - k) * math.cos(a) - l * k * math.sin(((1 - k) / k) * a)))
                Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                Color2 = (random.randint(0, 255), 0, random.randint(0, 255))
                pygame.draw.circle(ventana,Color, (x-x1,y-y2),r, 1)

            pygame.draw.circle(ventana, Color2, (x, y), R, 1)
        pygame.display.flip()  # Actualiza trazos14
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame.


def main():
    r=int(input("Dime r: "))
    R=int(input("Dime R: "))
    l=float(input("Dime l: (Favor de mantener el valor lo mas pequeño posible)"))
    dibujar(r,R,l)


main()
