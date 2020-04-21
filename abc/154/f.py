#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    r1, c1, r2, c2 = map(int, input().split())
    X = [[0]*r2 for i in range(c2)]
    for i in range(r2):
        for j in range(c2):
            if i>=1 and j>=1:
                X[i][j] = X[i-1][j] + X[i][j-1]
            elif i!= 0:
                X[i][j] = X[i-1][j]
            elif j!= 0:
                X[i][j] = X[i][j-1]
            else:
                X[i][j] = 0
    
    print(X)
def dp(r,c):
    if r>1 and c>0:
        return dp(r-1,c) + dp(r,c-1)
    elif r == 0 and c>0:
        return dp(r,c-1)
    elif r>0 and c == 0:
        return dp(r-1,0)
    elif r==0 and c==0: return 1


    
if __name__ == '__main__':
    main()
