#import re
#import heapq
#import bisect
#from collections import deque
import math
from functools import reduce

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans += gcd(i+1, j+1, k+1)
    print(ans)

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)
    


    
if __name__ == '__main__':
    main()
