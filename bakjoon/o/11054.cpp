#include <iostream>
#include <algorithm>
using namespace std;

int cache[1001 * 2] = {0};
int values[1001] = {0};
int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> values[i];
	}
	for (int i = 0; i < N - 1; i++) {
		for (int j = i + 1; j < N; j++) {
			if (values[j] > values[i]) {
				cache[j] = max(cache[j], cache[i] + 1);
			}
			if (values[j] < values[i]) {
				cache[j + 1001] = max({ cache[j + 1001], cache[i] + 1, cache[i + 1001] +1 });
			}
		}
	}
	cout << *max_element(cache , cache +2002) + 1;
	return 0;
}
