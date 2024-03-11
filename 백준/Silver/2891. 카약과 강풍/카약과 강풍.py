n, s, r = map(int, input().split())
damaged = set(map(int, input().split()))
extra = set(map(int, input().split()))

# 자신의 여분의 카약으로 손상된 카약을 대체할 수 있는 팀 처리
intersect = damaged & extra
damaged -= intersect
extra -= intersect

# 여분의 카약을 빌려줄 수 있는 경우 처리
for e in list(extra):
    if e - 1 in damaged:
        damaged.remove(e - 1)
    elif e + 1 in damaged:
        damaged.remove(e + 1)
        extra.remove(e)

# 출발하지 못하는 팀의 수 출력
print(len(damaged))
