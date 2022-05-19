n=int(input())
l=len(str(n))
s=0
p=n*n
for i in range(1,l+1):
    r=p%10
    s=s*10+r
    p=p//10
l1=len(str(s))
t=0
for j in range (1,l1+1):
    q=s%10
    t=t*10+q
    s=s//10
if n==t:
    print("Automorphic Number")
else:    
    print("Not an Automorphic Number")