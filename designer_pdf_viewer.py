#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h,word):
    # Write your code here
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    index=[]
    max_in=0
    sum=0
    for i in range(len(word)):
        arri=arr.index(word[i])
        sum=sum+h[arri]
        index.append(h[arri])
    max_in=max(index)
    return max_in*len(word)


    



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))[:26]

    word = str(input())

    result = designerPdfViewer(h,word)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    # 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7