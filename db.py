import socket
from commandHandlers import *


HOST = 'localhost'
PORT = 6969
store = {}

# create the socket
try:
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket creation succesfully")
except:
    print("There was an error creating the socket")


COMMAND_HANDLERS = {
    'PUT': handlePut,
    'GET': handleGet,
    'DELETE': handleDelete,
    'GETLIST': handleGetList,
    'PUTLIST': handlePutList,
    "ERROR": handleError
}


def parseRequest(req):
    # check for number of args
    if(len(req.split(":")) < 3):
        return ("ERROR", 2, "")
    command, key, value = req.split(":")
    # check if the command exists
    if command not in COMMAND_HANDLERS:
            return ("ERROR", 1, "")
    # check for list of values
    if(len(value.split(",")) > 1):
        value = value.split(",")
    return (command, key,  value)


def main():
    SOCKET.bind((HOST, PORT))
    SOCKET.listen(1)  # number of  concurrent connections not been accepted
    while True:
        connection, address = SOCKET.accept()
        print("New connectionf from", address)
        connection.send(
            "Connected\nEnter CLOSE to terminalte the connection\nFormat for querying TYPE:<key>:value \nleave the field blank if not applicable, separate the values by comma in case of list\n".encode())
        request = connection.recv(4096).decode()
        command, key, value = parseRequest(request)

        if command in(
            'GET',
            'GETLIST'
        ):
            response = COMMAND_HANDLERS[command](key)
        elif command in(
            'PUT',
            'PUTLIST'
        ):
            response = COMMAND_HANDLERS[command](key, value)
        else:
            response = COMMAND_HANDLERS["ERROR"](key)
        connection.send(response.encode())
        connection.close()

if __name__ == '__main__':
    main()
