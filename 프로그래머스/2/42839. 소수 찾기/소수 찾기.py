from itertools import permutations,combinations
import math

def isPrime(n):
    if n < 2:                                 
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    num=[]
    temp=[]
    
    for i in numbers:
        num.append(i)
        
    for i in range(1, len(num)+1):
        temp += list(permutations(num, i)) 

    number = [int(''.join(t)) for t in temp] 

    
    for i in number:
        if isPrime(i):
            answer.add(i)
 

    return len(answer)   