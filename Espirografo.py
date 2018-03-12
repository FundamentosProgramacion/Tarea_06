import pygame
import math
from random import randint

ANCHO = 800
ALTO = 800
centroX = ANCHO//2
centroY = ALTO//2

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


def estrella(radio, Radio, l, r2, R2, l2, r3, R3, l3):
#Esta función usa un ciclo for para generar circulos y cuadrados en el rango de la ventana
	pygame.init()
	ventana = pygame.display.set_mode((ANCHO, ALTO))
	reloj = pygame.time.Clock()
	termina = False
	while not termina: #Ciclo Principal de Pygame
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
				termina = True
		ventana.fill(NEGRO)


		k = radio/Radio
		vueltas = radio//math.gcd(radio, Radio)
		while vueltas > 0:
			for ang in range (0, 361, 5):
				a = math.radians(ang)
				x = int((((l-k)*math.cos(a))+(l*k*math.cos((l-k/(k))*a))) * Radio)
				y = int((((l-k)*math.sin(a))+((l*k)*math.sin((l-k)/k)*a))  * Radio)
				randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
				pygame.draw.circle(ventana, randomColor, (centroX + x,  centroY + y), radio, 1)
			vueltas = vueltas - 1

			k2 = r2 / R2
			vueltas = r2 // math.gcd(r2, R2)
			while vueltas > 0:
				for ang in range(0, 361, 5):
					a = math.radians(ang)
					x = int((((l2 - k2) * math.cos(a)) + (l2 * k2 * math.cos((l2 - k2 / (k2)) * a))) * R2)
					y = int((((l2 - k2) * math.sin(a)) + ((l2 * k2) * math.sin((l - k2) / k2) * a)) * R2)
					randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
					pygame.draw.circle(ventana, randomColor, (centroX + x, centroY + y), r2, 1)
				vueltas = vueltas - 1

		k3 = r3 / R3
		vueltas = r3 // math.gcd(r3, R3)
		while vueltas > 0:
			for ang in range(0, 361, 5):
				a = math.radians(ang)
				x = int((((l3 - k3) * math.cos(a)) + (l3 * k3 * math.cos((l3 - k3 / (k3)) * a))) * R3)
				y = int((((l3 - k3) * math.sin(a)) + ((l3 * k3) * math.sin((l3 - k3) / k3) * a)) * R3)
				randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
				pygame.draw.circle(ventana, randomColor, (centroX + x, centroY + y), r3, 1)
			vueltas = vueltas - 1

		pygame.display.flip()
		reloj.tick(40)

	pygame.quit()  # termina pygame


def main():
	radio = int(input("radio menor: "))
	_Radio_  = int(input("Radio Mayor: "))
	l = float(input("Valor de PC/r: "))
	radio2 = int(input("radio menor 2: "))
	_Radio2 = int(input("Radio Mayor 2: "))
	l2 = float(input("valor 2 e l: "))
	radio3 = int(input("radio menor 3: "))
	_Radio3 = int(input("Radio Mayor 3: "))
	l3 = float(input("valor 3 de l: "))
	estrella(radio, _Radio_, l, radio2, _Radio2, l2, radio3, _Radio3, l3)

main()

'''Dibujo 1 con los siguientes valores
radio menor: 120
Radio Mayor: 550
Valor de PC/r: .4648465
radio menor 2: 180
Radio Mayor 2: 360
valor 2 e l: .222355
radio menor 3: 220
Radio Mayor 3: 710
valor 3 de l: .789798
'''