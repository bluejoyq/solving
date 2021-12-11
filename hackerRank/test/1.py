import operator
a= [1,2,3,4]
b = [[1,2],[2,3],[3,4],[4,5]]

def trans_arr(arr): 
    # roates input arr
    return list(map(list,zip(*arr)))


print(trans_arr(a))