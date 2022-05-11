#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

pair<int,int> values[100];
int cache[100005] = {0};
int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);
	int N, K;
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> values[i].first >> values[i].second;
	}
	for (int i = 0; i < N; i++) {
		vector<int> v;
		for (int weight = 0; weight < K - values[i].first + 1; weight++) {
			if (cache[weight] == 0 || cache[weight + values[i].first] > cache[weight] + values[i].second) {
				continue;
			}
			v.push_back(weight);
		}
		reverse(v.begin(), v.end());
		for (int weight: v) {
			cache[weight + values[i].first] = max(cache[weight + values[i].first],cache[weight] + values[i].second);
		}
		if (values[i].first > K) continue;
		cache[values[i].first] = max(cache[values[i].first], values[i].second);
	}
	int max_val = 0;
	for (int i = 0; i < K + 1; i++) {
		max_val = max(max_val, cache[i]);
	}
	cout << max_val;
	return 0;
}
