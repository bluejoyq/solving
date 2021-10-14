#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int N, three_max, three_pos_max, cur;
    char result[20];
    cin >> N;
    cur = 1;
    three_pos_max = 1;
    while(N > cur){
        three_pos_max+= 1;
        cur = int((pow(3,three_pos_max) - 1) / 2);
        
    }
    cout << three_pos_max;

    for(int i = three_pos_max; i > -1; i--){
        cur = pow(3, i);
        if(N > cur){
            N -= cur;
        } 
    }
}