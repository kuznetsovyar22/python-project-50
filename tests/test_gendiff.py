import json, yaml
from gendiff.gendiff import izmen
from gendiff.formatters.stylish import formatter_stylish
from gendiff.formatters.plain import formatter_plain


json1 = json.load(open('tests/fixtures/file1.json'))
json2 = json.load(open('tests/fixtures/file2.json'))
yml1 = yaml.safe_load(open('tests/fixtures/file1.yml'))
yml2 = yaml.safe_load(open('tests/fixtures/file2.yml'))
rec1 = json.load(open('tests/fixtures/file1rec.json'))
rec2 = json.load(open('tests/fixtures/file2rec.json'))
expected = open("tests/fixtures/expected.txt", "r")
expectedyml = open("tests/fixtures/expectedyml.txt", "r")
expectedrec = open("tests/fixtures/expectedrec.txt", "r")
expectedplain = open("tests/fixtures/expectedplain.txt", "r")


def test_generate_diff_json():
    znak = izmen(json1, json2, [])
    assert formatter_stylish(json1, json2, znak) == expected.read()


def test_generate_diff_yml():
    znak = izmen(yml1, yml2, [])
    assert formatter_stylish(yml1, yml2, znak) == expectedyml.read()


def test_generate_diff_rec():
    znak = izmen(rec1, rec2, [])
    assert formatter_stylish(rec1, rec2, znak) == expectedrec.read()


def test_generate_diff_plain():
    znak = izmen(rec1, rec2, [])
    assert formatter_plain(rec1, rec2, znak, []) == expectedplain.read()
