#import re
import sys
#input = sys.stdin.readline
#import heapq
#import bisect
from collections import deque
#import math

def main():
    n, k = map(int, input().split())
    P = list(map(int,input().split()))
    d = deque()
    tmpans = 0
    ans = 0
    for i in range(k):
        tmpans += (P[i]+1)/2.0
        d.append(P[i])

    for i in range(k,n):
        com = d.popleft()
        into = P[i]
        d.append(into)
        tmpans = tmpans + (into - com)/2
        if ans < tmpans: ans = tmpans
    print(ans)
    
    


    
if __name__ == '__main__':
    main()
