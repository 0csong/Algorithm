n=int(input()) 
x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]    
            
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x=nx
    y=ny

print(x,y)    

#n*n차원 행렬에서 주인공위치 1,1 
#알파벳 입력시이동 하나 이동불가능하면 멈춤
#마지막 위치 print
