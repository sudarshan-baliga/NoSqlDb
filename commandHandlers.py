import json
import pickle
import os

STORE_DIR = './store.pkl'

# load or create the data base file
if os.path.exists(STORE_DIR):
    with open(STORE_DIR, 'rb') as file:
        store = pickle.load(file)
    print(store)
else:
    print("store.pkl  file not found \ncreating store.pkl")
    file = open(STORE_DIR, 'w')
    file.close()
    store = {}

def handlePut(key, value):
    """Inserting single value into key
    and return JSON object containing status and the message back to client"""
    store[key] = value
    with open(STORE_DIR, 'wb') as dbFile:
        pickle.dump(store, dbFile)
    return json.dumps({"status": "success", "message":"inserted succesfully"})


def handleGet(key):
    """Returns JSON object containing status and value, if value exists
    or false to the client"""
    if key not in store:
        return json.dumps({"status": "failure", "message":"key not found"})
    else:
        return json.dumps({"status": "sucess", "message":"key found", key: store[key]})


def handleDelete(key):
    """Returns JSON object containing status if value exists and 
    deleted or false along with the message"""
    pass


def handleGetList(key):
    """ReturnsJSON object containing status and list of elements if key exists 
    along with the message"""
    pass

def handlePutList(key, value):
    """ReturnsJSON object containing status if list is inserted succesfully to the 
    key and also returns the message"""
    pass


def handleError(errCode):
    "Return json object containing status and error message"
    if errCode == 1:
        msg = "Command not found"
    elif errCode == 2:
        msg = "not enough args"
    return json.dumps({"status": "failure", "message": msg})
