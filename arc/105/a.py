#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    a, b, c, d = map(int, input().split())
    if a == b+c+d:
        print("Yes")
    elif b == a+c+d:
        print("Yes")
    elif c == a+b+d:
        print("Yes")
    elif d == a+b+c:
        print("Yes")
    elif a+b == c+d:
        print("Yes")
    elif a+c == b+d:
        print("Yes")
    elif a+d == b+c:
        print("Yes")
    else:
        print("No")
    


    
if __name__ == '__main__':
    main()
