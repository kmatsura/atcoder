#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    hashmap = {}
    for i in range(n):
        hashmap[i] = 0
    for a in A:
        hashmap[a] += 1
    ans = 0
    tmp = k
    for i in range(n):
        c = hashmap[i]
        if tmp > c:
            tmp = c
        if tmp > 0:
            ans += tmp
        else:
            break
    print(ans)

    


    
if __name__ == '__main__':
    main()
