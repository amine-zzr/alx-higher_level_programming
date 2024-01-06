#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":

    sum_of = 0

    for arg in argv[1:]:
        sum_of += int(arg)

    print(sum_of)
