import pygame
from Orbiter import *
import math

class NPCShip(pygame.sprite.Sprite):
	def __init__(self, name, x, y, rot, fire, img, imgFire):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		self.image = pygame.image.load("images/redShip.png")
		self.image = pygame.transform.scale(self.image, (20, 20))
		self.original = self.image
		self.changeValues(x, y, rot)
		self.fireImg = pygame.image.load("images/missileFire.png")
		

	def changeValues(x, y, rot, fire):
		self.x = x
		self.y = y
		self.rot = rot

		self.image = pygame.transform.rotate(self.original, rot)
		self.rect = self.image.get_rect(center=(x, y))

	# def update():
