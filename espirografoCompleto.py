#autor: Diana Aguilar
#descripción: dibujar rosa
import pygame
import math
from random import randint
#from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def dibujarEspiro(ventana,r,R,l):
    k= (r/R)
    random = (randint(0, 255), randint(0, 255), randint(0, 255))

    for alpha in range(0, ((r//math.gcd(r,R))*360)+1, 1):
        a = math.radians(alpha)  # Convierte a radianes
        x = int(R*((1-k)* math.cos(a)+l*k*(math.cos(((1-k)/k)*a))))
        y = int(R*((1-k)* math.sin(a)-l*k*(math.sin(((1-k)/k)*a))))
        pygame.draw.circle(ventana, random, (x + ANCHO // 2, ALTO // 2 - y),1)
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
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        dibujarEspiro(ventana,r,R,l)


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(60)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame



def main():
    r= int(input("Teclee el valor de r: "))
    R = int(input("Teclee el valor de r: "))
    l = float(input("Teclee el valor de r: "))
    dibujar(r,R,l)



main()