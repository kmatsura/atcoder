#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, m = map(int, input().split())
    W = list(map(int, input().split()))
    W.sort(reverse=True)
    VL = [(0,0) for i in range(m)]
    # V = [0 for i in range(m)]
    for i in range(m):
        VL[i] = list(reversed(list(map(int, input().split()))))
    VL.sort()

    print(n,m,W,VL)
    


    
if __name__ == '__main__':
    main()
