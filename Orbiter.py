from Vector import *
import pygame

class Orbiter(pygame.sprite.Sprite):
	def __init__(self,position, velocity,gravity):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.velocity = velocity
		self.gravity = gravity #Strength of the gravitation attraction
		self.angularMomentum = position.cross(velocity)
		self.LRL = velocity.coCross(self.angularMomentum) - gravity * position / position.abs()
		self.rotation = velocity.arg()
	def physicsUpdate(self,dv = 0, dt = .1):
		pass
	def getRadius(self,th):
		return (self.angularMomentum**2)/(self.gravity+self.LRL.abs()*cos(th))
		
