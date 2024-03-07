import sys
input=sys.stdin.readline
from collections import deque
n=int(input())

q=deque()
for i in range(1,n+1):
    q.append(i)

for i in range(n-1):
    q.popleft()
    q.append(q[0])
    q.popleft()
print(q[0])

