def solution(brown, yellow):
    answer = []
    total=brown+yellow
    for i in range(1,total+1):
        if total%i==0:
            a=total//i
            b=total//a
            if (a-2) * (b-2)==yellow:
                return [a,b]
    
    return answer