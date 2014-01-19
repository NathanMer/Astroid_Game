def drawPlus(screen,x,y,color,size = 3):
	x,y = int(x),int(y)
	for X in range(x-size, x+size+1):
		screen.set_at((X,y),color)
	for Y in range(y-size, y+size+1):
		screen.set_at((x,Y),color)
