import pygame
from Orbiter import *
import math

IMGS = pygame.image.load("images/redShip.png")

class NPCShip(pygame.sprite.Sprite):
	def __init__(self, name, x, y, rot, fire):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		self.image = IMGS
		self.image = pygame.transform.scale(self.image, (20, 45))
		self.original = self.image
		self.changeValues(x, y, rot, fire)
		

	def changeValues(self, x, y, rot, fire):
		self.x = x
		self.y = y
		self.rot = rot
		self.image = pygame.transform.rotate(self.original, rot+90)
		self.rect = self.image.get_rect(center=(x, y))

	# def update():
