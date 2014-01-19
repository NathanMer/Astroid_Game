import pygame, math

class Explosion(pygame.sprite.Sprite):
	def __init__(self, p):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/missileExplosion.png")
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect(center=p)
		self.counter = 30

	def update(self):
		self.counter -= 1
		if self.counter <= 1:
			self.kill()