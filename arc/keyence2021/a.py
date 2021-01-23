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
    B = list(map(int, input().split()))
    max_b = 0
    max_a = 0
    tmp_max = 0
    for i in range(n):
        ans = 0
        a = A[i]
        b = B[i]
        if max_a < a:
            max_a = a
        comp = max_a * b
        if comp > tmp_max:
            tmp_max = comp
        print(tmp_max)


    
if __name__ == '__main__':
    main()
