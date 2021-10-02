// https://www.acmicpc.net/problem/2225
// 

#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int N, K,  cache[201][402]= {0};
	cin >> N >> K;
	// 최대가 400이니까~
	
	for(int cur = 0; cur < N+1; cur++){
		cache[1][cur] = 1;
	}
	for(int selected = 2; selected < K + 1; selected++){
		for(int cur = 0; cur < N+1; cur++){
			for(int bef = 0; bef < N+1; bef++){
				cache[selected][bef + cur] = (cache[selected][bef + cur] + cache[selected - 1][bef]) % 1000000000;
			}
		}
	}
	cout << cache[K][N];
 	return 0;
}