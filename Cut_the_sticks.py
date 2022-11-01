#!/bin/python3

import math
import os
import random
import re
import sys

from sqlalchemy import true

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    # mini=min(arr)
    arr2=[]
    counter=0


    
    for i in range(n):
        
        mini=min(arr)
        arr.remove(mini)
        arr2.append(arr[i]-mini)
        # print(len(arr2))
        arr= arr[i]-mini
        print(arr)
        # if arr[i]!=0:
        #     counter=counter+1
        # print(counter)
    
    
        # for j in range(len(arr2)):
        #     if arr2[j]==0:
        #         pass
        #     else:
        #         counter=counter+1
        # print(counter)
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().strip().split()))[:n]
    # print(arr)
    result=cutTheSticks(arr)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
