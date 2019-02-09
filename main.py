import sys
from localparser.scanner import scan
from localparser.parser import parseS as parse


def main():
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
    else:
        print("Please type your line: ")
        input_string = input()
    string_to_parse = "{} ".format(input_string)
    tokens = scan(string_to_parse)
    parse(tokens)
    print("Valid input!")


if __name__ == '__main__':
    main()
