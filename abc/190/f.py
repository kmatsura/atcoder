#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def main():
    n = int(input())
    bit = Bit(n)
    tenti = [0 for _ in range(n)]
    A = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        bit.add(A[i]+1, 1)
        tmp = bit.sum(n) - bit.sum(A[i]+1)
        ans += tmp
        tenti[i] = tmp
    for i in range(n):
        c = A[i]
        ans += bit.sum(n) - bit.sum(c+1)
    for i in range(n):
        print(ans)



    


    
if __name__ == '__main__':
    main()
