n=int(input())
l=list(map(int,input().split()))
t=int(input())
s=0
for i in range(0,t):
    s=s+l[i]
print(s)    