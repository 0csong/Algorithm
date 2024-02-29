import sys
from collections import deque
input=sys.stdin.readline

M,N,H=map(int,input().split())
graph=[[list(map(int, input().split())) for _ in range(N)]for _ in range(H)]
dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]


def bfs():
    while q:
        z,x,y=q.popleft()
        for i in range(6):
            nz=z+dz[i]
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and graph[nz][nx][ny]==0:
                graph[nz][nx][ny]=graph[z][x][y]+1
                q.append((nz,nx,ny))


q=deque()
# 먼저 1인 토마토를 다 넣어서 BFS를 시작함. 단순히 하나씩 넣게되면 중간에서 만나는 토마토를 계산하지 못함
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k]==1:
                q.append((i,j,k))
bfs()


max_days = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            max_days = max(max_days, graph[i][j][k])

print(max_days - 1)#시작일이 1이였음

