#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    t = int(input())
    for _ in range(t):
        count = 0
        ax, ay, bx, by, cx, cy = map(int, input().split())
        mean_x = (ax + bx + cx) / 3
        mean_y = (ay + by + cy) / 3
        move_x = int(mean_x) * 2
        move_y = int(mean_y) * 2
        shape = round((mean_x - move_x)), round((mean_y - move_y))
        print(move_x, move_y)
        move_x += shape[0]
        move_y += shape[1]
        naname = min(abs(move_x), abs(move_y))
        yoko = max(abs(move_x), abs(move_y)) - naname
        print(move_x, move_y, naname, yoko)
        count += naname
        count += yoko
        if move_x == 1 and move_y == 1:
            print(1)
            continue
        elif move_x == 1 and move_y == -1:
            print(1)
            continue
        elif move_x == -1 and move_y == 1:
            print(1)
            continue
        if naname > 0 and yoko == 0:
            count += 2
        print(count)
        

    


    
if __name__ == '__main__':
    main()
