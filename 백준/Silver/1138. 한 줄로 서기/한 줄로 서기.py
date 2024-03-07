import sys
input=sys.stdin.readline

n=int(input())
person=list(map(int, input().split()))

answer=[0]*n
for i in range(n):#각 사람에 대해 반복
    # 자신의 왼쪽에 있는 키 큰 사람의 수
    cnt = 0
    for j in range(n):# 나열할 위치를 찾기 위해 사용
        # 자신의 왼쪽에 있는 키 큰 사람의 수와 맞고, 그 자리에 아무도 없다면
        if cnt == person[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        # 자리에 아무도 없다면 자신의 왼쪽에 키 큰 사람의 수를 카운트
        elif answer[j] == 0:
            cnt += 1
print(*answer)