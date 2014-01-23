# import Vector, Orbiter, Ship, Missile, Asteroid
from Vector import *
from Orbiter import *
from MyShip import *
from Planet import *
from Explosion import *
from plus import *
from Missile import *
from DumbMissile import *
from Connection import *
from Server import *
from NPCShip import *
from multiprocessing import Process, Pipe

import time
import pygame
import os, sys

ROTSPEED = 3.0
THRUST = 0.1
CENTER = (500, 500)
G = 50000
TRIGGER = 30


###############
#networking constants

def namePick(ip,port,name, client, childPipe):
	print "hi"
	a = client.pickName(ip,port,name)
	print a
	childPipe.send(a)
	conn.close()


# rep = raw_input("server? [Y, N]")
# if rep =="y":
# 	serve = Server(9000)
try:
	client = Connection()
	name = raw_input("Name? [10 Character]")
	while len(name) < 10:
		name = name + " "
	ip = raw_input("What Ip?")

	# if rep =="y": 
	# 	parent, child = Pipe()
	# 	t = Process(target=namePick, name="SecondThread", args=(ip, 9000, name, client, child))

	# 	t.start()
	# 	time.sleep(2)
	# 	print serve.recieve()
	# 	t.join(timeout=3)
	# 	flag = parent.recv()
	# else:
	flag = client.pickName(ip,9000,name)

	while not flag:
		name = raw_input("Other Name? [10 Character]")

		while len(name) < 10:
			name = name + " "
		# if rep == "y":
		# 	parent, child = Pipe()
		# 	t = Process(target=namePick, name="SecondThread", args=(ip, port, name, client, child))

		# 	t.start()
		# 	time.sleep(2)
		# 	serve.recieve()
		# 	t.join(timeout=3)
		# 	flag = parent.recv()
		# else:
		flag = client.pickName(ip,9000,name)

	print client.name

except:
	client.close()
	sys.exit()

###############
# startV


def hitBy(p, missiles, triggerRange):
	inRange = []
	out = []
	for sp in missiles.sprites():
		if sp.inside(p):
			inRange.append(sp)

	if not len(inRange):
		return False

	for sp in inRange:
		missiles.remove(sp)
		out.append(sp.rect.center)
	return out





pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("SpaceGame")


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# print "black?"

gameClock = pygame.time.Clock()


player = MyShip(CENTER, ROTSPEED, THRUST, G, 40)
pl = Planet(CENTER[0], CENTER[1])

playerGroup = pygame.sprite.RenderPlain(player, pl)
myMissiles = pygame.sprite.RenderPlain()
explosions = pygame.sprite.RenderPlain()
otherMissiles = pygame.sprite.RenderPlain()
npcs = pygame.sprite.RenderPlain()

newExplo = []
# centerGroup = pygame.sprite.RenderPlain((planet))
# playerGroup.add(pl)

# NPC = {}

pressed = []
mouseLoc = (0,0)
mouseDown = False

frame = 0

# wait till all clients are conneted?

while True:

	otherMissiles.empty()
	npcs.empty()

	data = client.recieve()

	if not data:
		data = []

	for event in data:
		if event["type"] == "L":
			npcs.add(NPCShip(event['name'], event['x'], event['y'], event['rotation'], event['burning']))
			# name = event["name"]
			# print NPC
			# if name in NPC.keys():
			# 	NPC[name] = NPC[name].changeValues(event['x'], event['y'], event['rotation'], event['burning'])

			# else:
			# 	NPC[name] = NPCShip(name, event['x'], event['y'], event['rotation'], event['burning'])



		# if event["type"] == "R":
		# 	if event["name"] in NPC.keys():
		# 		NPC.pop(event["name"])


		if event["type"] == "S":
			otherMissiles.add(DumbMissile(int(event['x']), int(event['y']), int(event['rotation']), event['burning']))
			#create a dumb missile, check  for collisions later

		if event["type"] == "E":
			explosions.add(Explosion((event['x'], event['y']),client , createNew=False))

	# npcs.empty()
	# for k in NPC.keys():
	# 	npcs.add(NPC[k])



	#get keyboard events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		
			pygame.quit()

			# if rep =="y":
			# 	serve.close()

			client.close()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			pressed.append(event.key)

		elif event.type == pygame.KEYUP:
			try:
				pressed.remove(event.key)
			except:
				pass

			try:
				pressed.remove(event.key)
			except:
				pass


		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouseDown = True

		elif event.type == pygame.MOUSEBUTTONUP:
			mouseDown = False

	mouseLoc = pygame.mouse.get_pos()


	playerGroup.update(pressed, mouseLoc, mouseDown)

	# checking for missile explodes

	hits = hitBy(player.p, myMissiles, TRIGGER)		###deals with this player's missiles hitting player

	if hits:
		for p in hits:
			explosions.add(Explosion(p, client))
			client.sendRemove()

	
	hits = hitBy(player.p, otherMissiles, TRIGGER)	###deals with missiles of other players
	if hits:
		for p in hits:
			explosions.add(Explosion(p, client))
			client.sendRemove()
				

	exploded = False
	for expl in explosions.sprites():
		hits = hitBy(expl.p, myMissiles, TRIGGER)
		if expl.inside(player.p) and not exploded:
			exploded = True
			explosions.add(Explosion(player.p, client))
			player.rect.center = (-20, -20)
			try:
				playerGroup.remove(player)
			except:
				pass

		if hits:
			for p in hits:
				explosions.add(Explosion(p, client))

	if exploded:
		player.explode = True
		client.sendRemove()

	
	if player.new:
		m = player.out
		myMissiles.add(m)

	if player.explode:
		player.explode = False
		client.sendRemove()
		explosions.add(Explosion(player.p, client))

	for sp in myMissiles:

		if sp.explode:
			newExplo.append(sp)

	for sp in newExplo:
		myMissiles.remove(sp)
		e = Explosion(sp.p, client)
		explosions.add(e)

	newExplo = []

	myMissiles.update(client)
	explosions.update()


	screen.blit(background, (0, 0))
	explosions.draw(screen)
	playerGroup.draw(screen)
	myMissiles.draw(screen)
	npcs.draw(screen)
	otherMissiles.draw(screen)

	
	#drawing usefull stuff
	drawPlus(screen, CENTER[0]+player.getApoapsis().x, CENTER[1]+player.getApoapsis().y, (255,255,0))
        drawPlus(screen, CENTER[0]+player.getPeriapsis().x, CENTER[1]+player.getPeriapsis().y, (0,255,255))


	pygame.display.flip()


	
	x, y = player.rect.center
	client.sendLocation(int(x),int(y), True, int(math.degrees(player.rotation))%360)


	
	# if rep == "y":
	# 	serve.recieve()
	gameClock.tick(60)

	
except:
	client.close()
	pygame.quit()
	sys.exit()
	
