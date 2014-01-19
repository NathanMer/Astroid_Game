import pygame, Orbiter, Vector, sys

from math import *

pygame.init()
black = 0, 0, 0
white = 255,255,255
red = 255,255,0
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((400, 400))
bg = pygame.Surface(window.get_size())
bg = bg.convert()
bg.fill(black)

window.blit(bg, (0, 0))
pygame.display.flip()

window.set_at((200,200),white)

ship = Orbiter.Orbiter(Vector.Vector(100,0), Vector.Vector(0, 20), 50000)

print ship.LRL.abs(), ship.LRL.arg()

tVect = Vector.Vector(0,0)

for i in range(0,20):
	th = i * pi / 10
	r = ship.getRadius(th)
	tVect.setP(r,th)
	print r
	window.set_at((int(200+tVect.x),int(200+tVect.y)),red)

pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
