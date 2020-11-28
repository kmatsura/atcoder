#import re
import sys
input = sys.stdin.readline
#import bisect
#from collections import deque
#import math


def janken(h1, h2):
    if h1 == h2:
        return h1
    elif h1 == "R":
        if h2 == "S":
            return "R"
        elif h2 == "P":
            return "P"
    elif h1 == "S":
        if h2 == "R":
            return "R"
        elif h2 == "P":
            return "S"
    elif h1 == "P":
        if h2 == "S":
            return "S"
        elif h2 == "R":
            return "P"
    else:
        return None

def main():
    n, k = map(int, input().split())
    hand = input()
    # print(n,k,hand)
    stride = 2 * n
    tmp = ""
    for i in range(k):
        for j in range(int(stride/2)):
            # print((2*j)%n, (2*j+1)%n)
            # print(hand[(2*j)%n], hand[(2*j+1)%n])
            h1 = hand[(2*j)%n]
            h2 = hand[(2*j+1)%n]
            result = janken(h1, h2)
            tmp += result
        hand = tmp
        tmp = ""
        # print(hand)
    print(hand[0])
    
if __name__ == '__main__':
    main()
