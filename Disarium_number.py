n=int(input())
l=len(str(n))
s=0
t=n
for i in range(1,l+1):
    r=n%10
    s=s+r**(l-i+1)
    n=n//10
if s==t:
    print(True)
else:
    print(False)