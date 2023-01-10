import itertools


def kto(file, depth):
    return str(stringify(file, spacesCount=depth + 2)) if isinstance(file, dict) else fix(file)  # noqa: E501


def search(znak, item):
    for i in znak:
        if i['key'] == item:
            return i['znak']
    return '  '


def kick(znak, item):
    count = 0
    for i in znak:
        if i['key'] == item:
            count += 1
        if count > 1:
            for j in znak:
                if j['key'] == item:
                    znak.remove(j)
                    return


def output(file1, file2, i, znak, depth):
    if search(znak, i) == '- ':
        return kto(file1[i], depth)
    elif search(znak, i) == '  ':
        return kto(file2[i], depth)
    elif search(znak, i) == '+ ':
        return kto(file2[i], depth)


def fix(file):
    if isinstance(file, bool):
        return str(file).lower()
    elif file is None:
        return "null"
    else:
        return str(file)


def formatter_stylish(file1, file2, znak, replacer='  '):
    def walk(file1, file2, depth):
        res = ''
        allkeys = sorted(list(file1.keys() | file2.keys()))
        tab = replacer * depth
        curtab = replacer * (depth + 1)
        for i in allkeys:
            if search(znak, i) == 'd ':
                res += curtab + '  ' + fix(i) + ': ' + fix(walk(file1[i], file2[i], depth + 2)) + '\n'  # noqa: E501
                kick(znak, i)
            elif search(znak, i) == '? ':
                res += curtab + '- ' + fix(i) + ': ' + kto(file1[i], depth) + '\n'  # noqa: E501
                res += curtab + '+ ' + fix(i) + ': ' + kto(file2[i], depth) + '\n'  # noqa: E501
                kick(znak, i)
            else:
                res += curtab + search(znak, i) + fix(i) + ': ' + output(file1, file2, i, znak, depth) + '\n'  # noqa: E501
                kick(znak, i)
        result = itertools.chain('{', '\n', res, [tab + '}'])
        return ''.join(result)
    return walk(file1, file2, 0)


def stringify(tree, replacer='  ', spacesCount=1):
    def walk(value, depth):
        res = ''
        tab = replacer * (spacesCount * depth)
        curtab = tab + replacer
        for i in value:
            if isinstance(value[i], dict):
                res += curtab + '  ' + str(i) + ': ' + str(walk(value[i], depth + 1)) + '\n'  # noqa: E501
            else:
                res += curtab + '  ' + str(i) + ': ' + str(value[i]) + '\n'
        result = itertools.chain('{', '\n', res, [tab + '}'])
        return ''.join(result)
    return walk(tree, 1)
