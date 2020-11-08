#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    # 入力
    n = int(input())
    A = list(map(int, input().split()))
    P = [0 for _ in range(n)]
    Q = [0 for _ in range(n)]
    max_n = 0
    now = 0
    for i in range(n):
        if i == 0:
            P[i] = A[i]
            Q[i] = max(0, A[i])
        else:
            P[i] = P[i-1] + A[i]
            Q[i] = max(Q[i-1], P[i])
    r = 0
    x = 0
    for i in range(n):
        r = max(r, x + Q[i])
        x += P[i]
    print(r)
    
if __name__ == '__main__':
    main()
