#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s : str):
    timeparts = s.split(":")
    is_am = True if timeparts[2].lower().endswith("am") else False
    timeparts[-1] = timeparts[-1][0:2]
    if is_am == "am":
        return ":".join(timeparts[0:3])
    else:
        timeparts[0] = str(int(timeparts[0]) + 12)
        return ":".join(timeparts[0:3])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
