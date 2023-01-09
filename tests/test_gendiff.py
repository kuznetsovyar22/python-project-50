import json, yaml
from gendiff.gendiff import generate_diff


expected = open("tests/fixtures/expected.txt", "r")
expectedyml = open("tests/fixtures/expectedyml.txt", "r")
expectedrec = open("tests/fixtures/expectedrec.txt", "r")
expectedplain = open("tests/fixtures/expectedplain.txt", "r")
generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')

def test_generate_diff_json():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected.read()


def test_generate_diff_yml():
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == expectedyml.read()


def test_generate_diff_rec():
    assert generate_diff('tests/fixtures/file1rec.json', 'tests/fixtures/file2rec.json') == expectedrec.read()


def test_generate_diff_plain():
    assert generate_diff('tests/fixtures/file1rec.json', 'tests/fixtures/file2rec.json', format='plain') == expectedplain.read()
