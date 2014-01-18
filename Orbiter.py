from Vector import *
import pygame

class Orbiter(pygame.sprite.Sprite):
	def __init__(self,position, velocity,gravity):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.velocity = velocity
		self.gravity = gravity #Strength of the gravitation attraction
		self.angularMomentum = position.cross(velocity)
		self.LRL = velocity.cross(self.angularMomentum) - gravity * position / position.abs()
		self.rotation = velocity.arg()
	def physicsUpdate(dv = 0, dt = .1):
		pass
	def getRadius(th):
		return self.angularMomentum.abs2()/(self.gravity()+self.LRL.abs()*cos(th))
		
