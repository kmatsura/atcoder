#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect


n = int(input())
L = list(map(int, input().split()))
mc = 0
ans = 0
for i in range(1000):
  if i == 0:
      continue
  count = 0
  for l in L:
    if l%(i+1)==0:
      count += 1
  if mc <= count:
    mc = count
    ans = i+1
print(ans)