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
    memo = []
    former = 0
    latter = 0
    mini = 0
    for i in range(n):
        if i%2 == 0: 
            if A[i]<A[mini]:
                mini = i
    if n%2 == 1 and A[mini]<0:
        A[mini] = 0

    for i in range(n):
        if i == 0:
            val = A[0] - A[1]
        elif i == n-1:
            val = A[n-1] - A[n-2]
        else:
            val = A[i] - A[i-1] - A[i+1]
        
        if i%2 == 0:
            former+=val
        else:
            latter+=val
    print(max(former,latter))
    



    
if __name__ == '__main__':
    main()
