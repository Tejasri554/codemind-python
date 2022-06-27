n=int(input())
m=0
for i in range (1,n):
    r=n%10
    if r>m:
        m=r
    n=n//10
print(m)    
