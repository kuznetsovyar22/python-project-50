from gendiff.formatters.stylish import formatter_stylish
from gendiff.formatters.plain import formatter_plain
from gendiff.formatters.json import formatter_json


def generate_diff(file1, file2, format):
    znak = izmen(file1, file2, [])
    if format == 'stylish':
        print(formatter_stylish(file1, file2, znak))
    elif format == 'plain':
        print(formatter_plain(file1, file2, znak, []))
    elif format == 'json':
        print(formatter_json(znak))


def izmen(file1, file2, znak):
    allkeys = sorted(list(file1.keys() | file2.keys()))
    for i in allkeys:
        if i in file1.keys() and i in file2.keys():
            obrab(file1, file2, i, znak)
        elif i not in file1.keys():
            znak.append({'key': i, 'znak': '+ '})
        elif i not in file2.keys():
            znak.append({'key': i, 'znak': '- '})
    return znak


def obrab(file1, file2, i, znak):
    if isinstance(file1[i], dict) and isinstance(file2[i], dict):
        znak.append({'key': i, 'znak': 'd '})
        izmen(file1[i], file2[i], znak)
    elif file1[i] == file2[i]:
        znak.append({'key': i, 'znak': '  '})
    elif file1[i] != file2[i]:
        znak.append({'key': i, 'znak': '? ', 'old': file1[i], 'new': file2[i]})  # noqa: E501
