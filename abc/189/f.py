#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, m, k = map(int, input().split())
    if k > 0:
        A = list(map(int, input().split()))
    exp_m = (1+m) / 2
    time = 10**4
    for i in range(time):
        num = 0
        for a in A:
            num += (a - m) / exp_m


    


    
if __name__ == '__main__':
    main()
