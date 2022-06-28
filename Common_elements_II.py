a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in range(0,a):
    if l1[i] not in l2:
        print(l1[i],end=' ')
for j in range(0,b):
     if l2[j] not in l1:
         print(l2[j],end=' ')