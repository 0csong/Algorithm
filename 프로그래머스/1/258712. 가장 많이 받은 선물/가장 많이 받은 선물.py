def solution(friends, gifts):
    answer=0
    gifted={}
    gift_idx={}
    for friend in friends:
        gifted[friend]={}
        gift_idx[friend]=0
    for gift in gifts:
        t,f=gift.split(' ')# t: 선물을 준 사람, f: 받은 사람
        if f in gifted[t]:
            gifted[t][f]+=1
        else:
            gifted[t][f] = 1
        gift_idx[t] += 1
        gift_idx[f] -= 1
        will_get=[0 for _ in friends]
        for i in range(len(friends)):
            curr=friends[i]
            for j in range(i+1,len(friends)):
                another = friends[j] # 인덱스 j에 해당하는 친구
                # curr가 another에게 준 선물 개수
                a = gifted[curr][another] if another in gifted[curr] else 0 
                # another가 curr에게 준 선물 개수
                b = gifted[another][curr] if curr in gifted[another] else 0 
                if a > b: # curr가 선물을 더 많이 줬다면
                        will_get[i] += 1
                elif a < b: # another가 선물을 더 많이 줬다면
                    will_get[j] += 1
                elif a == b: # 둘이 선물을 주고 받은 개수가 같다면 선물 지수 확인
                    ai, bi = gift_idx[curr], gift_idx[another]
                    if ai > bi:
                        will_get[i] += 1
                    elif ai < bi:
                        will_get[j] += 1
    
    answer = max(will_get)
    return answer
            
        