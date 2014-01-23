from Server import *
import sys

try:
	ser = Server(9000)

	while True:
	    ser.recieve()
except KeyboardInterrupt:
	ser.close()
	print "\nexited cleanly"
	sys.exit()