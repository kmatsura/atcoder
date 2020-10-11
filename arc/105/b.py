import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()
flag = True
while(flag):
    tmp = A[0]
    max_a = A[n-1]
    for i in reversed(range(n)):
        if tmp == max_a:
            break
        if A[i] == max_a:
            A[i] -= tmp
            # flag2 = True
            c = 0
            while(True):
                if i-c == 0:
                    break
                if A[i-c] < A[i-c-1]:
                    t1 = A[i-c]
                    t2 = A[i-c-1]
                    A[i-c-1], A[i-c] = t1, t2
                    c += 1
                else:
                    break
        else:
            break
    if A[0] == A[n-1]:
        flag = False
print(tmp)