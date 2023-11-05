#!/usr/bin/env python3
"""Inverted Index Reducer for Aggregating Document Word Mappings in MapReduce"""

import sys
from itertools import groupby
from operator import itemgetter


def read_mapper_output(file, separator="\t"):
    for line in file:
        yield line.rstrip().split(separator, 1)


def reducer(separator="\t"):
    data = read_mapper_output(sys.stdin, separator=separator)

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            documents = set(doc_name for _, doc_name in group)
            documents_str = ", ".join(documents)
            print(f"{current_word}{separator}{documents_str}")
        except ValueError:
            pass


if __name__ == "__main__":
    reducer()
