#include <iostream>
using namespace std;

int cache[1000003] = {0};

int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);
	int N;
	cin >> N;
	cache[0] = 1;
	for (int i = 0; i < N; i++) {
		cache[i + 2] += cache[i];
		cache[i + 1] += cache[i];
		cache[i + 2] %= 15746;
		cache[i + 1] %= 15746;
	}
	cout << cache[N];
	return 0;
}
