#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(k,n+2):
        ans += number(i,n) 
    print(ans%(10**9+7))

def number(i,n):
    minn = int((0 + i - 1)*i/2)
    maxn = int(((n-i+1)+n)*i/2)
    return maxn - minn + 1
if __name__ == '__main__':
    main()
