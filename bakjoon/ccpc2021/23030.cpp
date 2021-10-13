// https://www.acmicpc.net/problem/23030

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int shortest_path(int T,int U1,int U2,int V1,int V2, int* nodes_per_line, pair<int,int> edges[][51]){
	priority_queue<tuple<int,int,int>,  vector<tuple<int,int,int>>, greater<tuple<int,int,int>>> p_q;
	bool visited[11][51] = {0};
	int cur_line, cur_node, cur_val;

	p_q.push(make_tuple(0,U1, U2));
	while(p_q.size()){
		cur_val = get<0>(p_q.top());
		cur_line = get<1>(p_q.top()); 
		cur_node = get<2>(p_q.top());
		p_q.pop();
		if (cur_line == V1 && cur_node == V2){
			return cur_val;
		}
		if (visited[cur_line][cur_node]){
			continue;
		}
		visited[cur_line][cur_node] = 1;
		
		if(edges[cur_line][cur_node].first != -1 && visited[edges[cur_line][cur_node].first][edges[cur_line][cur_node].second] == 0){
			p_q.push(make_tuple(cur_val + T, 
				edges[cur_line][cur_node].first, edges[cur_line][cur_node].second));
		}
		if(cur_node < nodes_per_line[cur_line] && !visited[cur_line][cur_node + 1]){
			p_q.push(make_tuple(cur_val + 1, cur_line, cur_node +1));
		}
		

		if(cur_node > 0 && !visited[cur_line][cur_node -1]){
			p_q.push(make_tuple(cur_val + 1, cur_line, cur_node-1));
		}
		
	}
	return 0;
}

int main() {
	int N, M, K, nodes_per_line[11]; 
	pair<int,int> edges[11][51];
	for (int i = 0; i < 11; i++){
		for(int j = 0; j < 51; j++){
			edges[i][j].first = -1;
			edges[i][j].second = -1;
		}
	}
	cin >> N;
	for (int i = 0; i < N; i++){
		cin >> nodes_per_line[i];
	}

	cin >> M;
	int P1,P2,Q1,Q2;
	for (int i = 0; i < M; i++){
		cin >> P1 >> P2 >> Q1 >> Q2;
		edges[P1-1][P2-1] = {Q1-1,Q2-1};
		edges[Q1-1][Q2-1] = {P1-1,P2-1};
	}

	cin >> K;
	int T,U1,U2,V1,V2;
	for (int i = 0; i < K; i++){
		cin >> T >> U1 >> U2 >> V1 >> V2;
		cout << shortest_path(T, U1-1,U2-1,V1-1,V2-1 ,nodes_per_line, edges) << endl;
	}
	
}