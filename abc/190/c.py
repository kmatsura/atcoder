#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, m = map(int, input().split())
    M = [0 for _ in range(m)]
    for i in range(m):
        M[i] = tuple(map(int, input().split()))
    k = int(input().split()[0])
    K = [0 for _ in range(k)]
    for i in range(k):
        K[i] = tuple(map(int, input().split()))
    ans = 0
    for i in range(2**k):
        c = str(bin(i))[2:]
        while(len(c) < k):
            c = "0" + c
        ballset = set()
        for j in range(len(c)):
            choose = int(c[j])
            ball = K[j][choose]
            ballset.add(ball)
        tmp = 0
        for m in M:
            a = m[0]
            b = m[1]
            if a in ballset and b in ballset:
                tmp += 1
        if tmp > ans:
            ans = tmp
    print(ans)
    


    
if __name__ == '__main__':
    main()
