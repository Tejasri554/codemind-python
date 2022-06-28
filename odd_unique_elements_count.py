n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i not in s:
       s.append(i)
       c=0
for i in s:
    if i%2!=0:
        c+=1
print(c)      