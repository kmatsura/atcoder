#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n = int(input())
    rgb = input()
    ans = 0
    for moji in ["RGB", "RBG", "BGR", "BRG", "GBR", "GRB"]:
        ans += search(moji, rgb)
    print(ans)

def search(moji, kensaku):
    n = len(kensaku)
    memo1 = []
    r = 0
    g = 0
    b = 0
    red = 0
    for i in range(n):
        if kensaku[i] == moji[0]:
            memo1.append(i)
        elif kensaku[i] == moji[1]:
            for num in memo1:
                check = num + 2 * (i - num)
                if check >= n:
                    continue
                else:
                    if kensaku[check] == moji[2]:
                        red += 1
    for i in range(n):
        if kensaku[i] == moji[0]:
            r += 1
        elif kensaku[i] == moji[1]:
            g += r
        elif kensaku[i] == moji[2]:
            b += g
    ans = b - red
    return ans


    


    
if __name__ == '__main__':
    main()
