import json, yaml
from gendiff.gendiff import generate_diff, izmen
from gendiff.format import stringify

json1 = json.load(open('tests/fixtures/file1.json'))
json2 = json.load(open('tests/fixtures/file2.json'))
yml1 = yaml.safe_load(open('tests/fixtures/file1.yml'))
yml2 = yaml.safe_load(open('tests/fixtures/file2.yml'))
rec1 = json.load(open('tests/fixtures/file1rec.json'))
rec2 = json.load(open('tests/fixtures/file2rec.json'))
expected = open("tests/fixtures/expected.txt", "r")
expectedyml = open("tests/fixtures/expectedyml.txt", "r")
expectedrec = open("tests/fixtures/expectedrec.txt", "r")


def test_generate_diff_json():
    assert generate_diff(json1, json2) == expected.read()


def test_generate_diff_yml():
    assert generate_diff(yml1, yml2) == expectedyml.read()


def test_generate_diff_yml():
    znak = izmen(rec1, rec2, [])
    assert stringify(rec1, rec2, znak) == expectedrec.read()
