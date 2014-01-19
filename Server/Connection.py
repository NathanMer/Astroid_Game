# Connection Class
import socket

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
        #self.recieveFromServer()
        #self.recieveFromUsers()
        pass


    ##################################### SEND #############################
    def send(self, message):
        #message = self.convertMessage(message)
        try:
            self.c.sendall(message)
        except socket.error:
            pass
