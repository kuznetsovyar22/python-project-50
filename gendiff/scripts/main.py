import argparse
from gendiff.gendiff import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', default='stylish', help='set format of output')  # noqa: E501
    return parser.parse_args()


def main():
    args = parse_args()
    file1 = args.first_file
    file2 = args.second_file
    print(generate_diff(file1, file2, args.format))


if __name__ == '__main__':
    main()
