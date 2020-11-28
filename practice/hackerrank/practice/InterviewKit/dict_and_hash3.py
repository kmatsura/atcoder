def sherlockAndAnagrams(s):
    ans = 0
    for i in range(1, len(s)):
        for j in range(0, len(s)):
            start = j
            end = j+i
            if end > len(s):
                break
            check1 = s[start:end]
            check1_st = sorted(check1)
            for k in range(j+1, len(s)):
                st = k
                en = k + i
                if en > len(s):
                    break
                check2 = s[st:en]
                check2_st = sorted(check2)
                if check1_st == check2_st:
                    ans += 1
    return ans

s = input()
ans = sherlockAndAnagrams(s)
print(ans)