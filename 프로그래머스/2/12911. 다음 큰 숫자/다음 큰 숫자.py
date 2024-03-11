def check(x):
    binary = bin(x)
    one = binary.count('1')
    return one  

def solution(n):
  
    num = check(n)
    while True:
        n += 1
        if int(check(n)) == num:
            return n