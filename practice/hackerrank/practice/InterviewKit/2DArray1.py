#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
MIN = -100

def calc_a_hour_glass_sum(arr, i, j):
    try:
        ans = (arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1])
    except:
        ans = MIN
    return ans

def hourglassSum(arr):    
    max_ans = MIN
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            tmp = calc_a_hour_glass_sum(arr, i, j)
            print(tmp, (i,j))
            if tmp > max_ans:
                max_ans = tmp
    return max_ans

        
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
