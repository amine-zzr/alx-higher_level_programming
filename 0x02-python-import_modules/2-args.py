#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num = len(argv) - 1
    print("{:d} argument{}{}".format(num, 's' if num != 1 else '',
                                     ':' if num != 0 else '.'))
    for i, arg in enumerate(argv[1:], 1):
        print("{:d}: {}".format(i, arg))
