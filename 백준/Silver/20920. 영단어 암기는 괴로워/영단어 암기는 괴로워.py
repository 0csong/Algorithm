import sys
input=sys.stdin.readline

n,m=map(int,input().split())
words={}
for i in range(n):
    word=input().rstrip()
    if len(word)<m:
        continue
    else:
        if word in words:
            words[word]+=1
        else:
            words[word]=1
words_sorted=sorted(words.items(),key=lambda x: (-x[1],-len(x[0]),x[0]))

for i,v in words_sorted:
    print(i)
