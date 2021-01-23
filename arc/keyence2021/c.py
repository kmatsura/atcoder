#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
from collections import deque
#import math

def main():
    h, w, k = map(int, input().split())
    HW = [[[-1, -1, ""] for _ in range(w)] for _ in range(h)]
    masu = h * w
    l_keiro = h + w - 1
    nandemo = 3 ** (masu - l_keiro)
    num_keiro = 0
    NK = [[-1 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        NK[i][0] = 1
    for i in range(w):
        NK[0][i] = 1
    for i in range(h):
        if i == 0:
            continue
        for j in range(w):
            if j == 0:
                continue
            NK[i][j] = NK[i-1][j] + NK[i][j-1]
    num_keiro = NK[h-1][w-1]
    for i in range(h):
    


    
if __name__ == '__main__':
    main()
