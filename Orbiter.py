from Vector import *
import pygame

class Orbiter(pygame.sprite.Sprite):
	def __init__(self,position, velocity,gravity):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.velocity = velocity
		self.gravity = gravity #Strength of the gravitation attraction
		self.rotation = velocity.arg()
		self.computeLRL()
	
	def computeLRL(self):
		self.angularMomentum = self.position.cross(self.velocity)
		self.LRL = self.velocity.coCross(self.angularMomentum) - self.gravity * self.position / self.position.abs()
		

	def physicsUpdate(self,dv = 0, dt = .1):
		self.velocity += dv
		self.computeLRL()
		th = self.position.arg() + dt * self.angularMomentum / self.position.abs()
		self.position.setP(self.getRadius(th),th)
		
	def getRadius(self,th):
		return (self.angularMomentum**2)/(self.gravity+self.LRL.abs()*cos(th-self.LRL.arg()))
		
