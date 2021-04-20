#BFS는 큐사용
from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue: #큐가빌때까지 반복
        v=queue.popleft()#큐에서 하나씩제거
        print(v,end=' ')
        for i in graph[v]: #i를 인덱스로 사용
            if not visited[i]:
                queue.append(i)
                visited[i]=True
graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],
      [3,4],[7],[2,6,8],[1,7]] 
visited=[False]*9 #모든 노드 방문 x로
bfs(graph,1,visited)
