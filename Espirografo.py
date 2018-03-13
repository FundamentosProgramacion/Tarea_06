#Autor:Nataly Paulina Lopez Salazar
#Espirografo
import pygame
from random import randint
import math

# Dimensiones de la pantalla

ANCHO = 800

ALTO = 800

# Colores

BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]

VERDE_BANDERA = (0, 122, 0)

ROJO = (255, 0, 0)


# Estructura básica de un programa que usa pygame para dibujar

def dibujarFiguras(ventana, r, R, l):
    k =  (r/R)
    azar = (randint(0,255),randint(0,255),randint(0,255))

    for alfa in range(0,((r//math.gcd(r,R))*360)+1,1):
        rad = math.radians(alfa) #convierte radianes
        x = int(R*((1-k)*math.cos(rad)+1*k*(math.cos(((1-k)/k)*rad))))
        y = int(R * ((1 - k) * math.sin(rad) - 1 * k * (math.sin(((1 - k) / k) * rad))))
        pygame.draw.circle(ventana,azar,(x+ANCHO//2,ALTO//2-y),1)

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

        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        dibujarFiguras(ventana,r,R,l)



        pygame.display.flip()  # Actualiza trazos

        reloj.tick(40)  # 40 fps

    # Después del ciclo principal

    pygame.quit()  # termina pygame


def main():
    r = int(input("Dame el valor de r:"))
    R = int(input("Dame el valor de R:"))
    l = int(input("Dame el valor de l:"))

    dibujar(r,R,l)


main()