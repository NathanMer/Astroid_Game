import pygame, math
from Orbiter import *
from Vector import *

MISS = pygame.image.load("images/missile.png")

class Missile(Orbiter):
	def __init__(self, pos, rot, burn, Vi, g, center, surface):
		Orbiter.__init__(self, Vector(pos.x, pos.y), Vector(Vi.x, Vi.y), g)
		self.thrust = 0.5
		self.explode = False

		self.surface = surface


		self.adjust = 90		

		self.center = center
		self.rotation =  rot

		self.trigger = 20

		self.burnTime = burn
		self.p = (self.center[0] + self.position.x, self.center[1] + self.position.y)
		self.fuse = 40
		self.image = MISS
		self.image = pygame.transform.scale(self.image, (5, 10))
		self.image = pygame.transform.rotate(self.image, math.degrees(self.rotation) + self.adjust)
		self.rect = self.image.get_rect()
		# self.original = self.image

	def inside(self, pos):
		return (Vector(pos[0], pos[1]) - Vector(self.p[0], self.p[1])).abs() < self.trigger and self.fuse<1
				

	def update(self, client):

		if self.fuse <1:
			self.explode = (self.getAltitude() <= self.surface)
			self.p = (self.center[0] + self.position.x, self.center[1] + self.position.y)

		else:
			self.fuse -= 1

		if self.burnTime > 0:
			self.burnTime -= 1
			try:
				self.physicsUpdate(createPolar(self.thrust, self.rotation))
			except:
				self.explode = True

		else:
			try:
				self.physicsUpdate(createPolar(0, self.rotation))
			except:
				self.explode = True


		try:
			self.rect.center = (self.center[0] + self.position.x, self.center[1] + self.position.y)
		except TypeError:
			self.kill()

		self.p = (self.center[0] + self.position.x, self.center[1] + self.position.y)
		if int(self.p[0]) >0 and int(self.p[1]) >0 and int(self.p[0]) < 1000 and int(self.p[1]) < 1000 :
			client.sendMissile(int(self.p[0]), int(self.p[1]), (self.fuse<1), int(math.degrees(self.rotation))%360)






		



