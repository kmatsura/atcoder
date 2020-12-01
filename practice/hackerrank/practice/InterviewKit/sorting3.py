#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.

def activityNotifications(expenditure, d):
    ans = 0
    check_list = {}
    for i in range(201):
        check_list[i] = 0
    for i in range(d):
        if expenditure[i] in check_list:
            check_list[expenditure[i]] += 1
        else:
            check_list[expenditure[i]] = 1
    for i in range(d, len(expenditure)):
        count = 0
        median = 0
        for k, v in check_list.items():
            count += v
            # print(count, median)
            if d%2 == 0:
                if count==d/2:
                    median += k/2
            if count > d/2:
                if median == 0:
                    median += k
                else:
                    median += k/2
                break
        if expenditure[i] >= median*2:
            ans += 1
        check_list[expenditure[i-d]] -= 1
        if expenditure[i] in check_list:
            check_list[expenditure[i]] += 1
        else:
            check_list[expenditure[i]] = 1
    return ans

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)