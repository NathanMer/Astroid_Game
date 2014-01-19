# import Vector, Orbiter, Ship, Missile, Asteroid
from Vector import *
from Orbiter import *
from MyShip import *
from Planet import *
from Explosion import *
from plus import *
# from Asteroid import *
from Missile import *
import pygame
import os, sys

ROTSPEED = 3.0
THRUST = 0.1
CENTER = (350, 350)
G = 50000
# startV


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("SpaceGame")


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# print "black?"

gameClock = pygame.time.Clock()


player = MyShip(CENTER, ROTSPEED, THRUST, G, 20)
pl = Planet(350, 350)

playerGroup = pygame.sprite.RenderPlain(player, pl)
myMissiles = pygame.sprite.RenderPlain()
explosions = pygame.sprite.RenderPlain()
# centerGroup = pygame.sprite.RenderPlain((planet))
# playerGroup.add(pl)

NPC = {}

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



	playerGroup.update(pressed, mouseLoc, mouseDown)
	
	if player.new:
		m = player.out
		myMissiles.add(m)

	if player.explode:
		player.explode = False
		explosions.add(Explosion(player.p))

	myMissiles.update()
	explosions.update()


	screen.blit(background, (0, 0))
	explosions.draw(screen)
	playerGroup.draw(screen)
	myMissiles.draw(screen)

	
	#drawing usefull stuff
	drawPlus(screen, CENTER[0]+player.getApoapsis().x, CENTER[1]+player.getApoapsis().y, (255,255,0))
        drawPlus(screen, CENTER[0]+player.getPeriapsis().x, CENTER[1]+player.getPeriapsis().y, (0,255,255))


	pygame.display.flip()


	frame += 1
	if not (frame%3):
		#send networking stuff
		pass

	# do networking stuff
	gameClock.tick(60)
	
