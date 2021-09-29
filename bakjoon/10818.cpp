#include <iostream>

using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, tmp;
    std::cin >> N;
    int min_value = 876543210;
    int max_value = -876543210;
    for(int i = 0; i < N; i++){
        std::cin >> tmp;
        min_value = std::min(tmp, min_value);
        max_value = std::max(tmp, max_value);
    }

    std::cout << min_value << ' ' << max_value;
    return 0;
}