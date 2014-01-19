import pygame

class Planet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/moon.png")
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect(center=(x, y))
		self.counter = 0

	def update(self, pressed, mouseLoc, mouseDown):
		self.counter += 1