def kto(file):
    return '[complex value]' if isinstance(file, dict) else fix(file)  # noqa: E501


def search(znak, item):
    for i in znak:
        if i['key'] == item:
            return i['znak']


def output(file1, file2, i, znak):
    if search(znak, i) == '- ':
        return 'removed'
    elif search(znak, i) == '+ ':
        return 'added with value: ' + kto(file2[i])
    elif search(znak, i) == '? ':
        return f'updated. From {kto(file1[i])} to {kto(file2[i])}'


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


def fix(file):
    if isinstance(file, bool):
        return str(file).lower()
    elif file is None:
        return "null"
    elif isinstance(file, int):
        return file
    else:
        return f'\'{file}\''


def formatter_plain(file1, file2, znak, res):
    def walk(file1, file2, path, res):
        allkeys = sorted(list(file1.keys() | file2.keys()))
        for i in allkeys:
            if search(znak, i) == 'd ':
                walk(file1[i], file2[i], path + str(i) + '.', res)  # noqa: E501
                kick(znak, i)
            elif search(znak, i) == '  ':
                kick(znak, i)
                continue
            else:
                res.append(f'Property \'{path + str(i)}\' was {output(file1, file2, i, znak)}\n')  # noqa: E501
                kick(znak, i)
        return ''.join(res)[:-1]
    return walk(file1, file2, '', res)
