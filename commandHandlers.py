import json


def handlePut(key, value):
    """Inserting single value into key
    and return JSON object containing status and the message back to client"""
    return json.dumps({key: value})


def handleGet(key):
    """Returns JSON object containing status and value, if value exists
    or false to the client"""
    pass


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
