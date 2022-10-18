#include <bits/stdc++.h>

using namespace std;

const int N = (2 * 1e5) + 5;

struct Query {
  string type;
  int x;
} query[N];

int n;
int q;
map <int, int> fw;
int rev[N];

void upd(int x, int v) {
  for (x; x <= n; x += x & -x) fw[x] += v;
}

int get(int x) {
  int res = 0;
  for (x; x >= 1; x -= x & -x) res += fw[x];
  return res;
}

int main() {
  cin >> q;
  for (int i = 1; i <= q; i++) {
      cin >> query[i].type;
      if (query[i].type != "MEDIAN") cin >> query[i].x;
  }
  vector <int> zip;
  for (int i = 1; i <= q; i++)
    if (query[i].type != "MEDIAN") zip.push_back(query[i].x);
  sort(zip.begin(), zip.end());
  zip.resize(distance(zip.begin(), unique(zip.begin(), zip.end())));
  n = zip.size() + 1;

  for (int i = 1; i <= q; i++) {
    if (query[i].type == "MEDIAN") continue;
    int t = lower_bound(zip.begin(), zip.end(), query[i].x) - zip.begin() + 1;
    rev[t] = query[i].x;
   // cout << t << " " <<  query[i].x << endl;
    query[i].x = t;
  }

 // cout << endl;

  for (int i = 1; i <= q; i++) {
    if (query[i].type == "IN") {
        upd(query[i].x, 1);
    } else if (query[i].type == "OUT") {
        upd(query[i].x, -1);
    }else {
        int cnt = get(n);
        if (cnt % 2 == 0) {
          int res1 = -1, res2 = -1, mid, left = 1, right = n;
          while (left <= right) {
            mid = (left + right) >> 1;
            if (get(mid) >= cnt / 2) {
              res1 = mid;
              right = mid - 1;
            } else left = mid + 1;
          }

          left = 1; right = n;
          while (left <= right) {
            mid = (left + right) >> 1;
            if (get(mid) >= cnt / 2 + 1) {
              res2 = mid;
              right = mid - 1;
            } else left = mid + 1;
          }
          res1 = rev[res1];
          res2 = rev[res2];
          if ((res1 + res2) % 2 == 0) {
            cout << (res1 + res2) / 2 << "\n";
          } else {
            cout <<  (res1 + res2) / 2 << ".5\n";
          }
         // cout << fixed << setprecision(1) << (double(res1) + (res2 * 1.0)) / 2.0 << "\n";
        } else {

          int res = -1, mid, left = 1, right = n;
          while (left <= right) {
            mid = (left + right) >> 1;
            if (get(mid) >= (cnt + 1) / 2) {
              res = mid;
              right = mid - 1;
            } else left = mid + 1;
          }

       //   cout << res << endl;
          res = rev[res];
          cout << res << "\n";
        }

    }
  }

  return 0;
}


/*
22
IN 1
MEDIAN
IN 2
MEDIAN
IN 3
MEDIAN
IN 4
MEDIAN
IN 5
MEDIAN
OUT 1
MEDIAN
IN 6
MEDIAN
OUT 2
MEDIAN
IN 7
MEDIAN
OUT 5
MEDIAN
IN 8
MEDIAN
*/
