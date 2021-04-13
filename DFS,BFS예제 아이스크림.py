#n*m의 얼음틀 구멍이 뚫리면 0, 칸막이있으면 1,
#구멍이 뚫려있는 부분끼리 상하좌우 붙어있으면 연결되어잇음
#얼음틀이 주어졌을때 생성되는 총 아이스크림개수구하는 프로그램
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0  틀모양
#입력은 N과 M, 두번째 줄부터 N+1번째 줄까지 얼음틀 형태
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1#해당노드 방문처리
        #상하좌우 재귀 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True#방문됐을경우 True
    return False #예상치 못해서 종료될경우 

n,m=map(int,input().split())# n입력후 한칸띄고 m

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))#0이나 1 붙여서 입력, 입력한값을 리스트에 저장

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:#해당노드가 방문되엇다면
            result+=1  #결과 +1 이것은 아이스크림
print(dfs(n,m))#마지막에는 다 방문하면 DFs는 False반환
print(result)   
