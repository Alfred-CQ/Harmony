#!/usr/bin/env python3

"""JSON Inverted Index Mapper for Document Word Mapping in MapReduce"""

import sys
import os
import json

def read_input(file):
    for line in file:
        yield json.loads(line.strip())


def inverted_index(separator="\t"):
    data = read_input(sys.stdin)
    for record in data:
        document_id = record.get('id', '')
        content = record.get('content', '')
        words = content.split()
        for word in words:
            print(f"{word}{separator}{document_id}")


if __name__ == "__main__":
    inverted_index()
