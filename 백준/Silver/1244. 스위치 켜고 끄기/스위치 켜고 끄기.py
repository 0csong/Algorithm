import sys
input=sys.stdin.readline
sw=int(input())
state=[-1]+list(map(int,input().split()))
student=int(input())

def change(num):
    if state[num] == 0:
        state[num] = 1
    else:
        state[num] = 0
    return

for _ in range(student):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, sw+1, num):
            change(i)
    else:
        change(num)
        for k in range(sw // 2):
            if num + k > sw or num - k < 1:
                break
            if state[num + k] == state[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

for i in range(1, sw+1):
    print(state[i], end = " ")
    if i % 20 == 0 :
        print()