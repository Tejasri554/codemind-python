n=int(input())
l=len(str(n))
s=0
t=n
for i in range (1,l+1):
    r=n%10
    s=s+r
    n=n//10
if t%s==0:
    print(True)
else:
    print(False)