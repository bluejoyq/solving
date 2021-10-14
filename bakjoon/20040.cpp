#include <iostream>

using namespace std;

int find_parent(int parents[],int cur){
    if(parents[cur] == cur){
        return cur;
    }
    parents[cur] = find_parent(parents,parents[cur]);
    return parents[cur];
}

int union_parents(int ranks[],int parents[], int a, int b){
    int a_root = find_parent(parents, a),
        b_root = find_parent(parents, b);
    if (a_root == b_root)
        return false;
    
    if(ranks[a_root] < ranks[b_root]){
        parents[a_root] = b_root;
    }
    else if(ranks[a_root] > ranks[b_root]){
        parents[b_root] = a_root;
    }
    else {
        parents[b_root] = a_root;
        ranks[a_root] += 1; 
    }

    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N,M,a,b, result = 0,*parents = new int[N], *ranks = new int[N];
    // 동적할당일 때 시간이 줄어드나?
    cin >> N >> M;
    for(int i = 0; i < N; i++){
        parents[i] = i;
        ranks[i] = 0;
    }

    for(int i = 0; i < M; i++){
        cin >> a >> b;
        if(union_parents(ranks, parents,a,b))
            continue;
        
        if(result == 0)
            result = i + 1;
            break;
    }
    cout << result;
}