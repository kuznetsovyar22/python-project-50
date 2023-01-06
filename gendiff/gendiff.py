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

