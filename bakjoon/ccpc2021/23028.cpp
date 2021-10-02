// https://www.acmicpc.net/problem/23028

#include <iostream>
using namespace std;

int main() {
	const int ALL_NEED = 130, PRIMARY_NEED = 66;
	int N,A,B,X,Y,
		primarys[10], subs[10];
	
	cin >> N >> A >> B;
	for(int i = 0; i < 10; i++){
		cin >> primarys[i] >> subs[i];
	}
	
	int cur = 0, primary_num;
	while(cur < 8 - N) {
		primary_num = min(6,primarys[cur]);
		A += primary_num * 3;
		B += primary_num * 3;
		B += min(6- primary_num, subs[cur]) * 3;
		cur += 1;

		if (A >= PRIMARY_NEED && B >= ALL_NEED){
			cout << "Nice";
			return 0;
		}
	}
	cout << "Nae ga wae";
} 
