#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ANS = [0 for i in range(200001)]
    ans = 0
    for i in range(n):
        check = p[i]
        if ANS[check] == 0:
            ANS[check] = 1
        if ans != check:
            print(ans)
        else:
            for j in range(ans, 200001):
                if ANS[j] == 0:
                    ans = j
                    print(ans)
                    break

    


    
if __name__ == '__main__':
    main()
