n=int(input ())
s=0
l=len(str(n))
for i in range (1,l+1):
    r=n%10
    s=s*10+r
    n=n//10
print (s)