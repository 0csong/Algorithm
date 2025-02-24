import sys
input=sys.stdin.readline

n,k=map(int,input().split())
eat = list(input().strip())
cnt=0
for i in range(n): #사람 탐색
    if eat[i]=='P': #사람을 찾았다면
        for j in range(i-k,i+k+1): #햄버거를 찾자
            if 0<=j<n and eat[j]=='H': #햄버거를 찾았고, 그 햄버거가 식탁범위 안에 있다면(햄버거는 왼쪽부터)
                eat[j]=0 #햄버거를 먹자
                cnt+=1 #가능수 1 증가
                break #다시 사람을 찾아보자!
print(cnt)