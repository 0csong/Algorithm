#괴물이 잇는곳은 0,없으면 1
#동빈이 위치는 1,1 탈출을 위해 움직여야하는 최소 칸은?
#출구는 n,m에 존재
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue: #큐가빌때까지 반복
        x,y=queue.popleft()
        for i in range(4):#이동방향이 4개
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:#그래프 벗어날경우 무시
                continue
            if graph[nx][ny]==0: #벽인경우 무시
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1#노드값을 증가시켜 최소칸수를 만듬
                queue.append((nx,ny))
    return graph[n-1][m-1]#가장 오른쪽아래
   
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0] #상하좌우
dy=[0,0,-1,1]
print(bfs(0,0))   