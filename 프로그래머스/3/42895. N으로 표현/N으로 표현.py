def solution(N, number):
    dp = [set() for i in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        print(dp)
        for j in range(0, i): 
            for k in dp[j]:
                for l in dp[i-j]: # 사칙연산의 경우 모두 넣음
                    dp[i].add(k+l)
                    dp[i].add(k-l)
                    dp[i].add(k*l)
                    if k !=0 and l !=0: 
                        dp[i].add(k//l)
        if number in dp[i]: 
          
            return i
    return -1