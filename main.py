import sys
from localparser.parser import parse


def main():
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
    else:
        print("Please type your line: ")
        input_string = input()
    string_to_parse = "{} ".format(input_string)
    print(parse(string_to_parse))


if __name__ == '__main__':
    main()
