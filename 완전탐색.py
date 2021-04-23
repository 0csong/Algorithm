h=int(input())

count=0
for i in range(h+1): #h시까지
    for j in range(60): #j분
        for k in range(60):#k초
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)

#00시 00분 00초부터 h시 59분 59초까지 3이 포함되는 시간 개수
#str로 처리해서 가능함
