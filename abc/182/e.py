#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    h, w, n, m = map(int, input().split())
    hl_list = [[] for i in range(h)]
    hb_list = [[] for i in range(h)]
    wl_list = [[] for i in range(w)]
    wb_list = [[] for i in range(w)]
    for i in range(n):
        hl, wl = map(int, input().split())
        hl -= 1
        wl -= 1
        hl_list[hl].append(wl)
        wl_list[wl].append(hl)
    for i in range(m):
        hb, wb = map(int, input().split())
        hb -= 1
        wb -= 1
        hb_list[hb].append(wb)
        wb_list[wb].append(hb)
    ANS = [[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        if not hl_list[i]:
            continue
        elif hl_list[i] and not hb_list[i]:
            for j in range(w):
                ANS[i][j] = 1
        else:  
            p = 0
            pl = hl_list[i][p]
            pe = hl_list[i][-1]
            be = -1
            flagc = 0
            for check in hb_list[i]:
                if flagc == 1:
                    break
                flag = 0
                bs = be + 1
                be = check
                while(pl < check):
                    if flag == 0:
                        for j in range(bs, be):
                            ANS[i][j] = 1
                        flag = 1
                    if pl != pe:
                        p += 1
                        pl = hl_list[i][p]
                    elif pl == pe:
                        flagc = 1
                        break
            if pl > check:
                for j in range(check+1, w):
                    ANS[i][j] = 1

    for i in range(w):
        if not wl_list[i]:
            continue
        elif wl_list[i] and not wb_list[i]:
            for j in range(h):
                ANS[j][i] = 1
        else:  
            p = 0
            pl = wl_list[i][p]
            pe = wl_list[i][-1]
            be = -1
            flagc = 0
            for check in wb_list[i]:
                if flagc == 1:
                    break
                flag = 0
                bs = be + 1
                be = check
                while(pl < check):
                    if flag == 0:
                        for j in range(bs, be):
                            ANS[j][i] = 1
                        flag = 1
                    if pl != pe:
                        p += 1
                        pl = wl_list[i][p]
                    elif pl == pe:
                        flagc = 1
                        break
            if pl > check:
                for j in range(check+1, h):
                    ANS[j][i] = 1
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += ANS[i][j]
    print(ans)


    


    
if __name__ == '__main__':
    main()
