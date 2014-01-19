import pygame, math
from Orbiter import *
from Vector import *

IMG = pygame.image.load("images/missile.png")

class DumbMissile(pygame.sprite.Sprite):
	def __init__(self, x, y, rot, fire):
		pygame.sprite.Sprite.__init__(self)

		self.trigger = 30

		self.explode = False

		self.adjust = 90		

		self.rotation =  rot

		self.armed = fire

		self.p = (x, y)

		self.image = IMG
		self.image = pygame.transform.scale(self.image, (20, 40))
		self.image = pygame.transform.rotate(self.image, self.rotation + self.adjust)
		self.rect = self.image.get_rect(center=self.p)

	def inside(self, pos):
		return (Vector(pos[0], pos[1]) - Vector(self.p[0], self.p[1])).abs() < self.trigger and self.armed

