import socket
from commandHandlers import *
HOST = 'localhost'
PORT = 6968

# create the socket
try:
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket creation succesfully")
except:
    print("There was an error creating the socket")

COMMAN_HANDLERS = {
    'PUT': handlePut,
    'GET': handlGet,
    'DELETE': handleDelete,
    'GETLIST': handleGetList,
    'PUTLIST': handlePutList
}

def main():
    SOCKET.bind((HOST, PORT))
    SOCKET.listen(1) #number of  concurrent connections not been accepted 
    while True:
        connection, address = SOCKET.accept()
        print("New connectionf from", address)
        connection.send("Connected".encode())
if __name__ == '__main__':
    main()