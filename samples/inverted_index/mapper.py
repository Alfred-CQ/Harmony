#!/usr/bin/env python3

"""Inverted Index Mapper for Document Word Mapping in MapReduce"""

import sys
import os


def read_input(file):
    for line in file:
        line = line.strip()
        yield line.split()


def inverted_index(separator="\t"):
    filepath = os.environ["map_input_file"]
    filename = filepath.split("/")[-1]
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print(f"{word}{separator}{filename}")


if __name__ == "__main__":
    inverted_index()
