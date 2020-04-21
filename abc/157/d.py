#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, m, k = map(int, input().split())
    F = [[0] * n for _ in range(n)]
    B = [[0] * n for _ in range(n)]
    for i in range(m):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        F[i][j] = 1
        F[j][i] = 1
    for i in range(k):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        B[i][j] = 1
        B[j][i] = 1
    
    ans = [0] * n 
    


    
if __name__ == '__main__':
    main()
