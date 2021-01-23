#import re
import sys
input = sys.stdin.readline
from math import factorial
import itertools

#import heapq
#import bisect
#from collections import deque
#import math

def main():
    ni = int(input())
    nt = 2 ** ni
    # print(nt)
    n = nt - 1
    r = int((n-1)/2)
    a = factorial(n) / factorial(r) / factorial(n - r)
    a = int(a)
    print(a)
    s = "A" * int(nt/2) + "B" * int(nt/2)
    # c = 0
    # while(True):
    lis = range(n)
    s = ["B" for _ in range(n)]
    ans_list = []
    for pair in itertools.combinations(lis, r):
        tmp = s.copy()
        for i in pair:
            tmp[i] = "A"
        ans_list.append(tmp)
        print("A"+"".join(tmp))
    for i in range(nt):
        for j in range(i+1, nt):
            c = 0
            for ans in ans_list:
                tmp = ["A"].copy()
                tmp.extend(ans)
                if tmp[i] == tmp[j]:
                    c += 1
            print(c)


    
    


    
if __name__ == '__main__':
    main()
