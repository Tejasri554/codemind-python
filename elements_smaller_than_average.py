n=int(input())
l=list(map(int,input().split()))
s=sum(l)
r=(int(s/n))
c=0
for i in l:
    if i<=r:
        c+=1
print(c)      