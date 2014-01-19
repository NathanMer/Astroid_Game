"""Converts the data for sending over a server"""

def parse(data):
    """Parses incoming data and puts it in a readable format"""
    data = data.split(",")
    allCommands = []
    for command in data:
        commands = {}
        commands["type"] = command[0]
        if (command[0] == "S"):
            commands["x"] = int(command[1:5])
            commands["y"] = int(command[5:9])
            commands["burning"] = bool(int(command[9]))
            commands["rotation"] = int(command[10:13])
        elif (command[0] == "L"):
            commands["name"] = command[1:11]
            commands["x"] = int(command[11:15])
            commands["y"] = int(command[15:19])
            commands["burning"] = bool(int(command[19]))
            commands["rotation"] = int(command[20:23])
        elif (command[0] == "E"):
            commands["x"] = int(command[1:5])
            commands["y"] = int(command[5:9])
        else:
            commands["name"] = command[1:11]
        allCommands.append(commands)
    return allCommands

def encode(allCommands):
    data = []
    for command in allCommands:
        if (command["type"] == "S"):
            data.append(str(command["type"]) + str(command["x"]).zfill(4) + str(command["y"]).zfill(4) + str(int(command["burning"])) + str(command["rotation"]).zfill(3))
        elif (command["type"] == "L"):
            data.append(str(command["type"]) + str(command["name"]) + str(command["x"]).zfill(4) + str(command["y"]).zfill(4) + str(int(command["burning"])) + str(command["rotation"]).zfill(3))
        elif (command["type"] == "E"):
            data.append(str(command["type"]) + str(command["x"]).zfill(4) + str(command["y"]).zfill(4))
        else:
            data.append(str(command["type"]) + str(command["name"]))

    data = ",".join(data)
    return data
