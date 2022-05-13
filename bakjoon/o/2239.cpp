#include <iostream>
#include <algorithm>

using namespace std;

long long int cache[10005];
int values[105];
int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);
	int N, K;
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> values[i];
		if (values[i] > K + 1) continue;
		cache[values[i]] += 1;
		for (int val = 0; val < K; val++) {
			if (cache[val] == 0 || val + values[i] > K + 1) continue;
			cache[val + values[i]] = cache[val + values[i]] + cache[val];
		}
	}
	cout << cache[K];
}
