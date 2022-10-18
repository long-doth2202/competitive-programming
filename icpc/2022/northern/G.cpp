#include <bits/stdc++.h>
using namespace std;

const int N = (int) 5e5 + 5;
const long long MOD = (long long) 1e9 + 7;

int test;
int n;
string str;
long long a[N];
long long s[N];
long long ss[N];
long long f[N];
long long t[N];

void reset() {
  for (int i = 0; i <= n + 1; i++) a[i] = s[i] = f[i] = ss[i] = t[i] = 0;
}

int main() {
  cin >> test;
  for (int i = 1; i <= test; i++) {
    cin >> str;
    n = str.size();
    for (int i = 1; i <= n; i++) {
      a[i] = str[i - 1] - 'a' + 1;
      s[i] = (s[i - 1] + a[i]) % MOD;
      ss[i] = (ss[i - 1] + s[i]) % MOD;
      t[i] = (t[i - 1] + 1LL * i * s[i] % MOD) % MOD;
    }

    //for (int i = 1; i <= n; i++) cout << a[i] << " "; cout << endl;

    long long ans = 0;
    for (int j = 1; j <= n; j++) {
      long long tmp1 = (1LL * j * s[j] % MOD * j % MOD + t[j - 1] + MOD) % MOD;
      long long tmp2 = (1LL * s[j] * j * (j - 1) / 2 % MOD) % MOD;
      long long tmp3 = 1LL * j * ss[j - 1] % MOD;
      ans = (ans + tmp1) % MOD;
      ans = (ans - tmp2 + MOD) % MOD;
      ans = (ans - tmp3 + MOD) % MOD;
    }
    cout << ans << "\n";
    reset();
  }

  return 0;
}
