#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zero_count = 0

    for itm in arr:
        if itm > 0:
            pos_count += 1
        elif itm < 0:
            neg_count += 1
        else:
            zero_count += 1
    print(f"{pos_count/len(arr):0.6f}")
    print(f"{neg_count/len(arr):0.6f}")
    print(f"{zero_count/len(arr):0.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)