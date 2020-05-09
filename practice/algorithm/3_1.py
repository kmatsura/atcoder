import sys

def main():
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    def insert(_h, size, x, i):
        h = _h.copy()
        if h[x%size - i] == 0:
            h[x%size-i] = x
            return h
        else:
            return insert(h, size, x, i+1)

    def search(h, size, x, i):
        if h[x%size - i] == 0:
            print("not found")
            return h
        elif h[x%size - i] == x:
            print("found")
            return h
        else:
            return search(h, size, x, i+1)
        
    q = int(input())
    size = 10
    h = [0 for i in range(size)]
    for i in range(q):
        t, x = map(int, input().split())
        if t == 0:
            h = insert(h, size, x, 0)

        elif t == 1:
            h = search(h, size, x, 0)


if __name__ == '__main__':
    main()
