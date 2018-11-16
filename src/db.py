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
    command = command.upper()
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
        print("New connectionf from ", address)
        connection.send(
            "Connected\nEnter CLOSE to terminalte the connection\nFormat for querying <TYPE>:<key>:<value> \nleave the field blank if not applicable, separate the values by comma in case of list\n".encode())
        try:
            request = connection.recv(4096).decode()
            # uncomment this line if not using the terminal
            # \n is getting appended when using netcat in the terminal
            request = request[:-1]
        except:
            print("connection lost or closing connection due to unhandled error")
            connection.close()
            continue
       
        while(request != "CLOSE"):
            command, key, value = parseRequest(request)
            if command in(
                'GET',
                'GETLIST',
                'DELETE'
            ):
                response = COMMAND_HANDLERS[command](key)
            elif command in(
                'PUT',
                'PUTLIST'
            ):
                response = COMMAND_HANDLERS[command](key, value)
            else:
                response = COMMAND_HANDLERS["ERROR"](key)
            try:
                connection.send(response.encode())
            except:
                print("connection lost or closing connection due to unhandled error")
                connection.close()
                break
            try:
                request = connection.recv(4096).decode()
                # uncomment this line if not using the terminal
                # \n is getting appended when using netcat in the terminal
                request = request[:-1]
            except:
                print("connection lost or closing connection due to unhandled error")
                connection.close()
                break


if __name__ == '__main__':
    main()
