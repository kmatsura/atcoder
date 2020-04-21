#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    B = [[]*3 for i in range(3)]
    for i in range(3):
        B[i] = list(map(int, input().split()))
    
    C = [[0]*3 for i in range(3)]
    n = int(input())
    for i in range(n):
        check = int(input())
        for i in range(3):
            for j in range(3):
                if B[i][j] == check:
                    C[i][j] = 1
    ans = "No"
    for i in range(3):
        if (C[i][0] == 1 and C[i][1] == 1 and C[i][2] == 1):
            ans = "Yes"
            break
        if (C[0][i] == 1 and C[1][i] == 1 and C[2][i] == 1):
            ans = "Yes"
            break
        if (C[0][0] == 1 and C[1][1] == 1 and C[2][2] == 1):
            ans = "Yes"
            break
        if (C[2][0] == 1 and C[1][1] == 1 and C[0][2] == 1):
            ans = "Yes"
            break
    
    print("Yes") if ans == "Yes" else print("No")
            
            


    
if __name__ == '__main__':
    main()
