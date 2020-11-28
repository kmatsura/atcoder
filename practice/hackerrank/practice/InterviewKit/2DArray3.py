#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swap_conter = [0 for i in range(len(q))]
    stop = False
    ans = 0
    for i in range(len(q)):
        if stop == True:
            break
        for j in range(len(q)-1):
            if stop == True:
                break
            if q[j] > j+1 and q[j+1] <= j+2:
                q[j+1], q[j] = q[j], q[j+1]
                swap_conter[q[j+1]-1] += 1
                if swap_conter[q[j+1]-1] > 2:
                    stop = True
                    ans = -1
                else:
                    ans += 1
    if ans == -1:
        print("Too chaotic")
    else:
        print(ans)
                
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
