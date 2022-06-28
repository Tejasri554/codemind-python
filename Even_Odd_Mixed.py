n=int(input())
l=len(str(n))
e=0
o=0
for i in range(1,l+1):
    r=n%10
    if r%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if l==e:
    print("Even")
elif l==o:
    print("Odd")
else:
    print("Mixed")