// https://www.acmicpc.net/problem/23027
#include <iostream>
#include <string>
using namespace std;

int main() {
	bool a_checker = false, b_checker = false, c_checker = false;
	string S;
	cin >> S;
	for(int i = 0; i < S.length(); i++){
		if(S[i] == 'A'){
			a_checker = true;
		} 
		else if(S[i]== 'B'){
			b_checker = true;
		}
		else if(S[i] == 'C'){
			c_checker = true;
		}
	}

	if (a_checker){
		for(int i = 0; i < S.length(); i++){
			if(S[i] == 'F' || S[i] == 'D'||S[i] == 'C'||S[i] == 'B' ){
				S[i] = 'A';
			} 
		}
	}
	else if (b_checker) {
		for(int i = 0; i < S.length(); i++){
			if(S[i] == 'F' || S[i] == 'D'||S[i] == 'C'){
				S[i] = 'B';
			} 
		}
	}
	else if (c_checker) {
		for(int i = 0; i < S.length(); i++){
			if(S[i] == 'F' || S[i] == 'D'){
				S[i] = 'C';
			} 
		}
	}
	else {
		for(int i = 0; i < S.length(); i++){
			S[i] = 'A';
		}
	}
	cout << S;
}