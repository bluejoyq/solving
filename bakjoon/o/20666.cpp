#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;
vector<pii> mobs[100005];
long long diffs[100005];
bool visited[100005];

struct cmp {
  bool operator()(pii a, pii b) {
    return a.first > b.first;
  }
};
int main() {
  cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
  priority_queue<pii, vector<pii>, cmp> pq;
  ll N, M, P, a, b, c, result = 0;
  cin >> N >> M;
  for (int i = 1; i < N + 1; i++) {
    cin >> diffs[i];
  }
  cin >> P;

  for (int i = 0; i < P; i++) {
    cin >> a >> b >> c;
    mobs[a].push_back({ b,c });
    diffs[b] += c;
  }
  for (int i = 1; i < N + 1; i++) {
    pq.push({ diffs[i], i });
  }
  int i = 0;
  while (i < M) {
    c = pq.top().first;
    a = pq.top().second;
    pq.pop();
    if (visited[a]) continue;
    visited[a] = true;
    for (auto k : mobs[a]) {
      diffs[k.first] -= k.second;
      pq.push({ diffs[k.first], k.first });
    }
    result = max(result, c);
    i += 1;
  }
  cout << result;
}