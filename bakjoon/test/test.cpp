#include <iostream>

using namespace std;

// 2차원 행렬

int main() {
	int row_a, col_a, **matrix_a,
		row_b,col_b, **matrix_b;
	// 행렬 1 가로 세로 사이즈 입력.
	cin >> row_a >> col_a;
	// 행렬 1 초기화
	matrix_a = new int*[row_a];
	for(int r = 0; r< row_a;r++){
		matrix_a[r] = new int[col_a];
	}
	// 행렬 2 입력
	for(int r = 0; r < row_a; r++){
		for(int c = 0; c < col_a; c ++){
			cin >> matrix_a[r][c];
		}
	}

	// 행렬 2 가로 세로 사이즈 입력.
	cin >> row_b >> col_b;
	// 행렬 2 초기화
	matrix_b = new int*[row_b];
	for(int r = 0; r< row_b;r++){
		matrix_b[r] = new int[col_b];
	}
	// 행렬 2 입력
	for(int r = 0; r < row_b; r++){
		for(int c = 0; c < col_b; c ++){
			cin >> matrix_b[r][c];
		}
	}

	int **result;
	result = new int* [row_a];
	for(int r = 0; r< row_a;r++){
		result[r] = new int[col_b];
	}

	for(int r = 0; r < row_a; r++){
		for(int c = 0; c < col_b; c ++){
			result[r][c]= 0;
			for(int i = 0; i < row_b; i++){
				result[r][c] += matrix_a[r][i] * matrix_b[i][c];
			}
		}
	}

	for(int r = 0; r < row_a; r++){
		for(int c = 0; c < col_b; c ++){
			cout << result[r][c] << ' ';
		}
		cout << endl;
	}
	// delete 생략
}