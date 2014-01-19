# Connection Class
import socket

class Connection():
    """Makes connections for multiplayer"""
    def __init__(self):
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def pickName(self, HOST, PORT, name):
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
        self.recieveFromServer()
        self.recieveFromUsers()


    ##################################### SEND #############################
    def send(self, message):
        message = self.convertMessage(message)
        try:
            self.c.sendall(message)
            for user in self.users:
                self.users[user].sendall(message)
        except socket.error:
            pass
