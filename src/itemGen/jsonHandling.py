import json

def impJSON(path):
    file = open(path, "r")
    fileString = file.read()
    file.close()
    jsonObj = json.loads(fileString)
    return jsonObj