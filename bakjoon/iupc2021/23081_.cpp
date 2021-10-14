#include <iostream>
#include <string>
using namespace std;


void renew_result(int continuous_white, int row, int col, int result[][500]){
    result[row][col] += continuous_white;
}

void find_possible_white(int cur, bool& black_checker, int& continuous_white
    ,int row, int col, int result[][500], int black_start[]){
    if (cur == 0){
        if(black_checker == 1){
            renew_result(continuous_white, row, col,result);
        }
        black_checker = 0;
        continuous_white = 0;
        black_start[0] =row;
        black_start[1] = col;
    }
    else if(cur == 1){
        if(black_checker == 0){
            renew_result(continuous_white, black_start[0],black_start[1],result);
            black_checker = -1;
        }
        else{
            black_checker = 1;
        }
        
        continuous_white = 0;
    }
    else{
        continuous_white += 1;
    }
}

int main() {
    int N, board[500][500] = {0};
    char tmp;
    cin >> N;
    for(int row = 0; row < N; row++){
        for(int col = 0; col < N; col++){
            cin >> tmp;
            if(tmp == 'B')
            {
                board[row][col] = 1;
            }
            else if(tmp == 'W')
            {
                board[row][col] = 2;
            }
        }
    }
    
    int continuous_white,cur, result[500][500] = {0}, black_start[2];
    bool black_checker;
    for(int row = 0; row < N; row++){
        continuous_white = 0;
        black_checker = -1;
        black_start[0] = 0;
        black_start[1] = 1;
        for(int col = 0; col < N; col++){
            cur = board[row][col];
            find_possible_white(cur, black_checker, continuous_white, 
                row,col,result, black_start);
        }
    }
    
    
    for(int col = 0; col < N; col++){
        continuous_white = 0;
        black_checker = -1;
        black_start[0] = 0;
        black_start[1] = 1;
        for(int row = 0; row < N; row++){
            cur = board[row][col];
            find_possible_white(cur, black_checker, continuous_white, 
                row,col,result, black_start);
        }
    }
    
    // /이방향으로
    int col, row;
    for(int count = 0; count < N; count ++){
        continuous_white = 0;
        black_checker = -1;
        col = 0;
        row = count;
        black_start[0] = 0;
        black_start[1] = 1;
        for(int diagonal = 0; diagonal < count + 1; diagonal++){
            cur = board[row][col];
            find_possible_white(cur, black_checker, continuous_white, 
                row,col,result, black_start);
            col += 1;
            row -= 1;
        }
    }

    for(int count = 1; count < N; count ++){
        continuous_white = 0;
        black_checker = -1;
        col = count;
        row = N- 1;
        black_start[0] = 0;
        black_start[1] = 1;
        for(int diagonal = 0; diagonal < count + 1; diagonal++){
            cur = board[row][col];
            find_possible_white(cur, black_checker, continuous_white, 
                row,col,result, black_start);
            col += 1;
            row -= 1;
        }
    }

    // \이방향으로
    for(int count = 0; count < N; count ++){
        continuous_white = 0;
        black_checker = -1;
        col = 0;
        row = N - 1 - count;
        black_start[0] = 0;
        black_start[1] = 1;
        for(int diagonal = 0; diagonal < count + 1; diagonal++){
            cur = board[row][col];
            find_possible_white(cur, black_checker, continuous_white, 
                row,col,result, black_start);
            col += 1;
            row += 1;
        }
    }

    for(int count = 1; count < N; count ++){
        continuous_white = 0;
        black_checker = -1;
        col = count;
        row = 0;
        black_start[0] = 0;
        black_start[1] = 1;
        for(int diagonal = 0; diagonal < count + 1; diagonal++){
            cur = board[row][col];
            find_possible_white(cur, black_checker, continuous_white, 
                row,col,result, black_start);
            col += 1;
            row += 1;
        }
    }

    int result_r, result_c, max_rev = 0;
    for(int r = 0; r < N; r++){
        for(int c = 0; c < N; c++){
            cur = result[r][c];
            if(cur > max_rev){
                max_rev = cur;
                result_r = r;
                result_c = c;

            }
            else if(cur == max_rev){
                if(c < result_c){
                    result_c = c;
                    result_r = r;
                }
                else if(c == result_c && r < result_r){
                    result_r = r;
                }
            }
        }
    }
    if (max_rev == 0){
        cout << "PASS";
    }
    else{
        cout << result_c << ' '<<result_r << '\n' << max_rev;
    }
    
};