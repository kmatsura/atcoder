#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    ans = 0
    for i in range(n):
        d = 0
        while(True):
            if i-d < 0 or i+d >= n:
                break
            elif s[i-d] == s[i+d]:
                if d>1:
                    if s[i-d+1] != s[i-d]:
                        break
                print(s[i-d: i+d+1])
                ans += 1
                d += 1
            else:
                break
    print(ans)
    for i in range(n):
        d = 0
        while(True):
            if i - d < 0 or i + 1 + d >= n:
                break
            elif s[i - d] == s[i + 1 + d]:
                ans += 1
                d += 1
            else:
                break
    print(ans)
    return ans
        

if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(result)