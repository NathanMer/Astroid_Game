import pygame, math
from Vector import *

IMGX = pygame.image.load("images/missileExplosion.png")

class Explosion(pygame.sprite.Sprite):
	def __init__(self, p, client, createNew=True):
		pygame.sprite.Sprite.__init__(self)
		self.image = IMGX
		self.image = pygame.transform.scale(self.image, (60, 60))
		self.rect = self.image.get_rect(center=p)
		self.x, self.y = p
		self.p = p
		self.counter = 30
		if createNew:
			client.sendExplode(int(self.x), int(self.y))

	def inside(self, p):
		return (Vector(p[0], p[1]) - Vector(self.x, self.y)).abs() < 60

	def update(self):
		self.counter -= 1
		if self.counter <= 1:
			self.kill()