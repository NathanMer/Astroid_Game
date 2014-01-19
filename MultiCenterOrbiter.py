import pygame

from Vector import *

class MultiCenterOrbiter(pygame.sprite.Sprite):
	def __init__(self,position, velocity, centerLocations, centerGravities):
		self.position = position
		self.velocity = velocity
		self.centerLocations = centerLocations
		self.centerGravities = centerGravities

	def physicsUpdate(self,dv = Vector(0,0), dt = .01):
		for i in range(len(self.centerLocations)):
			r = self.centerLocations[i] - self.position
			dv += r/r.abs() * self.centerGravities[i]/r.abs2() * dt
		self.velocity += dv
		self.position += self.velocity * dt
