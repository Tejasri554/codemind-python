l=list(map(int,input().split()))
s=1
for i in l:
    s=s*i
print(int((2*s*512)/1024),end='KB')    