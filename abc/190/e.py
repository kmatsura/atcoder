#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math
from heapq import heappush, heappop
INF = 10**9
def dijkstra(nodes, cost):
    start_node = nodes[0]
    routes_from_start = {n: math.inf for n in nodes}

    # 最初の頂点にゼロを設定
    routes_from_start[start_node] = 0

    minHeap = []

    # 最初の頂点を追加
    heappush(minHeap, (0, start_node))

    # ヒープがなくなるまで探索
    while minHeap:
        (cost, current_node) = heappop(minHeap)

        # priority keyは重複するのでここでチェックする
        if cost > routes_from_start[current_node]:
            continue

        for node in current_node.routes:
            price_info = current_node.routes[node]
            if routes_from_start[node] > price_info + routes_from_start[current_node]:
                routes_from_start[node] = price_info + routes_from_start[current_node]
                # 更新されたらpriorityに値を追加
                heappush(minHeap, (price_info + routes_from_start[current_node], node))

    return routes_from_start[nodes[-1]]

def main():
    n, m = map(int, input().split())
    G = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        G[a][b] = 1
        G[b][a] = 1
    
    dist = dijkstra()


    


    
if __name__ == '__main__':
    main()
