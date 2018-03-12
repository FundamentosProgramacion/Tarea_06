#Autor: Jean Paul Esquivel Lobato
#Dibujo del espirógrafo

import pygame
import math
from random import randint

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

def espirografo(ventana,r,R,l):
    k= (r/R)
    kA= ((1-k)/k)
    p= r//math.gcd(r,R)
    vueltas= p*360
    ColorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))

    for angulo in range(0, vueltas+1, 1):
        a = math.radians(angulo)  # Convierte a radianes
        x = int(R*((1-k)* math.cos(a)+l*k*(math.cos(kA*a))))
        y = int(R*((1-k)* math.sin(a)-l*k*(math.sin(kA*a))))
        pygame.draw.circle(ventana, ColorAzar, (x + ANCHO // 2, ALTO // 2 - y),1)

# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):

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
        espirografo(ventana,r,R,l)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

#función principal
def main():
    radioCirculoMenor= int(input("r: "))
    radioCirculoMayor= int(input("R: "))
    l= float(input("l: "))

    dibujar(radioCirculoMenor,radioCirculoMayor,l)

main()