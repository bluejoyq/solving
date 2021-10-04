// https://www.acmicpc.net/problem/23034
// 더이상 갈곳이 없을때까지 다익스트라
// 각각에서 출발했을때의 최소 값을 찾아서.ㅇㅇ기록

#include <iostream>
#include <vector>
using namespace std;


int find_best(int start,int cache[1000][1000]){
	int cur;
	bool visited[1000] = {0};
	vector<int> findings = {start};
	visited[start] = 1;
	while(findings.size()){
		cur = findings.back();
		findings.pop_back();
		
	}
}

int main() {
	int N, M, A,B,C, Q, edges[1000][1000] = {-1}, cache[1000][1000] = {0};
	cin >> N >> M;
	
	for (int i = 0; i < M; i++){
		cin >> A >> B >> C;
		edges[A][B] = C;
		edges[B][A] = C;
	}
	for (int start = 0; start < N; start++){

	}
	// 한번 출발하는거에서 온방향만 빼면 거기서의 최단거리 아닌감?
}