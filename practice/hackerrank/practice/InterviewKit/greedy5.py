from collections import deque
from collections import OrderedDict
from string import ascii_lowercase


def extract_char(ans, tmp_count, tmp_word, len_ans, resmap):
    print("tmpw", tmp_word)
    print("ansb", ans)
    # print("tc", tmp_count)
    i = 0
    for char in ascii_lowercase:
        # print(tmp_count)
        if resmap[char] == 0:
            continue
        while tmp_count[char] >= 1:
            ans += char
            resmap[char] -= 1
            # tmp_count[char] -= 1
            # if len(tmp_word) >=  2:
                # tmp_word = tmp_word[1:]
            # else:
                # return ans
            if len(ans) == len_ans:
                return ans
            while(True):
                c = tmp_word[i]
                i += 1
                tmp_count[c] -= 1
                print(i, c, tmp_count)
                if c == char:
                    break
    print("tmpwa", tmp_word)
    print("ansa", ans)
    return ans, resmap

s = input()
word_count = OrderedDict()
tmp_count_tmp = OrderedDict()
for char in ascii_lowercase:
    word_count[char] = 0
    tmp_count_tmp[char] = 0
for c in s:
    word_count[c] += 1
usemap = {}
resmap = {}
for k, v in word_count.items():
    usemap[k] = int(v/2)
    resmap[k] = int(v/2)
ans = ""
tmp_count = tmp_count_tmp.copy()
print(word_count)
# print(usemap)
print("s", s)
# print(len(s))
# print(int(len(s)/2))
tmp_word = ""
len_ans = int(len(s)/2)
for c in reversed(s):
    usemap[c] -= 1
    if usemap[c] == -1:
        ans, resmap = extract_char(ans, tmp_count, tmp_word, len_ans, resmap)
        tmp_count = tmp_count_tmp.copy()
        tmp_word = ""
        if resmap[c] >= 1:
            ans += c
            resmap[c] -= 1
    else:
        tmp_count[c] += 1
        tmp_word += c
    if len(ans) == len_ans:
        break
# print(len(ans))
# print(ans)