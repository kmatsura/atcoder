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
    Ans = [0]*n
    for i in range(n-1):
        Ans[A[i]-1] += 1
    for i in range(n):
        print(Ans[i])

    


    
if __name__ == '__main__':
    main()
