m=int(input())
n=int(input())
for i in range(m,n):
    temp=i
    reverse=0
    while temp>0:
        r=temp%10
        reverse=(reverse*10)+r
        temp=temp//10
    if i==reverse:
        print("%d "%i,end='')