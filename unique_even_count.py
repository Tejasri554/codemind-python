n=int(input())
l=list(map(int,input().split()))
s=[]
c=0
for i in l:
    if i not in s:
        s.append(i)
for i in s:
    if i%2==0:
        c=c+1
print(c)        