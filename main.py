import Vector, Orbitor, Ship, Missile, Asteroid
import pygame
import os, sys

ROTSPEED = 3.0
THRUST = 1.0
CENTER = (350, 350)
G = 5.0
# startV


pygame.init()
screen = pygame.display.set_mode(700, 700))
pygame.display.set_caption("SpaceGame")


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

gameClock = pygame.time.clock()


player = Ship(center, ROTSPEED, THRUST)

#other ships
#missiles

pressed = []
mouseLoc = (0,0)
mouseDown = False

frame = 0

# wait till all clients are conneted?

while True:

	#get keyboard events
	for event in pygame.event.get:
		if event = pygame.QUIT:
			break

		elif event == pygame.KEYDOWN:
			pressed.append(event.key)

		elif event == pygame.KEYUP:
			pressed.remove(event.key)


		elif event == pygame.MOUSEBUTTONDOWN:
			mouseDown = True

		elif event == pygame.MOUSEBUTTONUP:
			mouseDown = False

	mouseLoc = pygame.mouse.get_pos()

	#do physics

	# update sprites


	frame += 1
	gameClock.tick(60)
	
pygame.quit()
sys.exit()