#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    a = 0
    for i in range(m): 
        a += A[i]
    ans = n - a
    if ans >= 0:
        print(ans)
    else:
        print(-1)
    
if __name__ == '__main__':
    main()
