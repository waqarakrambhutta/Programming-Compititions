#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    new_arr = set(arr)
    
    max_num= max(new_arr,key= arr.count)

    return max_num
 


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))[:arr_count]

    result = migratoryBirds(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
