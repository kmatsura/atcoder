#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, m = map(int, input().split())
    ans = 0
    if n == 3:
        A = [10] * 3
        for i in range(m):
            s, c = map(int, input().split())
            s -= 1
            if A[s] == 10:
                A[s] = c
            elif A[s] != c:
                ans = -1
                break
        if A[0] == 0:
            ans = -1
        if A[0] == 10:
            A[0] = 1
        if A[1] == 10:
            A[1] = 0
        if A[2] == 10:
            A[2] = 0
        if ans == -1: print(-1)
        else: print(str(A[0]) + str(A[1]) + str(A[2]))
    
    if n == 2:
        A = [10] * 2
        for i in range(m):
            s, c = map(int, input().split())
            s -= 1
            if A[s] == 10:
                A[s] = c
            elif A[s] != c:
                ans = -1
                break
        if A[0] == 0:
            ans = -1
        if A[0] == 10:
            A[0] = 1
        if A[1] == 10:
            A[1] = 0
        if ans == -1: print(-1)
        else: print(str(A[0]) + str(A[1]))
    
    if n == 1:
        A = 10
        for i in range(m):
            s, c = map(int, input().split())
            if A == 10:
                A = c
            elif A != c:
                ans = -1
                break
        if A == 10:
            A = 0
        if ans == -1: print(-1)
        else: print(str(A))
        
        


    
if __name__ == '__main__':
    main()
