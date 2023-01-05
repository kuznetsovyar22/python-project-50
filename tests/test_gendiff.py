import json
from .gendiff.scripts.main import generate_diff

file1 = json.load(open('./fixtures/file1.json'))
file2 = json.load(open('./fixtures/file2.json'))
expected = open("./fixtures/expected.txt", "r")

def test_generate_diff():
    assert generate_diff(file1, file2) == expected