def solution(cakes, cut_rows, cut_columns):
    def search_kinds(old_cut_row, cut_row, old_cut_col, cut_col):
        kinds = {}
        for r in range(old_cut_row, cut_row):
            for c in range(old_cut_col, cut_col):
                cur = cakes[r][c]
                kinds[cur] = 1
        return len(kinds)
    
    answer = 0
    cut_rows.append(len(cakes))
    cut_columns.append(len(cakes[0]))
    old_cut_row = 0
    old_cut_col = 0
    
    for cut_row in cut_rows:
        old_cut_col = 0
        for cut_col in cut_columns:
            kinds = {}
            
            tmp = search_kinds(old_cut_row, cut_row, old_cut_col, cut_col)
            answer = max(tmp, answer)
            old_cut_col = cut_col
            
        old_cut_row = cut_row
    return answer