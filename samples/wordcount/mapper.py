#!/usr/bin/env python3

"""Mapper script for counting word occurrences in a dataset for MapReduce"""

import sys


def read_input(file):
    for line in file:
        line = line.strip()
        yield line.split()


def wordcount(separator="\t"):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print(f"{word}{separator}1")


if __name__ == "__main__":
    wordcount()
