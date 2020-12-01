#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    word_counter = {}
    for char in s:
        if char in word_counter:
            word_counter[char] += 1
        else:
            word_counter[char] = 1
    wc_list = sorted(word_counter.items(), reverse=True)
    wc_pointer = 0
    wc_list = list(map(lambda x: [x[0], x[1]/2], wc_list))
    ans = ""
    for char in s:
        print(char, ans, wc_pointer)
        if char == wc_list[wc_pointer][0]:
            ans = char + ans
            wc_list[wc_pointer][1] -= 1
            if wc_list[wc_pointer][1] == 0:
                wc_pointer += 1
                if wc_pointer == len(wc_list):
                    break
    return ans

if __name__ == '__main__':
    s = input()

    result = reverseShuffleMerge(s)

    print(result)