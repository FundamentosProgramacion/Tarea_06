#encoding: UTF-8
#autor: Genaro Ortiz Durán
#Descripción: Dibujar figuras tipo espirógrafo con funciones.
import pygame
import math



# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
radio=100


def dibujarGiro(ventana,r, R, l):
    k=r/R
    p= r//math.gcd(r,R)
    kAngulo =((1-k)/ k)
    for i in range(0,p*361,1):
        a = math.radians (i)
        x = int ( R * ((1 - k) * math.cos ( a ) + l * k * (math.cos ( kAngulo * a ))) )
        y = int ( R * ((1 - k) * math.sin ( a ) - l * k * (math.sin ( kAngulo * a ))) )
        pygame.draw.circle ( ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1 )


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init ()
    ventana = pygame.display.set_mode ( (ANCHO, ALTO) )  # Crea la ventana de dibujo
    reloj = pygame.time.Clock ()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get ():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill ( BLANCO )

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        dibujarGiro(ventana,r,R,l)
        pygame.display.flip ()  # Actualiza trazos
        reloj.tick ( 40 )  # 40 fps

    # Después del ciclo principal
    pygame.quit ()  # termina pygame





def main():
    r=int(input("Escribe r:"))
    R=int(input("Escribe R:"))
    l=float(input("Escribe l:"))

    dibujar(r,R,l)


main ()