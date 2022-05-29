from typing import List, Deque


def is_prime_number(x):
    if x < 2:
        return 0
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1


A: int = int(input())
B: int = int(input())
N = 18
is_prime: List[int] = [is_prime_number(i) for i in range(N + 1)]


def do_round(percent: int) -> int:
    result_denom = 1

    cur_scores = [0 for i in range(N + 2)]
    cur_scores[0] = 100
    for i in range(N):
        new_scores = [0 for i in range(N + 2)]
        for goal in range(N + 1):
            denom = cur_scores[goal]
            new_scores[goal + 1] += percent * denom
            new_scores[goal] += (100 - percent) * denom
        cur_scores = new_scores
    for goal in range(N + 1):
        if is_prime[goal]:
            continue
        result_denom += cur_scores[goal]
    return result_denom

    # 적어도 한 팀이 골을 소수? = 전체 - 모두가 소수 아님


a_d = do_round(A)
b_d = do_round(B)

print(1 - (a_d * b_d) / (100 ** (2 * N + 2)))
