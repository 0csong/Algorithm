def solution(n):
    answer = 0

    
    #1부터 시작해서 연속된 숫자로 더해나감
    for i in range(1,n+1):
        sum = 0
        #i부터 시작 i가 4라면 4+5+6+....
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer+=1
                break
            elif sum >n:
                break 
    
    return answer