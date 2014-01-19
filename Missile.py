import pygame, math
from Orbiter import *
from Vector import *

class Missile(Orbiter):
	def __init__(self, pos, rot, burn, Vi, g, center, surface):
		Orbiter.__init__(self, Vector(pos.x, pos.y), Vector(Vi.x, Vi.y), g)
		self.thrust = 1
		self.explode = False

		self.surface = surface


		self.adjust = 90		



		self.center = center
		self.rotation =  rot

		self.burnTime = burn
		self.fuse = 40
		self.image = pygame.image.load("images/missile.png")
		self.image = pygame.transform.scale(self.image, (20, 40))
		self.image = pygame.transform.rotate(self.image, math.degrees(self.rotation) + self.adjust)
		self.rect = self.image.get_rect()
		# self.original = self.image
				

	def update(self):

		if self.fuse <1:
			self.explode = (self.getAltitude() <= self.surface)
			self.p = (self.center[0] + self.position.x, self.center[1] + self.position.y)



		else:
			self.fuse -= 1


		if self.burnTime > 0:
			self.burnTime -= 1
			self.physicsUpdate(createPolar(self.thrust, self.rotation))


		else:
			self.physicsUpdate(createPolar(0, self.rotation))


		try:
			self.rect.center = (self.center[0] + self.position.x, self.center[1] + self.position.y)
		except TypeError:
			self.kill()






		



