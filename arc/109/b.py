import sys
input = sys.stdin.readline
import numpy as np

n = int(input())
n = np.float128(n)
k = int((-1 + (1 + 8 * (n+1)) ** 0.5) / 2)
print(n - k + 1)
