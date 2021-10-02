//https://www.acmicpc.net/problem/23029
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;

	int *values = new int[N];
	for(int i = 0; i < N; i++){
		cin >> values[i];
	}

	int cache[100002][2] = {0};
	
	for(int i = 0; i < N; i++){
		cache[i+1][0] = max({cache[i+1][0],cache[i][0], cache[i][1]});
		cache[i+1][1] = max({cache[i+1][1],cache[i][0] + values[i]});
		cache[i+2][0] = max({cache[i+2][0],cache[i][1] + int(values[i] / 2)} );
	}
	cout << max({cache[N][0], cache[N][1],cache[N-1][0], cache[N-1][1], cache[N+1][0]});
	delete[] values;
}