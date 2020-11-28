#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    a, b, x, y = map(int, input().split())
    if a > b:
        if 2 * x >= y:
            print(y * (a-b-1) + x)
        else:
            print(2 * x * (a-b-1) + x)

    else:
        if 2 * x >= y:
            print(y * (b-a) + x)
        else:
            print(2 * x * (b -a) + x)
    


    
if __name__ == '__main__':
    main()
