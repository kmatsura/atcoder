#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n = input()
    for c in n:
        if c == "7": 
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()
