// 애너그램 만들기
#include <bits/stdc++.h>
#include<cstdlib>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string str1;
	string str2;

	int cmp[26];
	int ans = 0;
	fill(cmp, cmp + 26, 0);
	
	cin >> str1 >> str2;

	for (int i = 0; i < str1.length(); i++) cmp[str1[i] - 'a']++;
	for (int i = 0; i < str2.length(); i++) cmp[str2[i] - 'a']--;
	
	for (int i = 0; i < 26; i++) {
		abs += abs(cmp[i])
	}
	cout << ans;
	return 0;
}