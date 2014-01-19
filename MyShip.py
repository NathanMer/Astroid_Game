import pygame, math
from Vector import *
from Orbiter import *


RAD = 0.017453292519943295

class MyShip(Orbiter):
	def __init__(self, center, rotSpeed, thrust, g):
		Orbiter.__init__(self, Vector(100, 0), Vector(0, -20), g)

		self.timer = None
		self.down = False
		self.rotSpeed = rotSpeed
		self.image = pygame.image.load("images/blueShip.png")
		self.image = pygame.transform.scale(self.image, (20, 45))
		self.image = pygame.transform.rotate(self.image, 90)
		self.original = self.image
		self.rect = self.image.get_rect()
		self.thrust = thrust
		self.center = center
		self.lastRot = self.rotation


	def updateRotation(self, pressed):

		if pygame.K_a in pressed:
			self.rotation += RAD * self.rotSpeed

		elif pygame.K_d in pressed:
			self.rotation -= RAD * self.rotSpeed

		c = self.rect.center
		self.image = pygame.transform.rotate(self.original, math.degrees(self.rotation))
		# self.lastRot = self.rotation
		self.rect = self.image.get_rect(center=c)
	


	def update(self, pressed, mouseLoc, mouseDown):
		

		self.physicsUpdate(createPolar(self.thrust * (pygame.K_w in pressed), self.rotation))

		self.rect.center = (self.center[0] + self.position.x, self.center[1] + self.position.y)

		self.updateRotation(pressed)


		if mouseDown and self.down:
			self.timer-=1

		elif mouseDown and not self.down:
			self.down = True
			self.timer = 120

		elif not mouseDown and self.down:
			print "missile fired", self.timer
			self.down = False

			self.image = pygame.transform.scale(self.original, (abs(self.timer), abs(self.timer)))
			self.rect = self.image.get_rect()





		
		
