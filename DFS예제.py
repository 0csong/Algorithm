def dfs(graph,v,visted):
    visted[v]=True
    print(v,end=' ') #end는 문장마지막에 뭘 넣을지 정할수잇음
    for i in graph[v]:
        if not visted[i]:
            dfs(graph,i,visted)

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],
      [3,4],[7],[2,6,8],[1,7]] #첫번째는 비워둔이유가 인덱스0인데 0이라는 노드가 없기에
visted=[False]*9
dfs(graph,1,visted)
#DFS는 스택사용

#visted[i]를 방문한것이였으면 true처리한다 하면
#if(visted[i])경우 이프문을 통과하게되어 이자체로 조건을 만들수있음
