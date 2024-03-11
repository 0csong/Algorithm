import sys
import heapq
input=sys.stdin.readline
n=int(input())
time=[list(map(int,input().split())) for _ in range(n)]

time.sort(key=lambda x:(x[0],x[1])) #시작 시간부터 정렬을 진행함, 이후 종료시간 정렬
heap=[time[0][1]] #먼저 종료시간을 넣음

for i in range(1,n): # 이미 heap에 0은 들어갔으니 1부터
    if heap[0]<=time[i][0]: #만약 종료시간보다 시작시간이 크다면 강의를 이어서 진행가능, 따라서 pop
        heapq.heappop(heap)
    heapq.heappush(heap,time[i][1]) # 현재 종료시간보다 시작시간이 작다면 동시에 진행 불가능, 따라서 push
print(len(heap))

