#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    h, w = map(int, input().split())
    ans = 0
    W = ["" for i in range(h)]
    for i in range(h):
        W[i] = input().split()[0]
        yoko = W[i]
        for j in range(w-1):
            if yoko[j] == "." and yoko[j+1] == ".":
                ans += 1
    for i in range(h-1):
        for j in range(w):
            if W[i][j] == "." and W[i+1][j] == ".":
                ans += 1
    print(ans)

    
if __name__ == '__main__':
    main()
