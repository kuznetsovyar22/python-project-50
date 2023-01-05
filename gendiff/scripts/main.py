import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


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
    return res


def main():
    args = parse_args()
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
