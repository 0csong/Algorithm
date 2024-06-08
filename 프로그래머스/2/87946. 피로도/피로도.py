from itertools import permutations
 
def solution(k, dungeons):
    answer=0
    for p in permutations(dungeons,len(dungeons)):
        hp=k
        count=0
        for i in p:
            if hp>=i[0]:
                hp-=i[1]
                count+=1
            if count>answer:
                answer=count
    return answer

