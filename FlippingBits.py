#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
    # Write your code here
    binaryStr = '{:032b}'.format(n)
    print(f"binaryStr: ", {binaryStr})
    flippedBinaryStr = ''.join(['1' if i == '0' else '0' for i in binaryStr])
    return int(flippedBinaryStr,2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
