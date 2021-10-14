#include <iostream>
#include <string>
using namespace std;

int main() {
    int K, len;
    string S,result = "";
    cin >> K;
    cin >> S;
    len = S.length();
    for(int i = 0; i < len; i += K){
        result += S[i];
    }
    cout << result;
}