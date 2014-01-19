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
		self.sweptArea = self.position.abs2() * self.angularMomentum / self.position.abs()

	def physicsUpdate(self,dv = 0, dt = .001):
		dv.x = -dv.x #This is necessary. Don't ask why
		self.velocity = Vector(-(self.LRL + self.gravity*self.position/self.position.abs()).y/self.angularMomentum,
			(self.LRL + self.gravity*self.position/self.position.abs()).x/self.angularMomentum)
		self.velocity += dv
		self.computeLRL()
		th = self.position.arg() + dt * self.sweptArea / self.position.abs2()
		self.position.setP(self.getRadius(th),th)
		
	def getRadius(self,th):
		return (self.angularMomentum**2)/(self.gravity+self.LRL.abs()*cos(th-self.LRL.arg()))
		
	def getApoapsis(self):
		th = (-self.LRL).arg()
		return createPolar(self.getRadius(th), th)

	def getPeriapsis(self):
		th = self.LRL.arg()
		return createPolar(self.getRadius(th), th)

	def getAltitude(self):
		return self.position.abs()
