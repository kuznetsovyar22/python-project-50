import yaml
import json


def parse_file(file):
    ext = file.split('.')
    if ext[1] == 'json':
        return json.load(open(file))
    elif ext[1] == 'yml' or ext[1] == 'yaml':
        return yaml.safe_load(open(file))
