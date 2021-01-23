#import re
import sys
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n = int(input())
    num_t = 1
    num_f = 1
    for i in range(n):
        s = input()
        num_f_b = num_f
        num_t_b = num_t
        if s == "OR":
            num_t = num_t_b * 2 + num_f_b
            num_f = num_f_b
        else:
            num_t = num_t_b
            num_f = num_t_b + num_f_b * 2
    print(num_t)

    
if __name__ == '__main__':
    main()


