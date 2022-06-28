n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in range(1,int(n/2)):
    s=s+l[i]
for i in range(int(n/2),n):
    s1=s1+l[i]
print(s1-s-1)    