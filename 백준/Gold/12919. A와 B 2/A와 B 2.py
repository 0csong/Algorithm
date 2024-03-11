import sys
S=list(input())
T=list(input())
result=0
def dfs(t): # 문자열 T를 입력받아
    global result
    if t==S:
        result=1
        return
    if len(t)==0:
        return
    if t[-1]=='A': # 마지막이 A이면
        dfs(t[:-1]) # 제거해서 재귀
    if t[0]=='B': # 처음이 B이면
        dfs(t[1:][::-1]) # B제거하고, 뒤집어서 재귀
dfs(T)
print(result)