import pygame, sys

from MultiCenterOrbiter import *

pygame.init()
black = 0, 0, 0
white = 255,255,255
red = 255,255,0
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((600, 600))
bg = pygame.Surface(window.get_size())
bg = bg.convert()
bg.fill(black)

window.blit(bg, (0, 0))
pygame.display.flip()

ship = MultiCenterOrbiter(Vector(10,0), Vector(0,10), [Vector(-100,0), Vector(100,0)], [10000,10000])

window.set_at((200,300),red)

window.set_at((400,300),red)

while True:
	window.set_at((int(300+ship.position.x), int(300+ship.position.y)), white)
	ship.physicsUpdate()
	pygame.display.flip()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()



