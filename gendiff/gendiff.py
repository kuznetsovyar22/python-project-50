def generate_diff(file1, file2):
    res = ''
    allkeys = sorted(set(list(file1.keys()) + list(file2.keys())))
    for i in allkeys:
        if i not in file2.keys():
            res += '- ' + str(i) + ': ' + str(file1[i]) + '\n'
        elif i not in file1.keys():
            res += '+ ' + str(i) + ': ' + str(file2[i]) + '\n'
        elif file1[i] == file2[i]:
            res += '  ' + str(i) + ': ' + str(file1[i]) + '\n'
        elif file1[i] != file2[i]:
            res += '- ' + str(i) + ': ' + str(file1[i]) + '\n'
            res += '+ ' + str(i) + ': ' + str(file2[i]) + '\n'
    res = res[:-1]
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
    elif file1[i] == file2[i]:
        znak.append({'key': i, 'znak': '  '})
    elif file1[i] != file2[i]:
        znak.append({'key': i, 'znak': '? ', 'old': file1[i], 'new': file2[i]})  # noqa: E501
