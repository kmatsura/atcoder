#import re
import sys
#input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    s, t = input().split()
    a, b = map(int,input().split())
    u = input()
    if s == u:
        print(a-1, b)
    else:
        print(a, b-1)


    
if __name__ == '__main__':
    main()
