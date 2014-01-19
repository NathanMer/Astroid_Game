"""Server class"""
import socket

class Server():
    """Runs the Server"""
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(False)
        self.s.bind((HOST, PORT))
        self.s.listen(1)
        print "Listening on %s" % ("%s:&s" % self.s.getsockname())

        self.users = {}

    ############################# RECIEVE ##################################
    def recieve(self):
        self.getNewConnections()
        for user in self.users:
            data = self.getData(user)
            self.parse(data)
    
    def getNewConnections(self):
        try:
            conn, addr = self.s.accept()
            newName = conn.recv(10)
            for user in self.users:
                if (newName == user):
                    conn.sendall("N")
                    conn.close()
                    conn = "Er"
            if (conn != "Er"):
                conn.sendall("Y")
                
                conn.setblocking(False)

                self.users[newName] = conn

                self.sendUsers()
        except socket.error:
            pass

    def getData(self, user):
        try:
            data = self.users[user].recv() ####FIX#####
        except socket.error:
            pass
        return data
    
    ########################### SEND #######################################
    def send(self, data):
        try:
            for user in self.users:
                self.users[user].sendall(data)
        except socket.error:
            pass

    def sendMissile(self):
        pass
    
    def sendLocation(self):
        pass

    def sendExplode(self):
        pass

    def sendMake(self):
        pass

    def sendRemove(self):
        pass

