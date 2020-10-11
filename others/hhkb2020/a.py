#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    s = input().split()[0]
    t = input().split()[0]
    if s == "Y":
        mapper = {"a": "A", "b": "B", "c": "C"}
        print(mapper[t])
    else:
        print(t)
    


    
if __name__ == '__main__':
    main()
