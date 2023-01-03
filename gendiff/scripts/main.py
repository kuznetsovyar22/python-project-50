import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', metavar='first_file')
parser.add_argument('second_file', metavar='second_file')
parser.add_argument('-f', '--format', help='set format of output')

def main():
    print('Bebra')
    args = parser.parse_args()
    print(args.accumulate(args.integers))

if __name__ == '__main__':
    main()