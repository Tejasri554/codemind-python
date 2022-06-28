n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for i in range(0,n):
    if i%2!=0:
        if l[i]%2!=0:
            c+=1
for i in l:
    if i%2!=0:
        s+=1
if c==s:
    print(True)
else:
    print(False)