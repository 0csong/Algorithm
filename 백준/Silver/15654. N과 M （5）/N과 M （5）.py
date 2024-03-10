import sys
input=sys.stdin.readline

n,m=map(int, input().split())
num=list(map(int,input().split()))
num=sorted(num)
chk=[False]*(n+1)
result=[]
def dfs(x,num):
    if len(result)==m:
        print(*result)
        return

    for i,ele in enumerate(num):
        if chk[i]==False:
            chk[i]=True
            result.append(ele)
            dfs(x+1,num)
            chk[i]=False
            result.pop()
dfs(0,num)
