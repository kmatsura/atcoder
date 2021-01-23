from collections import OrderedDict
from string import ascii_lowercase


s = input()
word_count = OrderedDict()
for char in ascii_lowercase:
    word_count[char] = -2
for c in s:
    if word_count[c] == -2:
        word_count[c] = 1
    else:
        word_count[c] += 1
resmap = {}
usemap = {}
for k, v in word_count.items():
    resmap[k] = int(v/2)  # 残りの余裕
    usemap[k] = int(v/2)  # 使ったやつ
ans = ""

i = 0
s = list(reversed(s))
for char in ascii_lowercase:
    # print(char, ans)
    # print("hi1", char, i, ans)
    while(True):
        # print("hi2", char, i, ans)
        # print(resmap)
        if resmap[char] == -1 and usemap[char] == -1:
            break
        check = s[i]
        c = 1
        if check < char:
            c -= 1
        while(c > 0):
            # print("hi3", char, i, ans, check)
            c -= 1
            resmap[check] -= 1
            if resmap[check] < 0:
                ans += check
                usemap[check] -= 1
                break
            if check == char:
                if resmap[char] >= 0:
                    ans += char
                    usemap[char] -= 1
                    # resmap[char] -= 1
                    if resmap[char] == 0:
                        resmap[char] = -1
                        usemap[char] = -1
                        break
        if i == len(s)-1:
            break
        else:
            i += 1
print(ans)