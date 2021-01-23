#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        check_min = A[i]
        for j in range(i, n):
            if A[j] < check_min:
                check_min = A[j]
            length = j - i + 1
            tmp = check_min * length
            if ans < tmp:
                ans = tmp
    print(ans)

            



    
if __name__ == '__main__':
    main()
