"""Server class"""
import socket

class Server():
    """Runs the Server"""
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(False)
        self.s.bind((HOST, PORT))
        self.s.listen(1)
        print "Listening"

        self.users = {}

    ############################# RECIEVE ##################################
    def recieve(self):
        """Recieves connections from new users and data from others"""
        self.getNewConnections()
        for user in self.users:
            data = self.getData(user)
            if (data != ""):
                self.send(data)
            self.parse(data)

    def getNewConnections(self):
        """Checks for new users and connects with them"""
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
        except socket.error:
            pass

    def getData(self, user):
        """Recieves data from current users"""
        try:
            data = self.users[user].recv() ####FIX#####
        except socket.error:
            data = ""
            pass
        return data

    ########################### SEND #######################################
    def send(self, data):
        """Sends data to all users"""
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

    def sendRemove(self):
        pass

    def close(self):
        """Closes all connection"""
        for user in self.users:
            self.users[user].close()
        self.s.close()

    ######################### PARSE ########################################
    def parse(self, data):
        """Parses incoming data and puts it in a readable format"""
        data = data.split(",")
        allCommands = []
        for command in data:
            commands = {}
            commands["type"] = command[0]
            if (command[0] == "S"):
                commands["x"] = command[1:5]
                commands["y"] = command[5:9]
                commands["burning"] = command[9]
                commands["rotation"] = command[10:13]
            elif (command[0] == "L"):
                commands["name"] = command[1:11]
                commands["x"] = command[11:15]
                commands["y"] = command[15:19]
                commands["burning"] = command[19]
                commands["rotation"] = command[20:23]
            elif (command[0] == "E"):
                commands["x"] = command[1:5]
                commands["y"] = command[5:9]
            else:
                commands["name"] = command[1:11]
            allCommands.append(commands)
        return allCommands
