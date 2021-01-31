#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n, s, d = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            break
    else:
        print("No")
    


    
if __name__ == '__main__':
    main()
