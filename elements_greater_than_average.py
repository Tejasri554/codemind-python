n=int(input())
l=list(map(int,input().split()))
s=int(sum(l)/n)
c=0
for i in l:
    if s<=i:
        c+=1
print(c)        