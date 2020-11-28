def countTriplets(arr, r):
    ans = 0
    hashmap = {}
    hashmap2 = {}
    for num in arr:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    for num in arr:
        if num in hashmap2:
            hashmap2[num] += 1
        else:
            hashmap2[num] = 1
        if (num % r) != 0:
            continue
        else:
            try:
                l = hashmap2[int(num/r)]
            except:
                l = 0
            try:
                r1 = hashmap[r*num]
            except:
                r1 = 0
            try:
                r2 =  hashmap2[r*num]
            except:
                r2 = 0
            right = r1 - r2
            print(l, right)
            ans += l * right
    return ans

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)