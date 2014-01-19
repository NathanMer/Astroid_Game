import pygame

from Vector import *

class MultiCenterOrbiter(pygame.sprite.Sprite):
	def __init__(position, velocity, centerLocations, centerGravities):
		self.position = position
		self.velocity = velocity
		self.centerLocations = centerLocations
		self.centerGravities = centerGravities

	def physicsUpdate(dv = 0, dt = .001):
		for i in range(len(self.centerLocations)):
			r = centerLocations[i] - position
			dv += r/r.abs() * centerGravities[i]/r.abs2() * dt
		self.velocity += dv
		self.position += self.velocity * dt
