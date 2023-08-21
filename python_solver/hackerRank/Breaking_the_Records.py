#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    minScore, maxScore, minCount, maxCount = scores[0], scores[0], 0, 0
    for score in scores:
        if score < minScore:
            minScore = score
            minCount += 1
        if score > maxScore:
            maxScore = score
            maxCount += 1

    print(f"[MAX, MIN] = {[maxCount,minCount]}")
    return [maxCount, minCount]


if __name__ == "__main__":
    fptr = open("hackerRank/input.file", "r")
    num_records = fptr.readline()
    records = fptr.readline()
    fptr.close()
    scores = list(map(int, records.rstrip().split()))
    records_break = breakingRecords(scores=scores)
    print(f"Record Broken: Higgest - {records_break[0]} |  Lowest - {records_break[1]}")
