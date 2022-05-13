#include <iostream>
#include <queue>
#include <vector>
using namespace std;
typedef pair<int,int> pii;
bool visited[10005];
vector<pii> edges[10005];

int main() {
  int N,M;
  cin >> N >> M;
  for(int i = 0; i < M; i++){
    int A,B,C;
    cin >> A >> B >> C;
    edges[A].push_back({C,B});
    edges[B].push_back({C,A});
  }
  
  priority_queue<pii, vector<pii>, greater<pii>> pq;
  pq.push({0, 1});
  
  int counter = 0, result = 0;
  while(counter < N){
    pii cur = pq.top();
    pq.pop();
    if(visited[cur.second]) continue;
    visited[cur.second] = true;
    counter += 1;
    result += cur.first;
    for(pii nxt : edges[cur.second]){
      if(visited[nxt.second]) continue;
      pq.push({nxt.first, nxt.second});
    }
  }
  cout << result;
}