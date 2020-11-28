#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; ++i)

int main() {
  int n;
  cin >> n;
  vector<int> A(n);
  rep(i, n) cin >> A[i];
  sort(A.begin(), A.end())
  int flag = 0
  while(flag == 0) {
      int tmp = A[0]
      int max_a = A[n-1]
      for (int i=n, i)
  }
  for (int i = 1; i < n; ++i) {
    for (int j = max(i - k, 0); j < i; ++j) {
      dp[i] = min(dp[i], dp[j] + abs(h[i] - h[j]));
    }
  }
  rep(i, n) cout << A[i];
  cout << dp[n - 1] << endl;
}

n
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