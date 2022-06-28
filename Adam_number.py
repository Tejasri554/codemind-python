n=int(input())
t=n
p=n*n
s=0
l=len(str(n))
for i in range(1,l+1):
    r=n%10
    s=s*10+r
    n=n//10
p1=s*s
t1=p1
l1=len(str(p1))
s1=0
for j in range(1,l1+1):
    r1=p1%10
    s1=s1*10+r1
    p1=p1//10
if p==s1:
    print(True)
else:
    print(False)