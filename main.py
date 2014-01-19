# import Vector, Orbiter, Ship, Missile, Asteroid
from Vector import *
from Orbiter import *
from MyShip import *
# from Asteroid import *
# from Missile import *
import pygame
import os, sys

ROTSPEED = 3.0
THRUST = 1.0
CENTER = (350, 350)
G = 50000
# startV


pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("SpaceGame")


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# print "black?"

gameClock = pygame.time.Clock()


player = MyShip(CENTER, ROTSPEED, THRUST, G)

playerGroup = pygame.sprite.RenderPlain((player))

#other ships
#missiles

pressed = []
mouseLoc = (0,0)
mouseDown = False

frame = 0

# wait till all clients are conneted?

while True:

	#get keyboard events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		
			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			pressed.append(event.key)

		elif event.type == pygame.KEYUP:
			pressed.remove(event.key)


		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouseDown = True

		elif event.type == pygame.MOUSEBUTTONUP:
			mouseDown = False

	mouseLoc = pygame.mouse.get_pos()

	# print "got input"

	#do physics

	# update sprites

	playerGroup.update(pressed, mouseLoc, mouseDown)

	screen.blit(background, (0, 0))
	playerGroup.draw(screen)
	pygame.display.flip()


	# frame += 1
	gameClock.tick(6)
	
