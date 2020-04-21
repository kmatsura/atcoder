#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
from collections import deque
#import math

def main():
    n, m, k = map(int, input().split())
    F = [[] for _ in range(n)]
    B = [[] for _ in range(n)]
    for i in range(m):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        F[i].append(j)
        F[j].append(i)
    for i in range(k):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        B[i].append(j)
        B[j].append(i)
    ANS = [0] * n
    for i in range(n):
        ans = 0
        l = [0] * n
        l[i] = 1
        Q = deque(F[i])
        while(Q):
            check = Q.pop()
            if l[check] == 1: continue
            else:
                l[check] = 1
                Fnew = F[check]
                if check not in F[i]:
                    if check not in B[i]: 
                        ans += 1
                Q.extend(Fnew)
        
        ANS[i] = ans
    print(*ANS)




    
if __name__ == '__main__':
    main()
