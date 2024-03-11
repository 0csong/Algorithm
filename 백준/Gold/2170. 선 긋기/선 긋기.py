import sys
input=sys.stdin.readline
n=int(input())
cord=[list(map(int, input().split())) for _ in range(n)]
cord.sort(key=lambda x:x[0])
cur_start=cord[0][0]
cur_end=cord[0][1]
length=0
for start,end in cord[1:]:#이어져있는 부분에 대해서 합을 구함
    if start>=cur_end:
        length+=(cur_end-cur_start)
        cur_start=start
    cur_end=max(cur_end,end)

length+=(cur_end-cur_start)

print(length)
