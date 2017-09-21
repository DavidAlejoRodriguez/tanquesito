import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 10
		self.estado = "bajando"
		self.imagenes = [util.cargar_imagen('imagenes/Tanque.png'),
						util.cargar_imagen('imagenes/tanque destruido.png'),
						util.cargar_imagen('imagenes/Tanque.png'),
						util.cargar_imagen('imagenes/Tanque.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(200, 500)
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			if teclas[K_LEFT] and self.rect.x>=10:
				self.rect.x -= 10
			elif teclas[K_RIGHT] and self.rect.x<=680-self.rect.width:
				self.rect.x += 10
			(""")if teclas[K_UP] and self.rect.y>=10:
				self.rect.y -= 10
				self.image = self.imagenes[2]
				if self.rect.y==0 and self.estado == "subiendo":
					self.puntos = self.puntos + 1
					self.estado = "bajando"
			elif teclas[K_DOWN] and self.rect.y<=640-self.rect.height:
				self.rect.y += 10
				self.image = self.imagenes[0]
				if self.rect.y==410 and self.estado == "bajando":
					self.puntos = self.puntos + 1
					self.estado = "subiendo"(""")
		else:
			self.image = self.imagenes[3]
