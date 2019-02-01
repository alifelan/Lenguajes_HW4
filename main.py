import sys
from localparser.parser import parse


def main():
    if len(sys.argv) > 1:
        s = ' '.join(sys.argv[1:])
    else:
        print("Please type your line: ")
        s = input()
    print(parse(s))


if __name__ == '__main__':
    main()
