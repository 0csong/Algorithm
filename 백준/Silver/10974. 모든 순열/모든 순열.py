import sys
input=sys.stdin.readline
n=int(input())
num=[i+1 for i in range(n) ]
res=[]
def dfs():
    if len(res)==n:
        print(*res)
        return
    for i in range(n):
        if not num[i] in res:
            res.append(num[i])
            dfs()
            res.pop()

dfs()
