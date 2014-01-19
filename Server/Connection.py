# Connection Class
import socket
from Conversion import *

class Connection():
    """Makes connections for multiplayer"""
    def __init__(self):
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def pickName(self, HOST, PORT, name):
        """Get registered as a user in the server"""
        self.c.connect((HOST, PORT))
        self.c.sendall(name)
        if (self.c.recv(1) == "Y"):
            self.c.setblocking(False)
            return True
        else:
            self.c.close()
            return False

    ##################################### RECIEVE ##########################
    def recieve(self):
        try:
            data = self.c.recv(2048)
            data = parse(data)
            return data
        except socket.error:
            pass

    ##################################### SEND #############################
    def send(self, message):
        #message = self.convertMessage(message)
        try:
            self.c.sendall(message)
        except socket.error:
            pass

    def sendMissile(self, x, y, b, r):
        t = encode([{"type":"S", "x":x, "y":y, "burning":b, "rotation":r}])
        self.send(t)

    def sendLocation(self, n, x, y, b, r):
        t=encode([{"type":"L","name":n,"x":x,"y":y,"burning":b,"rotation":r}])
        self.send(t)

    def sendExplode(self, x, y):
        t = encode([{"type":"E", "x":x, "y":y}])
        self.send(t)

    def sendRemove(self, n):
        t = encode([{"type":"R", "name":n}])
        self.send(t)

    ################################### EXIT ###############################
    def close(self):
        self.c.close()
