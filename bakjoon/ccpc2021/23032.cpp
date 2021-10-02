// https://www.acmicpc.net/problem/23032
#include <iostream>

using namespace std;

int main(){
	int  N, 
		result = 0,	min_sum = 1e9, differ,
		left_sum, right_sum, left, right, 
		values[2002], square_sum[2002] = {0};

	cin >> N;
	for(int i = 0; i < N; i ++){
		cin >> values[i]; 
		square_sum[i + 1] = square_sum[i] + values[i]; 
	}

	
	for(int contour = 1; contour < N; contour++){
		left = contour - 1;
		right = contour + 1;

		while(left > -1 && right < N + 1){
			left_sum = square_sum[contour] - square_sum[left];
			right_sum = square_sum[right] - square_sum[contour];
			differ = abs(left_sum - right_sum);
			if (min_sum  > differ) {
				min_sum = differ;
				result = left_sum + right_sum;
				
			} 
			else if(min_sum == differ) {
				result = max(result, left_sum + right_sum);
			}
			
			if (left_sum > right_sum){
				if(right == N){
					break;
				}
				right += 1;
			} else {
				if(left == 0){
					break;
				}
				left -= 1;
			}

		}
	}
	cout << result;
}	