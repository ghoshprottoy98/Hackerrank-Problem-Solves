#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    length = len(s)
    start = 0
    end = 1
    sum_of_squares = s[start]
    count = 0
    
    while True:
        print(sum_of_squares,count, start, end)
        if sum_of_squares == d and end - start == m:
            count += 1
            sum_of_squares -= s[start]
            start += 1
        elif sum_of_squares >= d:
            sum_of_squares -= s[start]
            start += 1
        else:
            if end == length:
                break
            sum_of_squares += s[end]
            end += 1
            
    return count
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
