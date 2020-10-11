#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math


def get_num(x, y, a):
    if x < a or y < a:
        return 0
    else:
        return (x - a + 1) * (y - a + 1)
def main():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        # a <= bにする
        if a > b:
            a, b = b, a
        a_max = (n - a + 1)**2
        ans = 0
        naka = n - (2 * a)
        if naka > b:
            ans += (naka - b) ** 2 * (a_max - (a + b - 1) ** 2)
            ans += 4 * (a**a * a_max - (a-1)**2*a**2/2 - a**2*(a-1)*b - a**2*b**2)
            ans += 4 * (a**a * a_max - )

        for i in range(n - b):
            for j in range(n - b):

                ans %= 1000000007
        print(ans)


    
if __name__ == '__main__':
    main()
