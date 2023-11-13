#!/usr/bin/env python3
"""Inverted Index Reducer for Aggregating Document Word Mappings in MapReduce"""

import sys
import json
from itertools import groupby
from operator import itemgetter


def read_mapper_output(file, separator="\t"):
    for line in file:
        yield line.rstrip().split(separator, 1)


def reducer(separator="\t"):
    data = read_mapper_output(sys.stdin, separator=separator)

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            documents = set(int(doc_id) for _, doc_id in group)
            json_output = json.dumps({"word": current_word, "documents": list(documents)})
            print(json_output)
        except ValueError:
            pass


if __name__ == "__main__":
    reducer()
