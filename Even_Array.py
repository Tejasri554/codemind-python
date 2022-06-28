n=int(input())
l=list(map(int,input().split()))
l1=len(l)
c=0
for i in l:
    if i%2==0:
        c+=1
if c==l1:
    print(True)
else:
    print(False)