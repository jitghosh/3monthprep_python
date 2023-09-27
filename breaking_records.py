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
    min_record = None
    max_record = None
    min_broken = 0
    max_broken = 0

    for score in scores:
        if min_record == None and max_record == None:
            min_record,max_record = score,score
        elif score < min_record:
            min_broken += 1
            min_record = score
        elif score > max_record:
            max_broken += 1
            max_record = score
    return [max_broken,min_broken]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
