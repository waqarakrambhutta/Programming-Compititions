import math
import os
import random
import re
import sys
def findDigits(n):
    # Write your code here
    s= str(n)
    counter=0
    for i in range(len(s)):
        try:
            if s[i]!=0:
                if n%(int(s[i]))==0:
                    counter=counter+1
        except ZeroDivisionError as e:
            pass
    print(counter)
        
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)