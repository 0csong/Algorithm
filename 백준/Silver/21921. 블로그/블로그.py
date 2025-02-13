import sys
input=sys.stdin.readline

n,x=map(int,input().split())
vistor=list(map(int,input().split()))

win=sum(vistor[:x])
max_vistor=win
max_cnt=1

for i in range(x,n):
    win-=vistor[i-x] #첫번째 인자 제거
    win+=vistor[i]

    if win == max_vistor:
        max_cnt+=1
    elif max_vistor<win:
        max_vistor=win
        max_cnt=1

if max_vistor==0:
    print('SAD')
else:
    print(max_vistor)
    print(max_cnt)