import pygame, math
from Vector import *
 

class MyShip(Orbiter):
	def __init__(self, center, rotSpeed, thrust, g):
		orbiter.__init__(self, Vector(100, 100), Vector(10, 0), g)
		self.timer = None
		self.image = pygame.image.load("triangle.png")
		self.original = self.image
		self.rect = self.image.get_rect()
		self.thrust = thrust
		self.center

	


	def update(self, pressed, mouseLoc, mouseDown):

		if pygame.

		self.physicsUpdate()



		
		
