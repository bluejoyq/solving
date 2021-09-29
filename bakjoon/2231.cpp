#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        int tmp = i;
        for(int j = 1; j <= i; j *= 10){
            tmp += (i % (j * 10)) / j;
        }
        //cout << tmp << endl;
        //cout << i << ' ' << tmp << endl;

        if (tmp == N) {
            cout << i;
            return 0;
        }
        
    }
    cout << 0;
    return 0;
}