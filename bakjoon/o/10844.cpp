#include <iostream>
#include <algorithm>
using namespace std;

int cache[105][10] = {0};
int MAX = 1000000000;
int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);
	int N, result = 0;
	cin >> N;
	for (int i = 1; i < 10; i++) {
		cache[0][i] = 1;
	}
	for (int i = 0; i < N; i++){
		cache[i + 1][1] = (cache[i+1][1] + cache[i][0]) % MAX;
		cache[i + 1][8] = (cache[i + 1][8] + cache[i][9]) % MAX;
		for (int j = 1; j < 9; j++) {
			cache[i + 1][j - 1] = (cache[i + 1][j - 1] + cache[i][j]) % MAX;
			cache[i + 1][j + 1] = (cache[i + 1][j + 1] + cache[i][j]) % MAX;
		}
	}
	for (int i = 0; i < 10; i++) {
		result = (result +cache[N-1][i]) % MAX;
	}
	cout << result;
}
