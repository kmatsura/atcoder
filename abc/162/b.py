#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        if (i+1)%3 == 0 or (i+1)%5 == 0:
            continue
        else:
            ans += i+1 
    print(ans)

    
if __name__ == '__main__':
    main()
