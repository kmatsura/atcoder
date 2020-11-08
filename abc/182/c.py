n = input()
n_list = [0 for _ in range(len(n))]
len_n = len(n_list)
sum_n = 0
for i in range(len(n)):
  n_list[i] = int(n[i])%3
  sum_n += int(n[i])%3
key = sum_n%3
if key == 0:
    print(0)
elif key == 1:
    if len_n == 1:
        print(-1)
    elif 1 in n_list:
        print(1)
    else:
        if len_n == 2:
            print(-1)
        else:
            c2 = 0
            for n in n_list:
                if n == 2:
                    c2 += 1
                if c2 >= 2:
                    print(2)
                    break
            else:
                print(-1)
elif key == 2:
    if len_n == 1:
        print(-1)
    elif 2 in n_list:
        print(1)
    else:
        if len_n == 2:
            print(-1)
        else:
            c1 = 0
            for n in n_list:
                if n == 1:
                    c1 += 1
                    if c1 >= 2:
                        print(2)
                        break
            else:
                print(-1)
