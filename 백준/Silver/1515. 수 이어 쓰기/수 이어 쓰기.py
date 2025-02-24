import sys
input=sys.stdin.readline

num=list(input().strip())
n=0
idx=0
while True:
    n+=1
    for s in str(n): # n이 100이라면 s는 1, 0,0
        if num[idx]==s:
            idx+=1
            if idx>=len(num):
                print(n)
                exit()
