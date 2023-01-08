import argparse
from gendiff.gendiff import izmen
from gendiff.parse import parse_file
from gendiff.format import stringify


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', default='stylish', help='set format of output')  # noqa: E501
    return parser.parse_args()


def main():
    args = parse_args()
    file1 = parse_file(args.first_file)
    file2 = parse_file(args.second_file)
    if args.format == 'stylish':
        znak = izmen(file1, file2, [])
        print(stringify(file1, file2, znak))


if __name__ == '__main__':
    main()
