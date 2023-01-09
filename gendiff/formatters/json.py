import json


def formatter_json(znak, replacer=' ', spacesCount=1):
    to_json = json.dumps(znak)
    return to_json
