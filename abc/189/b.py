#import re
import sys
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, x = map(int, input().split())
    x *= 100
    for i in range(n):
        v, p = map(float, input().split())
        x -= (v * p)
        if x < 0:
            print(i+1)
            break
    else:
        print(-1)
    
if __name__ == '__main__':
    main()
