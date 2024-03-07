import sys
input=sys.stdin.readline

n=int(input())
money=list(map(int,input().split()))
m=int(input())
start,end=0,max(money)

while start<=end:
    mid=(start+end)//2
    total=0 #종 지출양
    for i in money:
        if i>mid:
            total+=mid #예산양
        else:
            total+=i #할당량

    if total<=m:#지출이 예산보다 작으면
        start=mid+1
    else:
        end= mid-1 # 지출이 예산보다 크면

print(end)
