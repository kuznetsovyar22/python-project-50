import json
from gendiff.gendiff import generate_diff

file1 = json.load(open('tests/fixtures/file1.json'))
file2 = json.load(open('tests/fixtures/file2.json'))
expected = open("tests/fixtures/expected.txt", "r")

def test_generate_diff():
    assert generate_diff(file1, file2) == expected.read()