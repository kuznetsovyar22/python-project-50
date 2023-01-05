import json
from scripts.main import generate_diff

file1 = json.load(open('file1.json'))
file2 = json.load(open('file2.json'))
print(generate_diff(file1, file2))