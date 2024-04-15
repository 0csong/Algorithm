from itertools import combinations
def solution(number):
    # 조합으로 3개 짜기
    answer = 0
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1
    return answer