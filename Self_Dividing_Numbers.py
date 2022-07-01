n=int(input())
m=int(input())
for j in range(n,m+1):
    d=0
    p=0
    i=j
    while i>0:
        r=i%10
        i=i//10
        d+=1
        if r==0:
            continue
        if j%r==0:
            p+=1
    if p==d:
        print(j,end=' ')