def solution(stockPrices, k):
    result = 0
    bef = stockPrices[0]
    cur_count = 1
    
    if cur_count >= k:
        result += 1
    for cur in stockPrices[1:]:
        if cur > bef:
            cur_count += 1
        else:
            cur_count = 1
        bef = cur
        if cur_count >= k:
            result += 1
    return result