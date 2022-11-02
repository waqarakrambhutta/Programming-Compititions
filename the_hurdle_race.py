#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    maxi= height[0]
    for i in height:
        if i > maxi:
            maxi=i
    if k<maxi:
        doses=maxi-k
    elif k>=maxi:
        doses=0
    return doses


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))[:n]

    result = hurdleRace(k, height)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
