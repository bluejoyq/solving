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
    pair<int,int> values[N];
    int results[N];

    for(int i = 0; i < N; i++){
        cin >> values[i].first;
        values[i].second = values[i].first;
    }

    sort(values, values + N);
    

    return 0;
}