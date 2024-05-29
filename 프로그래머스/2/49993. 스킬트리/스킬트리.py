def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        sk=""
        for ch in s:
            if ch in skill:
                sk+=ch
        if skill[:len(sk)]==sk:
            answer+=1
            
    return answer