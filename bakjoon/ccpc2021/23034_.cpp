// https://www.acmicpc.net/problem/23034
// 더이상 갈곳이 없을때까지 다익스트라
// 각각에서 출발했을때의 최소 값을 찾아서.ㅇㅇ기록
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int find_parent(int parents[], int cur){
	if(parents[cur] == cur){
		return cur;
	}
	parents[cur] = find_parent(parents, parents[cur]);
	return parents[cur];
}

void union_parents(int ranks[], int parents[], int a, int b){
	int a_root = find_parent(parents, a),
		b_root = find_parent(parents, b);

	if(a_root == b_root){
		return ;
	}

	if(ranks[a_root] < ranks[b_root]){
		parents[a_root] = b_root;
	}
	else if(ranks[a_root] > ranks[b_root]){
		parents[b_root] = a_root;
	}
	else{
		parents[b_root] = a_root;
		ranks[a_root] += 1;
	}
}

bool is_same(int parents[], int a, int b){
	int a_root = find_parent(parents, a),
		b_root = find_parent(parents, b);
	if(a_root == b_root)
		return true;
	return false;
}
int edges[1000][1000], cache[1000][1000];
int main() {
	int N, M, A,B,C, Q;
	cout << edges << ' '<<&edges[1000];
	//fill(edges, &edges[1000], -1);
	//fill(cache, &cache[1000], -1);
	cin >> N >> M;
	
	for (int i = 0; i < M; i++){
		cin >> A >> B >> C;
		edges[A][B] = C;
		edges[B][A] = C;
	}
	
	cin >> Q;
	for (int i = 0; i < Q; i++){
		
	}
	// 한번 출발하는거에서 온방향만 빼면 거기서의 최단거리 아닌감?
}