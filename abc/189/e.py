#import re
import sys
import numpy as np
#import heapq
#import bisect
from collections import deque
#import math

def rotation(X, Y, rot):
    r = rot % 4
    if r == 0:
        return X, Y
    elif r == 1:
        return Y, X*-1
    elif r == 2:
        return X*-1, Y*-1
    elif r == 3:
        return Y*-1, X

def main():
    n = int(input())
    X = np.array([0]*n)
    Y = np.array([0] * n)
    for i in range(n):
        X[i], Y[i] = map(int, input().split())
    m = int(input())
    OP = [0] * m
    for i in range(m):
        OP[i] = tuple(map(int, input().split()))
    q = int(input())
    A = [0] * q
    B = [0] * q
    Q = [0] * q
    for i in range(q):
        Q[i] = tuple(map(int, input().split()))
    Q.sort()
    rot = 0
    p = 0
    for i in range(m):
        while(Q[p][0] == i):
            X, Y = rotation(X, Y, rot)
            rot = 0
            pos = Q[p][1]
            print(X[pos-1], Y[pos-1])
            p += 1
            if p >= len(Q):
                break
        op = OP[i][0]
        if op == 1:
            rot += 1
        elif op == 2:
            rot -= 1
        elif op == 3:
            X, Y = rotation(X, Y, rot)
            rot = 0
            jiku = OP[i][1]
            X = 2 * jiku - X
        elif op == 4:
            X, Y = rotation(X, Y, rot)
            rot = 0
            jiku = OP[i][1]
            Y = 2 * jiku - Y
    while(p < len(Q)):
        X, Y = rotation(X, Y, rot)
        rot = 0
        pos = Q[p][1]
        print(X[pos-1], Y[pos-1])
        p += 1
        if p >= len(Q):
            break

    
if __name__ == '__main__':
    main()
