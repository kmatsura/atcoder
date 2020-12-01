#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * m for _ in range(n)]
    for i in range(m):
        if s2[0] in s1[:i+1]:
            dp[0][i] = 1
    for i in range(n):
        if s1[0] in s2[:i+1]:
            dp[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    return dp[n-1][m-1]
if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)