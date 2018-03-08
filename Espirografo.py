# Fernando Sebastian Silva M
# Espirografo
from math import *
import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)


# Estructura básica de un programa que usa pygame para dibujar
def calcularPeriodo(r, R):
    return r//gcd(r,R)


def calcularX(alfaRad, k, l, R):
    x = R*((k-1)*cos(alfaRad)+(l*cos((k-1)*alfaRad)))
    return int(x)

def calcularY(alfaRad, k, l, R):
    y = R*((k-1)*sin(alfaRad)-(l*sin((k-1)*alfaRad)))
    return int(y)


def colorAzar(x):
    if x%2 == 0:
        return ROJO
    return AZUL




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

        # Dibujar, aquí haces todos los trazos que requiera
        k = r / R
        periodo = 0
        while periodo != calcularPeriodo(r,R):
            periodo += 1
            for grados in range(0, (360*(calcularPeriodo(r,R))+1)):
                alfaRad = radians(grados)
                x = calcularX(alfaRad, k, l, R)
                y = calcularY(alfaRad, k, l, R)
                pygame.draw.circle(ventana, colorAzar(grados), (x + ANCHO // 2, y + ALTO // 2), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    r =  int(input("Dame r "))
    R = int(input("Dame R "))
    l = float(input("Dame L "))
    dibujar(r,R,l)

main()
