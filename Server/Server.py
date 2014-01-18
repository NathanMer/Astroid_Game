"""Server class"""
import socket

class Server():
    """Runs the Server"""
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(False)
        self.s.bind((HOST, PORT))
        self.s.listen(1)
        print "Listening on %s" % ("%s:&s" % self.s.getsockname())

        self.users = {}

    def recieve(self):
        self.getNewConnections()
        for user in users:
            data = self.getData(user)
            self.parse(data)
    
    def getNewConnections(self):
        try:
            conn, addr = self.s.accept()
            newName = conn.recv() ########### fix #########
