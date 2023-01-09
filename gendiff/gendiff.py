from gendiff.formatters.stylish import formatter_stylish
from gendiff.formatters.plain import formatter_plain
from gendiff.formatters.json import formatter_json
from gendiff.parse import parse_file


def generate_diff(file1, file2, format='stylish'):
    file1 = parse_file(file1)
    file2 = parse_file(file2)
    znak = izmen(file1, file2, [])
    if format == 'stylish':
        res = formatter_stylish(file1, file2, znak)
        print(formatter_stylish(file1, file2, znak))
    elif format == 'plain':
        res = formatter_plain(file1, file2, znak, [])
        print(formatter_plain(file1, file2, znak, []))
    elif format == 'json':
        res = formatter_json(znak)
        print(formatter_json(znak))
    return res


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
    elif fix(file1[i]) == fix(file2[i]):
        znak.append({'key': i, 'znak': '  '})
    elif fix(file1[i]) != fix(file2[i]):
        znak.append({'key': i, 'znak': '? ', 'old': file1[i], 'new': file2[i]})  # noqa: E501


def fix(file):
    if isinstance(file, bool):
        return str(file).lower()
    elif file is None or file == 0:
        return "null"
    else:
        return str(file)
