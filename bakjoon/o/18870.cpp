#include <iostream>
#include <utility>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	pair<int,int> *values = new pair<int,int>[N];
	int *results = new int[N];

	for(int i = 0; i < N; i++){
		cin >> values[i].first;
		values[i].second =i;
	}

	sort(values, values + N);
	results[values[0].second] = 0;
	for(int i = 1; i < N; i++){
		if(values[i].first == values[i-1].first){
			results[values[i].second] = results[values[i - 1].second];
		}
		else {
			results[values[i].second] = results[values[i - 1].second] + 1;
		}
	}

	for(int i = 0; i < N; i++){
		cout << results[i] << ' ';
	}

	delete[] values;
	delete[] results;
	return 0;
}