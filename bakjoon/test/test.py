card_num, max_num = map(int, input().split())

# map(func, sequence) : 주어진 시퀀스에 함수 적용
# list(sequence) : 시퀀스를 리스트로
card = list(map(int,input().split()))

max_result = 0
# 기존 코드는 cards Permutaions 3을 하는데
# cards Combinations 3만해도 됨
for i in range(card_num - 2):
    for j in range(i+1, card_num - 1):
        for k in range(j+1, card_num):
            sum_num = card[i]+card[j]+card[k]
            if sum_num <= max_num:
                # 이거는 어차피 if문이 있어 선택이긴한데 
                # if문으로 꼭 비교해야하는 경우가 아니면 max 처리
                max_result = max(max_result,sum_num)

print(max_result)
