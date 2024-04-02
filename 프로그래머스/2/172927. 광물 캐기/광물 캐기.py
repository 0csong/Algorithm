def solution(picks, minerals):
    answer = 0
    mineralSort = []

    able = min(sum(picks) * 5, len(minerals))
    dia, iron, stone = 0, 0, 0

    for i in range(able):
        if minerals[i] == 'diamond':
            dia += 1
        elif minerals[i] == 'iron':
            iron += 1
        elif minerals[i] == 'stone':
            stone += 1
        
      
        if (i + 1) % 5 == 0 or i == able - 1:
            mineralSort.append((dia, iron, stone))
            dia, iron, stone = 0, 0, 0


    mineralSort.sort(key = lambda x : (x[0], x[1], x[2]), reverse = True)

    # 좋은 곡괭이를 먼저 사용
    i = 0
    for dia, iron, stone in mineralSort:
        # 해당 등급 곡괭이가 없으면 다음등급 곡괭이
        while picks[i] == 0:
            i += 1

        # 피로도 계산
        if i == 0:
            answer += (dia + iron + stone)
        elif i == 1:
            answer += (dia * 5 + iron + stone)
        elif i == 2:
            answer += (dia * 25 + iron * 5 + stone)

        # 곡괭이를 사용했으니 파괴
        picks[i] -= 1

    return answer