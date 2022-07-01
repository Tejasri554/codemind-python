n=int(input())
l=len(str(n))
s=0
p=1
for i in range(l):
    r=n%10
    s=s+r
    p=p*r
    n=n//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")