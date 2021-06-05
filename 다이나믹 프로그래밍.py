d=[0]*100 #리스트에 fibo의 값을 저장시킴

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0: #이미 계산했을경우 그대로 반환
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2) #아직계산하지 않은문제라면 피보나치 구동
    return d[x]

print(fibo(99))

#한번 계산한결과를 저장함으로써 메모리공간 낭비를 막음
