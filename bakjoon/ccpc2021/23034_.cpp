// https://www.acmicpc.net/problem/23034
// 더이상 갈곳이 없을때까지 다익스트라
// 각각에서 출발했을때의 최소 값을 찾아서.ㅇㅇ기록
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <tuple>
using namespace std; 

int edges[1000][1000];

int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	int N, M, A,B,C, Q, X,Y, T= 0;
	bool is_unions[1000] = {false};
	tuple<int,int,int> cur;
	priority_queue<tuple<int,int,int>, 
			vector<tuple<int,int,int>>, greater<tuple<int,int,int>>> pq;
	cin >> N >> M;

	for (int i = 0; i < M; i++){
		cin >> A >> B >> C;
		edges[A - 1][B - 1] = C;
		edges[B - 1][A - 1] = C;
	}

	
	

	cin >> Q;
	for (int i = 0; i < Q; i++){
		T = 0;
		cin >> X >> Y;
		X-= 1;
		Y-= 1;
		fill(is_unions, &is_unions[1000], false);
		is_unions[X] = 1;
		is_unions[Y] = 1;
		for(int nxt = 0; nxt < N; nxt++){
			if(edges[X][nxt] > 0 && !is_unions[nxt]){
				pq.push({edges[X][nxt],X, nxt});
			}
			if(edges[Y][nxt] > 0 && !is_unions[nxt]){
				pq.push({edges[Y][nxt],Y, nxt});
			}
		}
		
		while(pq.size()){
			cur = pq.top();
			pq.pop();
			C = get<0>(cur);
			A = get<1>(cur);
			B = get<2>(cur);	
			
			if(is_unions[B]){
				continue;
			}
			is_unions[B] = 1;
			T+= C;
			for(int nxt = 0; nxt < N; nxt++){
				if(edges[B][nxt] > 0 && !is_unions[nxt]){
					pq.push({edges[B][nxt],B, nxt});
				}
			}
		}
		cout << T << '\n';
	}
}